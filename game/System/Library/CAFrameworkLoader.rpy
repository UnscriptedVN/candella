#
# CAFrameworkLoader.rpy
# Candella
#
# Created by Marquis Kurt on 2/7/21.
# Copyright © 2021 Marquis Kurt. All rights reserved.
#

init -999 python in CAFrameworkLoader:
    import json
    import logging
    from store import AS_FRAMEWORKS_DIR, clog

    def get_framework_names():
        """Returns a list of all of the available frameworks to Candella/AliceOS."""
        fr_files = [
            file.replace(AS_FRAMEWORKS_DIR, "") for file in renpy.list_files()\
            if file.startswith(AS_FRAMEWORKS_DIR)
        ]
        frameworks = []
        for file in fr_files:
            name = file.split("/")[0].replace(".aosframework", "")
            if name in frameworks:
                continue
            frameworks.append(name)
        return frameworks

    def get_framework_manifest(framework_name):
        """Returns the manifest for a specified framework name."""
        manifest = {}
        if not renpy.loadable(AS_FRAMEWORKS_DIR + framework_name + ".aosframework/manifest.json"):
            clog.error("Manifest for framework not found: %s", framework_name)
            return {}
        with renpy.file(AS_FRAMEWORKS_DIR + framework_name + ".aosframework/manifest.json") as file:
            manifest = json.load(file)
        return manifest

    def check_framework_requirements(framework_name):
        """Check whether the framework's requisites exist in this installation.

        Returns:
            True if the requisites are present or if no requisites exist, False otherwise.
        """
        manifest = get_framework_manifest(framework_name)
        known = get_framework_names()

        if not manifest:
            return False

        if "requisites" not in manifest or not manifest["requisites"]:
            clog.debug("No requisites listed for framework: %s", framework_name)
            return True

        for requisite in manifest["requisites"]:
            if requisite not in known:
                clog.error("Requisite framework for %s is missing: %s", framework_name, requisite)
                return False
        return True

init 7 python in CAFrameworkLoader:
    from store import ASHalt

    # Scan all frameworks.
    for framework in get_framework_names():
        clog.debug("Checking framework requirements for: %s", framework)
        if not check_framework_requirements(framework):
            try:
                ASHalt.halt("REQUISITE_FRAMEWORK_MISSING")
            except:
                renpy.quit()
