#
# CACoreService.rpy
# Candella Core Services
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = -20

init python:
    from store.CAFrameworkLoader import get_framework_names
    import logging

    class CACoreService(ASCoreServiceRepresentative, CAObservable):

        def __init__(self, app_path):
            ASCoreServiceRepresentative.__init__(self, app_path)
            self.requisites = []

            try:
                self._load_manifest()
            except Exception as problem:
                logging.warn(
                    "A problem occurred when reading the manifest for %s: %s",
                    self.__class__.__name__,
                    problem
                    )

            self._validate_requisites()
            self.data = ServiceStorage(self)

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

            if "requisites" in manifest:
                self.requisites = manifest["requisites"]

            self.permissions = manifest["permissions"]

            if self.id not in persistent.AS_PERMISSIONS:
                persistent.AS_PERMISSIONS[self.id] = {}

            # Auto-grant permissions listed in the service's requisites.
            for permission in self.permissions:
                perm = CA_PERMISSIONS[permission].key
                persistent.AS_PERMISSIONS[self.id][perm] = True

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
            clog.debug("Requisites have been validated for service %s.", self.id)

        def launch_at_login(self):
            self.serviceWillLaunchAtLogin()
            self.serviceDidLaunchAtLogin()
            self.emit_signal("service_launched_at_login", name=self.__class__.__name__)

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
