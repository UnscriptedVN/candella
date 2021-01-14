#
# ASAppManager.rpy
# Candella
#
# Created by Marquis Kurt on 9/9/19
# Copyright © 2019-2021 Marquis Kurt. All rights reserved.
#

init 10 python:
    class ASAppManager(CAApplication):
    
        def applicationWillLaunch(self):
            renpy.show_screen("ASAppManagerView")
            pass

        def gather_applications(self):
            """Returns a list of all of the gathered applications."""
            import gc
            apps = []
            for obj in gc.get_objects():
                if isinstance(obj, ASAppRepresentative):
                    apps.append(obj)
            return apps
            
        def get_app_name(self, app):
            if isinstance(app, CAApplication):
                return app.get_name()
            return app.bundleName

        def __init__(self):
            CAApplication.__init__(self, AS_DEFAULT_APP_DIR + "AppManager.aosapp/")

    appManager = ASAppManager()
