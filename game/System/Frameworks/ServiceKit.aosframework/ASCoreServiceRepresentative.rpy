#
# ASCoreServiceRepresentative.rpy
# Candella
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init -20 python:

    class ASCoreServiceRepresentative(object):
        bundleName = "Bundle name"
        bundleId = "dev.unscriptedvn.candella.bundle"
        bundleDir = AS_CORESERVICES_DIR + "Bundle/"
        bundleAuthor = "Author"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            No description has been provided.
        """

        icons = {
            16: bundleDir + "Resources/Iconset/16.png",
            24: bundleDir + "Resources/Iconset/24.png",
            32: bundleDir + "Resources/Iconset/32.png",
            64: bundleDir + "Resources/Iconset/64.png",
            128: bundleDir + "Resources/Iconset/128.png",
            256: bundleDir + "Resources/Iconset/256.png"
        }

        def __init__(self, appDirectory):

            self.bundleDir = appDirectory

            self.icons = {
                16: self.bundleDir + "Resources/Iconset/16.png",
                24: self.bundleDir + "Resources/Iconset/24.png",
                32: self.bundleDir + "Resources/Iconset/32.png",
                64: self.bundleDir + "Resources/Iconset/64.png",
                128: self.bundleDir + "Resources/Iconset/128.png",
                256: self.bundleDir + "Resources/Iconset/256.png"
            }

            pass

        # Steps to take when starting the app.
        def serviceWillLaunch(self):
            return

        # Steps to take when the app has finally finished launching.
        def serviceDidLaunch(self):
            return

        # Steps to take when the app is about to terminate.
        def serviceWillTerminate(self):
            return

        # Steps to take when the app is terminated.
        def serviceDidTerminate(self):
            return

        # Determine whether the app can safely send a notification request.
        def serviceShouldRequestNotification(self):
            return True

        # Steps to take when the app is about to send a notification
        def serviceWillRequestNotification(self, message, withDetails, responseCallback=Return(0)):
            if self.serviceShouldRequestNotification():
                renpy.call_screen("ASNotificationBanner", applet=self, message=message, withDetails=withDetails, responseCallback=responseCallback)
                self.serviceDidRequestNotification()
            else:
                print "This service is not authorized to send notifications."
            return

        # Steps to take when the app is done sending a notification
        def serviceDidRequestNotification(self):
            return
