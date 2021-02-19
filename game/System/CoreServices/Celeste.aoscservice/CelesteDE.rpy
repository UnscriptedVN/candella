#
# CelesteDE.rpy
# Celeste Desktop Shell
#
# (C) 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 5

init python:
    import gc
    import logging
    from os import listdir, path
    from time import gmtime, strftime
    from store.CADeprecated import deprecated
    from store import CADesign as design

    class CelesteShell(CACoreService):
        _wallpaper = AS_LIBRARY_DIR + "Desktop Pictures/Candella.png"
        _wall_display_mode = "cover"
        _dock = []
        _drawer_open = False
        _current_app_name = "Celeste Desktop"
        _acct_switcher_open = False

        def __init__(self):
            CACoreService.__init__(self, AS_CORESERVICES_DIR + "Celeste.aoscservice/")
            self._acct_mgr = CAAccountsService(self)

            self.settings = ServiceStorage(self)

            if not self.settings.get_entry("apps_list"):
                self.settings.set_entry("apps_list", self._default_apps())
                self.settings.commit()
            self._dock = self.settings.get_entry("apps_list", raise_falsy=True)

            if not self.settings.get_entry("wallpaper"):
                self.settings.set_entry("wallpaper", AS_LIBRARY_DIR + "Desktop Pictures/Candella.png")
                self.settings.commit()
            self._wallpaper = self.settings.get_entry("wallpaper", raise_falsy=True)

            if not self.settings.get_entry("display_mode"):
                self.settings.set_entry("display_mode", "cover")
                self.settings.commit()
            self._wall_display_mode = self.settings.get_entry("display_mode", raise_falsy=True)

            apps = CelesteShell.get_all_applications()
            for app in CelesteShell.get_all_applications():
                if not isinstance(app, CAApplication):
                    clog.warn("%s cannot emit signals and will be ignored.", app.bundleName)
                    continue
                app.register_event(self._app_listen)

        @staticmethod
        def wallpapers():
            """A list containing the names of all of the wallpapers available to Candella."""
            return [
                fil.replace(".png", "").replace(AS_LIBRARY_DIR + "Desktop Pictures/", "") \
                for fil in renpy.list_files() \
                if fil.startswith(AS_LIBRARY_DIR + "Desktop Pictures/") and fil.endswith(".png")
            ]

        @staticmethod
        def get_all_applications():
            """Returns all of the installed apps on the system."""
            return [
                app for app in gc.get_objects() if isinstance(app, CAApplication) or isinstance(app, ASAppRepresentative)
            ]

        @staticmethod
        def current_time():
            """Returns the current time of the system."""
            return strftime("%I:%M%p")

        @deprecated('21.02', renamed='CADesign.get_app_mask_frame')
        def get_app_mask(self):
            return design.get_app_mask_frame()

        def get_distributor_logo(self):
            if not renpy.loadable("System/Library/Branding/sprite_alt.png"):
                return self.bundleDir + "Resources/distributor_logo.png"
            return "System/Library/Branding/sprite_alt.png"

        def app_exists_in_current_launcher(self, app_id):
            """Returns if a given app bundle ID is in the current user's dock."""
            return app_id in self._dock

        def launch(self, transient=False):
            """Launch the desktop with the user's settings.

            Args:
                transient (bool): Whether to show the screen transiently. Defaults to false.
            """
            self.serviceWillLaunch()
            apps = self._get_dock_apps(self._dock)

            if transient:
                renpy.run(
                    ShowTransient(
                        "CelesteShellView", wallpaper=self._wallpaper,
                        apps=apps
                    )
                )
            else:
                renpy.call_screen(
                    "CelesteShellView", wallpaper=self._wallpaper,
                    apps=apps
                )
            self.serviceDidLaunch()
            self.emit_signal("service_launched", name=self.name)

        def launch_app(self, app_id):
            """Launch an app with a given app bundle ID.

            Arguments:
                app_id (str): The bundle ID of the app to launch.
            """
            app_target = [app for app in CelesteShell.get_all_applications() if app.bundleId == app_id]
            if not app_target:
                clog.error("Failed to launch app '%s'", app_id)
            app = app_target[0]
            self.launch_app_bundle(app)

        def launch_app_bundle(self, app_bundle):
            """Launch a specific app bundle.

            Arguments:
                app_bundle: The app bundle to launch.
            """

            if isinstance(app_bundle, CAApplication):
                app_bundle.launch()
            elif isinstance(app_bundle, ASAppRepresentative):
                app_bundle.applicationWillLaunch()
            else:
                clog.error("'%s' has no suitable launch method or is not an app.", app_id)

        def drawer(self):
            """Toggle the app drawer."""
            self._drawer_open = not self._drawer_open

            if self._drawer_open:
                renpy.run(ShowTransient("CelesteDrawer"))
            else:
                renpy.run(Hide("CelesteDrawer"))

        def start_acct_manager(self):
            """Call the account switcher dialog."""
            if self._acct_switcher_open:
                clog.error("Account switcher is already active.")
                return

            if len(CAAccountsService.get_all_users()) < 2:
                clog.error("There aren't any other users on the system.")
                return

            self._acct_switcher_open = True
            username = renpy.invoke_in_new_context(
                renpy.call_screen, "CelesteAccountSwitcher", users=CAAccountsService.get_all_users()
            )
            self._acct_switcher_open = False

            if type(username) is not str:
                clog.debug("User has requested to cancel or the username is invalid. Type: %s", username)
                return

            self._acct_mgr.change_current_user(username)

            renpy.run([Hide("CelesteShellView"), Hide("CelesteLauncher")])
            clog.debug("Reloading Celeste settings to current user.")

            self._init_settings()
            self.launch(transient=True)

        def _init_settings(self):
            self.settings = ServiceStorage(self)

            if not self.settings.get_entry("apps_list"):
                self.settings.set_entry("apps_list", self._default_apps())
                self.settings.commit()
            self._dock = self.settings.get_entry("apps_list", raise_falsy=True)

            if not self.settings.get_entry("wallpaper"):
                self.settings.set_entry("wallpaper", AS_LIBRARY_DIR + "Desktop Pictures/Candella.png")
                self.settings.commit()
            self._wallpaper = self.settings.get_entry("wallpaper", raise_falsy=True)

        def _default_apps(self):
            """Returns the list of default apps to load into the launcher."""
            return [
                "dev.unscriptedvn.candella.app-manager",
                "dev.unscriptedvn.candella.inventories",
                "dev.unscriptedvn.candella.glossary"
            ]

        def _get_dock_apps(self, apps):
            """Returns the list of app objects that is in the dock."""
            return [app for app in CelesteShell.get_all_applications() if app.bundleId in apps]

        def _set_wallpaper(self, name):
            """Set the wallpaper and save the preference."""
            self._wallpaper = AS_LIBRARY_DIR + "Desktop Pictures/" + name + ".png"
            self.settings.set_entry("wallpaper", self._wallpaper)
            self.settings.commit()

        def _update_wallpaper_display_mode(self, mode):
            if mode not in ["contain", "cover", "fill"]:
                clog.error("Not a valid display mode: %s.", mode)
                return
            self._wall_display_mode = mode
            self.settings.set_entry("display_mode", self._wall_display_mode)
            self.settings.commit()

        def _app_listen(self, *args, **kwargs):
            # Handle the title section on the desktop.
            if "application_launched" in args:
                self._current_app_name = kwargs["name"]
            elif "application_terminated" in args:
                self._current_app_name = "Celeste Desktop"

            # Handle app pinning from the App Manager.
            elif "__appman_pin" in args:
                app_id = kwargs["app"]
                if app_id in self._dock:
                    return
                self._dock.append(app_id)
                self.settings.set_entry("apps_list", self._dock)
                self.settings.commit()
                renpy.run([Hide("CelesteShellView"), Function(self.launch, transient=True)])

            # Handle app unpinning from the App Manager.
            elif "__appman_unpin" in args:
                app_id = kwargs["app"]
                if app_id not in self._dock:
                    return
                self._dock.remove(app_id)
                self.settings.set_entry("apps_list", self._dock)
                self.settings.commit()
                renpy.run([Hide("CelesteShellView"), Function(self.launch, transient=True)])

    celeste = CelesteShell()
