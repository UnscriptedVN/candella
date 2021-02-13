#
# Throax.rpy
# Candella
#
# Created by Marquis Kurt on 02/09/21.
# Copyright © 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 5
init python:
    import logging

    class Thorax(CACoreService):
        """A modular setup assistant for Candella."""

        def __init__(self):
            CACoreService.__init__(
                self,
                AS_CORESERVICES_DIR + "Thorax.aoscservice/"
            )

            self.__step_callbacks = {
                "create_user": self.__set_up_user,
                "complete": self.__complete_setup
            }

            self.default_steps = self.__create_steps(self.bundleDir + "Resources/default_steps.json")

        def __set_up_user(self, username):
            try:
                CAUserData._create_user_file(username)
                persistent.playername = username
            except:
                pass

        def __complete_setup(self, _x):
            persistent.AS_COMPLETED_SETUP = True
            return

        def __create_steps(self, json_path):
            results = []
            with renpy.file(json_path) as step_data:
                steps = json.load(step_data)
            for step in steps:
                results.append(
                    ThoraxStep(
                        step["name"],
                        step["detail"],
                        requires_keyboard_input=step["keyboard_input"],
                        on_receive_result=(self.__step_callbacks[step["callback"]] if "callback" in step else None)
                    )
                )
            return results

        def launch(self, steps=None):
            if steps and type(steps) is str:
                procedure = self.__create_steps(steps)
            elif steps and type(steps) is list:
                procedure = steps
            else:
                 procedure = self.default_steps

            for step in procedure:
                result = renpy.call_screen(
                    "ThoraxStepScreen",
                    step.name,
                    step.detail,
                    show_input=step.requires_keyboard_input
                )

                if step.result_callback is not None and callable(step.result_callback):
                    step.result_callback(result)

            clog.debug("Setup complete.")


            def add_setup_callback(self, name, fn):
                if name in self.__step_callbacks:
                    clog.error("The callback with name %s is already defined.", name)
                    return
                self.__step_callbacks[name] = fn


    # Initialize the service outside of the class.
    setup = Thorax()
