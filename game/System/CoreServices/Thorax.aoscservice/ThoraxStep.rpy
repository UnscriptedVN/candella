#
# ThoraxStep.rpy
# Candella
#
# Created by Marquis Kurt on 02/09/21.
# Copyright © 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 3
init python:

    class ThoraxStep():
        def __init__(self, name, detail, requires_keyboard_input=False, on_receive_result=None):
            self.name = name
            self.detail = detail
            self.requires_keyboard_input = requires_keyboard_input
            self.result_callback = on_receive_result
