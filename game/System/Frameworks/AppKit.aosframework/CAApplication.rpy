#
# CAApplication.rpy
# Candella
#
# Created by Marquis Kurt on 1/13/21.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#

init python:
    from store.CAFrameworkLoader import get_framework_names
    import json
    import logging

    class CAApplication(ASAppRepresentative, CAObservable):
        """The class used for Candella apps.

        CAApplication is an extension of the standard ASAppRepresentative class and aims to make app development
            simpler. This class provides extra utilities to simplify app development.

        Differences Between ASAppRepresentative:
            - Apps do not need to override class attributes to fill out app metadata. Instead, this is achieved with
                a manifest file, manifest.json.
            - Notification requests are handled by methods that simplify calls.
            - Grabbing icon sizes for an app is handled with a method.
            - The description field for the app includes information regarding AliceOS compatibility.
            - The license, product name, permissions, and description fields are present.
            - This class contains methods for accessing user data via the Multiuser framework.
            - This class inherits the CAObservable class, which will emit signals to services or apps that listen for
                it.

        Class Attributes:
            description (str): The description for the app (same as bundleDescription).
            product_name (str): The human-readable name of the app.
            license (str): The license this app falls under.
            permissions (list): A list containing all of the permissions this app needs.
            data (AppStorage): An app storage object for this app, or None if the app doesn't need app storage.
        """

        _warn_text = "\n\nThis app is made for the Candella distribution and may not be compatible with AliceOS."

        description = ""
        product_name = ""
        license = "No license provided."
        permissions = []
        data = None

        def __init__(self, app_path):
            """Initialize a Candella app.

            Arguments:
                app_directory: The path to the Candella app file.
            """

            # Initialize the AliceOS-compatible app.
            self.bundleDir = app_path

            self.icons = {
                16: self.bundleDir + "Resources/Iconset/16.png",
                24: self.bundleDir + "Resources/Iconset/24.png",
                32: self.bundleDir + "Resources/Iconset/32.png",
                48: self.bundleDir + "Resources/Iconset/48.png",
                64: self.bundleDir + "Resources/Iconset/64.png",
                128: self.bundleDir + "Resources/Iconset/128.png",
                256: self.bundleDir + "Resources/Iconset/256.png"
            }

            self.requisites = []

            # Load the manifest, if there is one.
            try:
                self._initialize_manifest()
            except Exception as problem:
                logging.warn(
                    "A problem occurred when reading the manifest for %s: %s",
                    self.__class__.__name__,
                    problem
                )

            # Perform the regular AliceOS permission inits if the manifest failed to load.
            if self.bundleId not in persistent.AS_PERMISSIONS:
                persistent.AS_PERMISSIONS[self.bundleId] = {}
            else:
                for require in self.requires:
                    if require not in persistent.AS_PERMISSIONS[self.bundleId]:
                        persistent.AS_PERMISSIONS[self.bundleId][require] = False

            # Add the compatibility notice to the description of the app.
            self.bundleDescription += self._warn_text
            self.description += self._warn_text

            # Load the app's storage files if the app has file system permissions.
            if "file_system" in self.permissions or \
                ("REQ_FILL_DISK" in persistent.AS_PERMISSIONS[self.bundleId] and \
                    persistent.AS_PERMISSIONS[self.bundleId]["REQ_FULL_DISK"]):
                self.data = AppStorage(self)

            self._validate_requisites()

        def applicationWillTerminate(self):
            if isinstance(self.data, AppStorage):
                self.data.commit()
            self.emit_signal("application_terminated")

        def _initialize_manifest(self):
            manifest = {}
            if not renpy.loadable(self.bundleDir + "manifest.json"):
                raise Exception("Manifest file not found: %s" % (self.bundleDir + "manifest.json"))

            with renpy.file(self.bundleDir + "manifest.json") as file:
                manifest = json.load(file)

            self.bundleName = self.name = manifest["name"]
            self.bundleProductName = self.product_name = \
                manifest["productName"] if "productName" in manifest else self.name
            self.bundleId = self.id = manifest["id"]
            self.bundleAuthor = self.author = manifest["author"]
            self.bundleVersion = self.version = manifest["version"]
            self.bundleDescription = self.description = manifest["description"]
            self.license = manifest["license"]

            if "requisites" in manifest:
                self.requisites = manifest["requisites"]

            self.permissions = manifest["permissions"]

            if self.bundleId in persistent.AS_PERMISSIONS:
                return

            for permission in manifest["permissions"]:
                if permission not in CA_PERMISSIONS:
                    continue
                permission_data = CA_PERMISSIONS[permission]
                self.requires[permission_data.key] = True
                persistent.AS_PERMISSIONS[self.id][permission_data.key] = permission_data.default_state

        def _validate_requisites(self):
            all_frameworks = get_framework_names()
            if not self.requisites:
                clog.warning("Requisite frameworks for %s are not defined. Skipping validation.", self.id)
                return
            for requisite in self.requisites:
                clog.debug("Checking requisite framework %s for %s.", requisite, self.id)
                if requisite not in all_frameworks:
                    clog.error("Requisite framework for %s is missing: %s.", self.id, requisite)
                    continue
            clog.info("Requisites have been validated for app %s.", self.id)

        def get_name(self):
            """Returns the name of the app, or its bundle name."""
            return self.product_name or self.bundleName

        def get_app_icon(self, size=16):
            """Returns the path for a given icon size."""
            return self.bundleDir + ("Resources/Iconset/%s.png" % (size))

        def launch_at_login(self):
            if "system_events" not in self.permissions or not self.applicationShouldLaunchAtLogin():
                clog.warn(
                    "App does not have permission to launch at login or doesn't provide a login service: %s.",
                    self.id
                )
                return
            self.application_will_launch_at_login()
            self.emit_signal("application_launched_at_login", name=self.get_name())

        def launch(self):
            """Launch the app."""

            self.application_will_launch()
            self.application_did_launch()
            self.emit_signal("application_launched", name=self.get_name())

        def terminate(self):
            self.application_will_terminate()
            self.application_did_terminate()
            self.emit_signal("application_terminated")

        def send_banner(self, mode='manual', **kwargs):
            """Send a notification banner with respect to the user's settings.

            The banner request can be used in one of two ways: automatic, which utilizes the CANotificationBanner class
                to create a notification banner, and manual, which uses keyword arguments at call time to generate a
                banner on the fly. In most cases, it is recommended to use the automatic mode since the
                CANotificationBanner class offers more granular control over the appearance of the banner such as the
                action button text.

            Arguments:
                mode (str): The means of sending the request. 'automatic' utilizes the CANotificationBanner class to
                    create a banner, and 'manual' uses to the old style. By default, this method uses manual mode to
                    ensure backwards-compatibility with AliceOS and older Candella versions.

            Keyword Arguments:
                banner (CANotificationBanner): The banner object to send through this app. Required in automatic
                    mode.
                title (str): The title of the banner. Required in manual mode.
                supporting (str): The supporting text for the banner. Required in manual mode.
                callback (callable): The response callback function to run when clicking the 'Respond' button. Required
                    in manual mode.

            Returns:
                response (any): The response from the banner request, if any.
            """

            if mode not in ["automatic", "manual"]:
                raise TypeError("mode must be 'automatic' or 'manual, but received %s" % (mode))

            if mode == "automatic" and self.application_should_request_notification():
                response = kwargs['banner']._send(self)
            else:
                response = self.application_will_request_notification(
                    kwargs["title"], kwargs["supporting"], response_callback=kwargs["callback"])
            self.application_did_request_notification()
            self.emit_signal("banner_sent", response=response)
            return response

        def send_alert(self, title, details, callback=Return('didDismissAlert')):
            """Send an alert with respect to the user's settings.

            Arguments:
                title (str): The title of the alert.
                details (str): The supporting text or details for the alert.
                callback (callable): The response callback function to run when dismissing the alert.

            Returns:
                response (any): The response from the alert, if any.
            """
            response = self.application_will_request_basic_alert(title, details, on_dismiss_callback=callback)
            self.application_did_request_alert()
            self.emit_signal("alert_sent", response=response)
            return response
