#
# CAApplication.rpy
# Candella
#
# Created by Marquis Kurt on 1/13/21.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#

init python:
    import json
    
    class CAApplication(ASAppRepresentative):
        """The class used for Candella apps.
        
        CAApplication is an extension of the standard ASAppRepresentative class and aims to make app development
            simpler. This class provides extra utilities to simplify app development.
            
        Differences Between ASAppRepresentative:
            - Apps do not need to override class attributes to fill out app metadata. Instead, this is achieved with
                a manifest file, manifest.json.
            - Notification requests are handled by methods that simplify calls.
            - Grabbing icon sizes for an app is handled with a method.
        """
        
        product_name = "Bundle product name"
        license = "No license provided."
        permissions = []
        
        def __init__(self, app_path):
            """Initialize a Candella app.
            
            Arguments:
                app_directory: The path to the Candella app file.
            """
            
            # Initialize the AliceOS-compatible app.
            ASAppRepresentative.__init__(self, app_path)
            
            # Load the manifest, if there is one.
            try:
                self._initialize_manifest()
            except FileNotFoundError:
                print("WARN: Manifest file for this app has not been found.")
                
            self.bundleDescription += "\n This app is made for the Candella distribution and may not be compatible with AliceOS."
            self.description += "\n This app is made for the Candella distribution and may not be compatible with AliceOS."
        
        def _initialize_manifest(self):
            manifest = {}
            if not renpy.exists(self.appDirectory + "manifest.json"):
                raise FileNotFoundError()
            
            with renpy.file(self.appDirectory + "manifest.json", 'r') as file:
                manifest = json.load(file)
                
            self.bundleName = self.name = manifest["name"]
            self.bundleProductName = self.product_name = manifest["productName"]
            self.bundleId = self.id = manifest["id"]
            self.bundleAuthor = self.author = manifest["author"]
            self.bundleVersion = self.version = manifest["version"]
            self.bundleDescription = self.description = manifest["description"]
            self.license = manifest["license"]
            
            self.permissions = manifest["permissions"]
            persistent.AS_PERMISSIONS[self.id] = {}
            for permission in manifest["permissions"]:
                if permission not in CA_PERMISSIONS:
                    continue
                permission_data = CA_PERMISSIONS[permission]
                persistent.AS_PERMISSIONS[self.id][permission_data.key] = permission_data.default_state
            
        def get_app_icon(self, size=16):
            """Returns the path for a given icon size."""
            return self.bundleDir + "Resources/Iconset/%.png" % (size)
            
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
            return response