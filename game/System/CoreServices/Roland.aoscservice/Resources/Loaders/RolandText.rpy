#
# RolandText.rpy
# Candella
#
# Created by Marquis Kurt on 02/14/21.
# Copyright © 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

screen RolandTextLoader():
    tag bootloader
    zorder 200
    modal False
    style_prefix "RolandText"

    add "#000000"

    default log_data = []

    timer 0.1 action SetScreenVariable("log_data", roland.get_os_log_data()) repeat True

    frame:
        vbox:
            spacing 0

            for line in log_data:
                python:
                    line = line.strip()
                    line = line.replace("[DEBUG]", "{color=#999999}[DEBUG]{/color}")
                    line = line.replace("[WARNING]", "{color=#FFA500}[WARNING]{/color}")
                    line = line.replace("[INFO]", "{color=#00FF00}[INFO]{/color}")
                    line = line.replace("[ERROR]", "{color=#FF0000}[ERROR]{/color}")
                text "[line]"

style RolandText_frame is frame:
    background None
    margin (0, 0)
    padding (4, 4)

style RolandText_text is text:
    font get_font("Unicode")
    line_spacing 0
    antialias False
    size 16
