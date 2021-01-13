#
# ASAppRepresentative.rpy
# Candella
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

# Set AliceOS permissions if they don't exist yet.
init -1000 python:
    if not persistent.AS_PERMISSIONS:
        persistent.AS_PERMISSIONS = {}

init python:

    # Class representation of an app on AliceOS.
    class ASAppRepresentative(object):

        # MARK: Manifest

        bundleName = "Bundle name"
        bundleId = "dev.unscriptedvn.candella.bundle"
        bundleDir = AS_APPS_DIR + "Bundle/"
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

        requires = {
            AS_REQUIRES_NOTIFICATIONKIT,
            AS_REQUIRES_FULL_DISK_ACCESS,
            AS_REQUIRES_SYSTEM_EVENTS
        }

        # MARK: Initialization

        # Initialize and create a blank template for permissions.
        def __init__(self, appDirectory):
            if self.bundleId not in persistent.AS_PERMISSIONS:
                persistent.AS_PERMISSIONS[self.bundleId] = {
                    AS_REQUIRES_NOTIFICATIONKIT: False,
                    AS_REQUIRES_FULL_DISK_ACCESS: False,
                    AS_REQUIRES_SYSTEM_EVENTS: False
                }
            else:
                if AS_REQUIRES_NOTIFICATIONKIT not in persistent.AS_PERMISSIONS[self.bundleId]:
                    persistent.AS_PERMISSIONS[self.bundleId][AS_REQUIRES_NOTIFICATIONKIT] = False

                if AS_REQUIRES_FULL_DISK_ACCESS not in persistent.AS_PERMISSIONS[self.bundleId]:
                    persistent.AS_PERMISSIONS[self.bundleId][AS_REQUIRES_FULL_DISK_ACCESS] = False

                if AS_REQUIRES_SYSTEM_EVENTS not in persistent.AS_PERMISSIONS[self.bundleId]:
                    persistent.AS_PERMISSIONS[self.bundleId][AS_REQUIRES_SYSTEM_EVENTS] = False

            self.bundleDir = appDirectory

            self.icons = {
                16: self.bundleDir + "Resources/Iconset/16.png",
                24: self.bundleDir + "Resources/Iconset/24.png",
                32: self.bundleDir + "Resources/Iconset/32.png",
                48: self.bundleDir + "Resources/Iconset/48.png",
                64: self.bundleDir + "Resources/Iconset/64.png",
                128: self.bundleDir + "Resources/Iconset/128.png",
                256: self.bundleDir + "Resources/Iconset/256.png"
            }

            pass


        # MARK: Permissions


        def requestPermission(self, forPermission):
            if forPermission in self.requires:
                store.tempPermission = False
                renpy.call_screen("ASPermissionRequest", bundleName=self.bundleName, requestingFor=forPermission, onAcceptRequest=[SetVariable("tempPermission", True), Return(0)])

                persistent.AS_PERMISSIONS[self.bundleId][forPermission] = store.tempPermission
                store.tempPermission = None
            else:
                print "The permission requested doesn't exist or isn't in the app's manifest."


        # Requests all permissions associated with the app.
        def requestAllPermissions(self):
            store.AS_REQUIRES_NOTIFICATIONKIT = False
            store.AS_REQUIRES_FULL_DISK_ACCESS = False
            store.AS_REQUIRES_SYSTEM_EVENTS = False

            if AS_REQUIRES_NOTIFICATIONKIT in self.requires:
                renpy.invoke_in_new_context(renpy.call_screen, "ASPermissionRequest", bundleName=self.bundleName, requestingFor=AS_REQUIRES_NOTIFICATIONKIT, onAcceptRequest=[SetVariable("AS_REQUIRES_NOTIFICATIONKIT", True), Return(0)])

            if AS_REQUIRES_FULL_DISK_ACCESS in self.requires:
                renpy.invoke_in_new_context(renpy.call_screen, "ASPermissionRequest", bundleName=self.bundleName, requestingFor=AS_REQUIRES_FULL_DISK_ACCESS, onAcceptRequest=[SetVariable("AS_REQUIRES_FULL_DISK_ACCESS", True), Return(0)])

            if AS_REQUIRES_SYSTEM_EVENTS in self.requires:
                renpy.invoke_in_new_context(renpy.call_screen, "ASPermissionRequest", bundleName=self.bundleName, requestingFor=AS_REQUIRES_SYSTEM_EVENTS, onAcceptRequest=[SetVariable("AS_REQUIRES_SYSTEM_EVENTS", True), Return(0)])

            persistent.AS_PERMISSIONS[self.bundleId] = {
                AS_REQUIRES_SYSTEM_EVENTS: store.AS_REQUIRES_SYSTEM_EVENTS,
                AS_REQUIRES_FULL_DISK_ACCESS: store.AS_REQUIRES_FULL_DISK_ACCESS,
                AS_REQUIRES_NOTIFICATIONKIT: store.AS_REQUIRES_NOTIFICATIONKIT
            }


        # MARK: Launch

        # Determine whether the app has been given permission to launch during boot.
        def applicationShouldLaunchAtLogin(self):
            if AS_REQUIRES_SYSTEM_EVENTS in self.requires:
                if persistent.AS_PERMISSIONS[self.bundleId] != None:
                    return persistent.AS_PERMISSIONS[self.bundleId][AS_REQUIRES_SYSTEM_EVENTS]
                else:
                    return False
            else:
                return False

        # Steps to take when running the app during the bootloader.
        def applicationWillLaunchAtLogin(self):
            return

        # Steps to take when starting the app.
        def applicationWillLaunch(self):
            print("WARN: %s (%s) doesn't have the applicationWillLaunch method implemented." % (self.bundleName, self.bundleId, ))
            pass

        # Steps to take when the app has finally finished launching.
        def applicationDidLaunch(self):
            return

        # Steps to take when the app is about to terminate.
        def applicationWillTerminate(self):
            return

        # Steps to take when the app is terminated.
        def applicationDidTerminate(self):
            return


        # MARK: Notifications


        # Determine whether the app can safely send a notification request.
        def applicationShouldRequestNotification(self):
            if AS_REQUIRES_NOTIFICATIONKIT in self.requires:
                if persistent.AS_PERMISSIONS[self.bundleId] == None:
                    return False
                else:
                    return persistent.AS_PERMISSIONS[self.bundleId][AS_REQUIRES_NOTIFICATIONKIT]
            else: return False
            return

        # Steps to take when the app is about to send a notification
        def applicationWillRequestNotification(self, message, withDetails, responseCallback=Return('didClickRespond')):
            if self.applicationShouldRequestNotification():
                notificationResponse = renpy.invoke_in_new_context(renpy.call_screen, "ASNotificationBanner", applet=self, message=message, withDetails=withDetails, responseCallback=responseCallback)
                self.applicationDidRequestNotification()
                return notificationResponse
            else:
                print "This app is not authorized to send notifications."
            return

        # Steps to take when the app is done sending a notification
        def applicationDidRequestNotification(self):
            return

        def applicationWillRequestBasicAlert(self, message, withDetails, onDismissCallback=Return('didDismissAlert')):
            if self.applicationShouldRequestNotification():
                notificationResponse = renpy.invoke_in_new_context(renpy.call_screen, "ASNotificationAlert", message=message, withDetails=withDetails, onDismissCallback=onDismissCallback)
                self.applicationDidRequestAlert()
                return notificationResponse
            else:
                print "This app is not authorized to send notifications."
            return

        def applicationWillRequestExtendedAlert(self, message, withDetails, primaryActionText, onPrimaryCallback=Return('didClickPrimary'), secondaryActionText=None, onSecondaryCallback=Return('didClickSecondary')):
            if self.applicationShouldRequestNotification():
                renpy.invoke_in_new_context(renpy.call_screen, "ASNotificationAlert", message=message, withDetails=withDetails, primaryActionText=primaryActionText, onPrimaryCallback=onPrimaryCallback, secondaryActionText=secondaryActionText, onSecondaryCallback=onSecondaryCallback)
                self.applicationDidRequestAlert()
            else:
                print "This app is not authorized to send notifications."
            return

        def applicationDidRequestAlert(self):
            return
