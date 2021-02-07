#
# CACoreService.rpy
# Candella Core Services
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = -20

init python:
    import logging

    class CACoreService(ASCoreServiceRepresentative, CAObservable):

        def __init__(self, app_path):
            ASCoreServiceRepresentative.__init__(self, app_path)

            try:
                self._load_manifest()
            except Exception as problem:
                logging.warn(
                    "A problem occurred when reading the manifest for %s: %s",
                    self.__class__.__name__,
                    problem
                    )

        def _load_manifest(self):
            manifest = {}
            if not renpy.loadable(self.bundleDir + "manifest.json"):
                raise Exception("Manifest file not found: %s" % (self.bundleDir + "manifest.json"))

            with renpy.file(self.bundleDir + "manifest.json") as file:
                manifest = json.load(file)

            self.bundleName = self.name = manifest["name"]
            self.bundleId = self.id = manifest["id"]
            self.bundleAuthor = self.author = manifest["author"]
            self.bundleVersion = self.version = manifest["version"]
            self.bundleDescription = self.description = manifest["description"]
            self.license = manifest["license"]
            self.requisites = manifest["requisites"]

            if self.id not in persistent.AS_PERMISSIONS:
                persistent.AS_PERMISSIONS[self.id] = {}

            # Auto-grant permissions listed in the service's requisites.
            for requisite in self.requisites:
                perm = CA_PERMISSIONS[requisite].key
                persistent.AS_PERMISSIONS[self.id][perm] = True

        def launch(self):
            self.serviceWillLaunch()
            self.serviceDidLaunch()
            self.emit_signal("service_launched", name=self.name)

        def terminate(self):
            self.serviceWillTerminate()
            self.serviceDidTerminate()
            self.emit_signal("service_terminated")

        def request_notification(self, message, details, callback=Return(0)):
            response = self.serviceWillRequestNotification(message, details, responseCallback=callback)
            self.serviceDidRequestNotification()
            self.emit_signal("service_requested_notification", response=response)
