#
# CAApplication.rpy
# Candella
#
# Created by Marquis Kurt on 1/13/21.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#

init python:
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
            
        def applicationWillTerminate(self):
            if isinstance(self.data, AppStorage):
                self.data.write()
            self.emit_signal("application_terminated")
                
        def _initialize_manifest(self):
            manifest = {}
            if not renpy.exists(self.bundleDir + "manifest.json"):
                raise FileNotFoundError()
            
            with renpy.file(self.bundleDir + "manifest.json") as file:
                manifest = json.load(file)
                
            self.bundleName = self.name = manifest["name"]
            self.bundleProductName = self.product_name = manifest["productName"]
            self.bundleId = self.id = manifest["id"]
            self.bundleAuthor = self.author = manifest["author"]
            self.bundleVersion = self.version = manifest["version"]
            self.bundleDescription = self.description = manifest["description"]
            self.license = manifest["license"]
            
            if self.bundleId in persistent.AS_PERMISSIONS:
                return
            
            self.permissions = manifest["permissions"]
            for permission in manifest["permissions"]:
                if permission not in CA_PERMISSIONS:
                    continue
                permission_data = CA_PERMISSIONS[permission]
                self.requires[permission_data.key] = True
                persistent.AS_PERMISSIONS[self.id][permission_data.key] = permission_data.default_state
        
        def get_name(self):
            """Returns the name of the app, or its bundle name."""
            return self.product_name or self.bundleName
                
        def get_app_icon(self, size=16):
            """Returns the path for a given icon size."""
            return self.bundleDir + ("Resources/Iconset/%s.png" % (size))
            
        def launch(self):
            """Launch the app."""
            
            self.application_will_launch()
            self.application_did_launch()
            self.emit_signal("application_launched", name=self.get_name())
            
        def terminate(self):
            self.application_will_terminate()
            self.application_did_terminate()
            self.emit_signal("application_terminated")
            
        def send_banner(self, title, supporting, callback=Return('didClickRespond')):
            """Send a notification banner with respect to the user's settings.
            
            Arguments:
                title (str): The title of the banner.
                supporting (str): The supporting text for the banner.
                callback (callable): The response callback function to run when clicking the 'Respond' button.
                
            Returns:
                response (any): The response from the banner request, if any.
            """
            response = self.application_will_request_notification(title, supporting, response_callback=callback)
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
            self.emit_signal("sent_alert", response=response)
            return response