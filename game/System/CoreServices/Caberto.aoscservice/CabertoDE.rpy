#
# CabertoDE.rpy
# Caberto Desktop Shell
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = 5

init python:
    import gc
    from os import listdir, path
    from time import gmtime, strftime
    
    class CabertoShell(ASCoreServiceRepresentative):
        bundleName = "Caberto Shell"
        bundleId = "dev.unscriptedvn.candella.caberto"
        bundleDir = AS_CORESERVICES_DIR + "Caberto.aoscservice/"
        bundleAuthor = "Marquis Kurt <software@marquiskurt.net>"
        bundleVersion = "1.0.0"
        bundleDescription = "A Unity/Lomiri-inspired desktop shell for Candella."
        
        _acct_mgr = CAAccountsService()
        _wallpaper = AS_LIBRARY_DIR + "Desktop Pictures/Candella.png"
        
        _drawer_open = False
        
        @staticmethod
        def wallpapers():
            """A list containing the names of all of the wallpapers available to Candella."""
            isimage = lambda pic: pic.endswith(".png")
            
            return [
                pic.replace(".png", "") for pic in\
                    listdir(config.basedir + "/game/" + AS_LIBRARY_DIR + "/Desktop Pictures/")\
                    if isimage(pic)
            ]
        
        @staticmethod
        def get_all_applications():
            """Returns all of the installed apps on the system."""
            is_app = lambda app: isinstance(app, ASAppRepresentative) or isinstance(app, CAApplication)
            return [app for app in gc.get_objects() if is_app(app)]
        
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
            
            self._wallpaper = self.settings.read_not_none("wallpaper")
            
        def launch(self):
            """Launch the desktop with the user's settings."""
            apps = self.settings.read_not_none("apps_list")
            renpy.call_screen("CabertoShellView", wallpaper=self._wallpaper, apps=self._get_dock_apps(apps))
            
        def drawer(self):
            """Toggle the app drawer."""
            self._drawer_open = not self._drawer_open
            
            if self._drawer_open:
                renpy.run(ShowTransient("CabertoDrawer"))
            else:
                renpy.run(Hide("CabertoDrawer"))
            
        def _default_apps(self):
            """Returns the list of default apps to load into the launcher."""
            # TODO: Complete this stub.
            return [
                "dev.unscriptedvn.candella.app-manager"
            ]
            
        def _get_dock_apps(self, apps):
            """Returns the list of app objects that is in the dock."""
            return [app for app in CabertoShell.get_all_applications() if app.bundleId in apps]
            
        def _set_wallpaper(self, name):
            """Set the wallpaper and save the preference."""
            self._wallpaper = AS_LIBRARY_DIR + "Desktop Pictures/" + name + ".png"
            self.settings.write_field("wallpaper", self._wallpaper)
            self.settings.write()
    
    caberto = CabertoShell()
