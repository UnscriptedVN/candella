#
# ASAppManager.rpy
# Candella
#
# Created by Marquis Kurt on 9/9/19
# Copyright © 2019-2021 Marquis Kurt. All rights reserved.
#

init 5 python:
    class ASAppManager(CAApplication):
        def applicationWillLaunch(self):
            renpy.show_screen("ASAppManagerView")
            pass

        def get_app_name(self, app):
            if isinstance(app, CAApplication):
                return app.get_name()
            return app.bundleName

        def _pin_to_shell_dock(self, app_id):
            """Prompt Celeste Shell to add/remove an app to/from the Dock."""
            if celeste.app_exists_in_current_launcher(app_id):
                self.emit_signal("__appman_unpin", app=app_id)
            else:
                self.emit_signal("__appman_pin", app=app_id)

        def __init__(self):
            CAApplication.__init__(self, AS_DEFAULT_APP_DIR + "AppManager.aosapp/")

    appman = appManager = ASAppManager()
