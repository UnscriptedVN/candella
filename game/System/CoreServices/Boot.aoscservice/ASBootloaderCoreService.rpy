#
# ASBootloaderCoreService.rpy
# Candella
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init 5 python:

    from threading import Thread
    from os import path
    import logging

    class ASBootloaderCoreService(ASCoreServiceRepresentative):
        bundleName = "Bootloader"
        bundleId = "dev.unscriptedvn.candella.core-services.boot"
        bundleDir = AS_CORESERVICES_DIR + "Boot.aoscservice/"
        bundleAuthor = "Project Alice and Unscripted Team"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Show a loading screen for Candella.
        """

        # Looks for all apps using AppKit and returns a list of them.
        def gatherAllApplications(self):
            import gc
            apps = []
            for obj in gc.get_objects():
                if isinstance(obj, ASAppRepresentative):
                    apps.append(obj)
            return apps

        def startLoginMethod(self, app):
            if app.applicationShouldLaunchAtLogin is not None and app.applicationShouldLaunchAtLogin():
                app.applicationWillLaunchAtLogin()
            else:
                if AS_REQUIRES_SYSTEM_EVENTS in app.requires and not app.applicationShouldLaunchAtLogin():
                    logging.warn("%s cannot run its login service because it doesn't have permission to do so.", app.bundleName)
                else:
                    logging.debug("%s doesn't have a defined login service. Skipped.", app.bundleId)

        def boot(self, timeout=5, expressSetup=True, disclaimer=None, bootView="ASBootloaderView"):
            if not persistent.AS_COMPLETED_SETUP:
                ASSetup.startSetup(express=expressSetup, disclaimer=disclaimer)

            for app in self.gatherAllApplications():
                appProcess = Thread(target=self.startLoginMethod, args=(app, ))
                appProcess.start()
                appProcess.join()


            renpy.call_screen(bootView, timeout=timeout)

        def __init__(self):
            ASCoreServiceRepresentative.__init__(self, AS_CORESERVICES_DIR + "Boot.aoscservice/")
            
            if not path.isdir(config.savedir + "/.causerland"):
                logging.error("Userland folder is missing. Re-running Setup Assistant.")
                persistent.AS_COMPLETED_SETUP = False

    ASBootloader = ASBootloaderCoreService()
