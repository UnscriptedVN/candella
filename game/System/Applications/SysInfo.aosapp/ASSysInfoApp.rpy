#
# ASSysInfoCoreService.rpy
# Candella
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init 5 python:

    class ASSysInfoApp(ASAppRepresentative):
        bundleName = "About Candella"
        bundleId = "dev.unscriptedvn.candella.sysinfo"
        bundleDir = AS_DEFAULT_APP_DIR + "SysInfo.aosapp/"
        bundleAuthor = "Project Alice and Unscripted Team"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            View System Information about Candella.
        """

        requires = { }

        def applicationWillLaunch(self):
            renpy.show_screen("ASSysInfoView")

        def __init__(self):
            ASAppRepresentative.__init__(self, AS_DEFAULT_APP_DIR + "SysInfo.aosapp/")

    ASSysInfo = ASSysInfoApp()
