#
# ASSysInfoCoreService.rpy
# Candella
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init 5 python:

    class ASSysInfoApp(CAApplication):

        def __init__(self):
            CAApplication.__init__(self, AS_DEFAULT_APP_DIR + "SysInfo.aosapp/")

        def applicationWillLaunch(self):
            renpy.show_screen("ASSysInfoView")


    ASSysInfo = ASSysInfoApp()
