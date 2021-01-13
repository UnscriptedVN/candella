#
# ASAppManager.rpy.rpy
# Candella
#
# Created by Marquis Kurt on 9/9/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

init 10 python:
    class ASAppManager(ASAppRepresentative):
        bundleName = "App Manager"
        bundleId = "dev.unscriptedvn.candella.app-manager"
        bundleDir = AS_DEFAULT_APP_DIR + "AppManager.aosapp/"
        bundleAuthor = "Project Alice and Unscripted Team"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            View the installed apps on Candella in detail and manage their permissions.
        """

        requires = { }

        def applicationWillLaunch(self):
            renpy.show_screen("ASAppManagerView")
            pass

        # Looks for all apps using AppKit and returns a list of them.
        def gatherAllApplications(self):
            import gc
            apps = []
            for obj in gc.get_objects():
                if isinstance(obj, ASAppRepresentative):
                    apps.append(obj)
            return apps

        def __init__(self):
            ASAppRepresentative.__init__(self, AS_DEFAULT_APP_DIR + "AppManager.aosapp/")

    appManager = ASAppManager()
