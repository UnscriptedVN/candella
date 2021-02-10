#
# Roland.rpy
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
    from gc import get_objects
    import os
    import logging

    class Roland(CACoreService):
        """A modular bootloader for Candella."""

        def __init__(self):
            CACoreService.__init__(self, AS_CORESERVICES_DIR + "Roland.aoscservice/")

        def __get_services(self):
            return [
                service for service in get_objects() if \
                isinstance(service, CACoreService) and service.id != self.id
            ]

        def __get_apps(self):
            return [app for app in get_objects() if isinstance(app, CAApplication)]

        def __check_userland_service(self):
            if not os.path.isdir(config.savedir + "/.causerland"):
                clog.error("Userland folder is missing. This folder will need to be created.")
                persistent.AS_COMPLETED_SETUP = False

        def __launch_service(self, service):
            return service.launch_at_login()

        def __launch_app(self, app):
            return app.launch_at_login()

        def boot(self, loader=None, minimum_load_time=0, run_setup=True):
            # Show a boot screen.
            clog.debug("Checking for boot screen.")
            if type(loader) is str and loader:
                try:
                    renpy.show_screen(loader)
                    clog.debug("Loader screen '%s' displayed.", loader)
                except:
                    clog.error("Loader screen %s could not be found.", loader)

            clog.debug("Checking that userland folder exists.")
            self.__check_userland_service()

            # Launch services.
            for service in self.__get_services():
                try:
                    self.__launch_service(service)
                except Exception as error:
                    clog.error("An exception occurred when launching %s: %s.", service.id, error)

            # Re-run the Setup Assistant, if necessary.
            if not persistent.AS_COMPLETED_SETUP and run_setup:
                try:
                    clog.debug("Launching Thorax.")
                    setup.launch()
                except NameError:
                    pass
                try:
                    clog.debug("Launching AliceOS Setup Assistant.")
                    ASSetup.startSetup()
                except:
                    ASHalt.halt("MISSING_OOBE_SERVICE")

            # Launch apps that have permission to do so.
            for app in self.__get_apps():
                try:
                    self.__launch_app(app)
                except Exception as error:
                    clog.error("An exception occurred when launching %s: %s.", app.id, error)

            # Display the bootloader for this long if the other services haven't finished loading.
            renpy.pause(minimum_load_time, hard=True)

            # Dismiss the boot screen.
            clog.debug("Dismissing boot loader screen.")
            if type(loader) is str and loader:
                try:
                    renpy.hide_screen(loader)
                    clog.debug("Loader screen '%s' dismissed.", loader)
                except:
                    clog.error("Loader screen %s could not be found.", loader)

            clog.debug("Ending boot sequence.")

        def shutdown(self, loader=None):
            clog.debug("Checking for boot screen.")
            if type(loader) is str and loader:
                try:
                    renpy.show_screen(loader)
                    clog.debug("Loader screen '%s' displayed.", loader)
                except:
                    clog.error("Loader screen %s could not be found.", loader)

            clog.debug("Terminating services.")
            for service in self.__get_services():
                try:
                    service.terminate()
                except:
                    pass

            clog.debug("Terminating apps.")
            for app in self.__get_apps():
                try:
                    app.terminate()
                except:
                    pass

            clog.debug("Dismissing boot loader screen.")
            if type(loader) is str and loader:
                try:
                    renpy.hide_screen(loader)
                    clog.debug("Loader screen '%s' dismissed.", loader)
                except:
                    clog.error("Loader screen %s could not be found.", loader)

            clog.debug("Handing off game quit procedure to Ren'Py.")

    # Initialize the service outside of the class.
    roland = Roland()
