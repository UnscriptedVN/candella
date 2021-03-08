#
# CSNotificationBanner.rpy
# Candella
#
# Created by Marquis Kurt on 03/08/21.
# Copyright © 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -10

init python:
    class CANotificationBanner():
        def __init__(self, message, details, callback=Return('didClickRespond')):
            self.message = message
            self.details = details
            self.callback = callback
            self.callback_text = "Respond"


        def __str__(self):
            return "CANotificationBanner(%s, %s, callback='%s')" % (self.message, self.details, self.callback_text)


        def _send(self, reference=None):
            return renpy.invoke_in_new_context(
                renpy.call_screen,
                "ASNotificationBanner",
                applet=reference,
                message=self.message,
                withDetails=self.details,
                r_text=self.callback_text,
                responseCallback=self.callback
            )
