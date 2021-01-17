#
# CabertoDE.rpy
# Caberto Desktop Shell
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = 5

init python:
    import gc
    from time import gmtime, strftime
    
    class CabertoShell(ASCoreServiceRepresentative):
        bundleName = "Caberto Shell"
        bundleId = "dev.unscriptedvn.candella.caberto"
        bundleDir = AS_CORESERVICES_DIR + "Caberto.aoscservice/"
        bundleAuthor = "Marquis Kurt <software@marquiskurt.net>"
        bundleVersion = "1.0.0"
        bundleDescription = "A Unity/Lomiri-inspired desktop shell for Candella."
        
        _acct_mgr = CAAccountsService()
        
        @staticmethod
        def get_all_applications():
            """Returns all of the installed apps on the system."""
            return [app for app in gc.get_objects() if isinstance(app, ASAppRepresentative)]
        
        @staticmethod
        def current_time():
            """Returns the current time of the system."""
            return strftime("%I:%M%p")
            
        def __init__(self):
            ASCoreServiceRepresentative.__init__(self, AS_CORESERVICES_DIR + "Caberto.aoscservice/")
            self.settings = ServiceStorage(self)
                        
            if not self.settings.read("apps_list"):
                self.settings.write_field("apps_list", self._default_apps())
                self.settings.write()
            if not self.settings.read("wallpaper"):
                self.settings.write_field("wallpaper", AS_LIBRARY_DIR + "Desktop Pictures/Candella.png")
                self.settings.write()
            
        def launch(self):
            """Launch the desktop with the user's settings."""
            apps = self.settings.read_not_none("apps_list")
            wallpaper = self.settings.read_not_none("wallpaper")
            renpy.call_screen("CabertoShellView", wallpaper=wallpaper, apps=self._get_dock_apps(apps))
            
        def _default_apps(self):
            """Returns the list of default apps to load into the launcher."""
            # TODO: Complete this stub.
            return [
                "dev.unscriptedvn.candella.app-manager"
            ]
            
        def _get_dock_apps(self, apps):
            return [app for app in CabertoShell.get_all_applications() if app.bundleId in apps]
    
    caberto = CabertoShell()
