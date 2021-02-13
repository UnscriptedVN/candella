#
# Glossary.rpy
# Glossary App
#
# Created by Marquis Kurt on 12/03/20.
# Copyright © 2020-2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init 10 python:
    import json
    import logging

    class GlossaryApp(CAApplication):
        _levels = []

        def __init__(self):
            CAApplication.__init__(self, AS_DEFAULT_APP_DIR + "Glossary.aosapp/")
            self.default_glossary = self.bundleDir + "Resources/glossary.json"

        def applicationWillLaunch(self):
            renpy.show_screen("GlossaryAppUIView", glossary=self.load_glossary())

        def load_glossary(self, filepath=None):
            """Returns a dictionary containing the glossary terms and definitions."""
            location = self.default_glossary if not filepath else filepath
            glossary = {}
            if not renpy.loadable(location):
                clog.warn("Glossary file couldn't be loaded: %s", location)
                return {}

            with renpy.file(location) as gloss:
                glossary = json.load(gloss)["dictionary"]
            return glossary

    glossary_app = GlossaryApp()
