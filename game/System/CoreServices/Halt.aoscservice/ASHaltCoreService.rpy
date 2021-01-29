#
# ASHaltCoreService.rpy
# Candella
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init 5 python:
    import logging

    class ASHaltCoreService(ASCoreServiceRepresentative):
        bundleName = "Error Halt System"
        bundleId = "dev.unscriptedvn.candella.core-services.halt"
        bundleDir = AS_CORESERVICES_DIR + "Halt.aoscservice/"
        bundleAuthor = "Project Alice and Unscripted Team"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Safely catch system-level errors and restart Candella.
        """

        def halt(self, code=""):
            clog.error("Received Stop error code: %s. Halting and restarting.", code)
            renpy.call_screen("ASHaltMessage", error=code)
            # renpy.full_restart()

        def __init__(self):
            ASCoreServiceRepresentative.__init__(self, AS_CORESERVICES_DIR + "Halt.aoscservice/")

    ASHalt = ASHaltCoreService()
