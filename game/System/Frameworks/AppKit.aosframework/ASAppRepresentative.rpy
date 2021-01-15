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
        """The base class that represents an application in AliceOS/Candella.
        
        To maintain compatibility with AliceOS apps using ASAppRepresentative, the original method
            names are retained in addition to their Pythonic counterparts.
        """

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

        requires = {}

        # MARK: Initialization

        def __init__(self, appDirectory):
            """Initialize and create a blank template for permissions."""
            
            if self.bundleId not in persistent.AS_PERMISSIONS:
                persistent.AS_PERMISSIONS[self.bundleId] = {}
            else:
                for require in self.requires:
                    if require not in persistent.AS_PERMISSIONS[self.bundleId]:
                        persistent.AS_PERMISSIONS[self.bundleId][require] = False

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

        # MARK: Permissions

        def requestPermission(self, forPermission):
            if forPermission in self.requires:
                store.tempPermission = False
                renpy.call_screen(
                    "ASPermissionRequest",
                    bundleName=self.bundleName,
                    requestingFor=forPermission,
                    onAcceptRequest=[SetVariable("tempPermission", True), Return(0)]
                )

                persistent.AS_PERMISSIONS[self.bundleId][forPermission] = store.tempPermission
                store.tempPermission = None
            else:
                print "The permission requested doesn't exist or isn't in the app's manifest."
                
        def request_permission(self, for_permission):
            """Request for a specific permission.
            
            Arguments:
                for_permission (str): The name of the permission to request by the user.
            """
            self.requestPermission(for_permissions)


        # Requests all permissions associated with the app.
        def requestAllPermissions(self):
            store.AS_REQUIRES_NOTIFICATIONKIT = False
            store.AS_REQUIRES_FULL_DISK_ACCESS = False
            store.AS_REQUIRES_SYSTEM_EVENTS = False

            if AS_REQUIRES_NOTIFICATIONKIT in self.requires:
                renpy.invoke_in_new_context(
                    renpy.call_screen,
                    "ASPermissionRequest",
                    bundleName=self.bundleName,
                    requestingFor=AS_REQUIRES_NOTIFICATIONKIT,
                    onAcceptRequest=[SetVariable("AS_REQUIRES_NOTIFICATIONKIT", True), Return(0)]
                )

            if AS_REQUIRES_FULL_DISK_ACCESS in self.requires:
                renpy.invoke_in_new_context(
                    renpy.call_screen,
                    "ASPermissionRequest",
                    bundleName=self.bundleName,
                    requestingFor=AS_REQUIRES_FULL_DISK_ACCESS,
                    onAcceptRequest=[SetVariable("AS_REQUIRES_FULL_DISK_ACCESS", True), Return(0)]
                )

            if AS_REQUIRES_SYSTEM_EVENTS in self.requires:
                renpy.invoke_in_new_context(
                    renpy.call_screen,
                    "ASPermissionRequest",
                    bundleName=self.bundleName,
                    requestingFor=AS_REQUIRES_SYSTEM_EVENTS,
                    onAcceptRequest=[SetVariable("AS_REQUIRES_SYSTEM_EVENTS", True), Return(0)]
                )

            persistent.AS_PERMISSIONS[self.bundleId] = {
                AS_REQUIRES_SYSTEM_EVENTS: store.AS_REQUIRES_SYSTEM_EVENTS,
                AS_REQUIRES_FULL_DISK_ACCESS: store.AS_REQUIRES_FULL_DISK_ACCESS,
                AS_REQUIRES_NOTIFICATIONKIT: store.AS_REQUIRES_NOTIFICATIONKIT
            }
            
        def request_all_permissions(self):
            """Request for all permissions this app requires."""
            self.requestAllPermissions()

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
                
        def application_should_launch_at_login(self):
            """Returns whether the application has permissions to launch during boot."""
            return self.applicationShouldLaunchAtLogin()

        # Steps to take when running the app during the bootloader.
        def applicationWillLaunchAtLogin(self):
            return
            
        def application_will_launch_at_login(self):
            """Perform tasks that the app will need when the bootloader is called."""
            self.applicationWillLaunchAtLogin()

        # Steps to take when starting the app.
        def applicationWillLaunch(self):
            print("WARN: %s (%s) doesn't have the applicationWillLaunch method implemented." 
                    % (self.bundleName, self.bundleId, ))
            pass
            
        def application_will_launch(self):
            """Perform pre-startup tasks for this app."""
            self.applicationWillLaunch()

        # Steps to take when the app has finally finished launching.
        def applicationDidLaunch(self):
            return
            
        def application_did_launch(self):
            """Perform post-launch tasks for this app."""
            self.applicationDidLaunch()

        # Steps to take when the app is about to terminate.
        def applicationWillTerminate(self):
            return
            
        def application_will_terminate(self):
            """Perform pre-termination tasks for this app."""
            self.applicationWillTerminate()

        # Steps to take when the app is terminated.
        def applicationDidTerminate(self):
            return
            
        def application_did_terminate(self):
            """Perform post-termination tasks for this app."""
            self.applicationDidTerminate()
            
        # MARK: File System
        
        def applicationShouldRequestData(self):
            """Returns whether the application should request data."""
            if AS_REQUIRES_FULL_DISK_ACCESS not in self.requires:
                return False
            if self.bundleId not in persistent.AS_PERMISSIONS:
                return False
            return persistent.AS_PERMISSIONS[self.bundleId][AS_REQUIRES_FULL_DISK_ACCESS]
            
        def application_should_request_data(self):
            return self.applicationShouldRequestData()


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
            
        def application_should_request_notification(self):
            """Returns whether the app can safely make a notification request."""
            return self.applicationShouldRequestNotification()

        # Steps to take when the app is about to send a notification
        def applicationWillRequestNotification(self, message, withDetails, responseCallback=Return('didClickRespond')):
            if self.applicationShouldRequestNotification():
                notificationResponse = renpy.invoke_in_new_context(
                                        renpy.call_screen,
                                        "ASNotificationBanner",
                                        applet=self,
                                        message=message,
                                        withDetails=withDetails,
                                        responseCallback=responseCallback
                                    )
                self.applicationDidRequestNotification()
                return notificationResponse
            else:
                print "This app is not authorized to send notifications."
            return
            
        def application_will_request_notification(self, message, with_details, response_callback=Return('didClickRespond')):
            """Request a banner alert.
            
            Arguments:
                message (str): The title of the banner.
                with_details (str): The supporting text for the banner.
                response_callback (callable): The callback response function when clicking 'Dismiss' or 'Respond'.
            
            Returns:
                response (any): The response from the notification, or None if the request was denied.
            """
            return self.applicationWillRequestNotification(message, with_details, responseCallback=response_callback)

        # Steps to take when the app is done sending a notification
        def applicationDidRequestNotification(self):
            return
            
        def application_did_request_notification(self):
            """Perform any post-notification request tasks."""
            self.applicationDidRequestNotification()

        def applicationWillRequestBasicAlert(self, message, withDetails, onDismissCallback=Return('didDismissAlert')):
            if self.applicationShouldRequestNotification():
                notificationResponse = renpy.invoke_in_new_context(
                    renpy.call_screen,
                    "ASNotificationAlert",
                    message=message,
                    withDetails=withDetails,
                    onDismissCallback=onDismissCallback
                )
                self.applicationDidRequestAlert()
                return notificationResponse
            else:
                print "This app is not authorized to send notifications."
            return
            
        def application_will_request_basic_alert(self, message, with_details, on_dismiss_callback=Return('didDismissAlert')):
            """Request a notification alert.
            
            Arguments:
                message (str): The title of the alert.
                with_details (str): The supporting text for the alert.
                on_dismiss_callback (callable): The callback response function when dismissing the alert.
                
            Returns:
                response (any): The response from the alert, or None if not permitted.
            """
            return self.applicationWillRequestBasicAlert(
                message,
                with_details,
                onDismissCallback=on_dismiss_callback
            )

        def applicationWillRequestExtendedAlert(
            self,
            message,
            withDetails,
            primaryActionText,
            onPrimaryCallback=Return('didClickPrimary'),
            secondaryActionText=None,
            onSecondaryCallback=Return('didClickSecondary')
        ):
            if self.applicationShouldRequestNotification():
                renpy.invoke_in_new_context(
                    renpy.call_screen,
                    "ASNotificationAlert",
                    message=message,
                    withDetails=withDetails,
                    primaryActionText=primaryActionText,
                    onPrimaryCallback=onPrimaryCallback,
                    secondaryActionText=secondaryActionText,
                    onSecondaryCallback=onSecondaryCallback
                )
                self.applicationDidRequestAlert()
            else:
                print "This app is not authorized to send notifications."
            return
            
        def application_will_request_extended_alert(
            self,
            message,
            with_details,
            primary_action_text,
            on_primary_callback=Return('didClickPrimary'),
            secondary_action_text=None,
            on_secondary_callback=Return('didClickSecondary')
        ):
            """Request an extended alert.
            
            Arguments:
                message (str): The title of the alert.
                with_details (str): The supporting text for the alert.
                primary_action_text (str): The primary action button's text.
                on_primary_callback (callable): The callback response function when clicking the primary action.
                secondary_action_text (str): The secondary action button's text.
                on_secondary_callback (callable): The callback response function when clicking the secondary action.
                
            Returns:
                response (any): The response from the alert, or None if not permitted.
            """
            return self.applicationWillRequestExtendedAlert(
                message,
                with_details,
                primary_action_text,
                onPrimaryCallback=on_primary_callback,
                secondary_action_text=secondaryActionText,
                onSecondaryCallback=on_secondary_callback
            )

        def applicationDidRequestAlert(self):
            return
            
        def application_did_request_alert(self):
            """Perform any post-alert tasks."""
            return self.applicationDidRequestAlert()
