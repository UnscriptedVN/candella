#
# ThoraxStepScreen.rpy
# Candella
#
# Created by Marquis Kurt on 02/09/21.
# Copyright © 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

screen ThoraxStepScreen(name, detail, show_input=False):
    tag setup
    zorder 250 # Ensure it's on top of the loading screen.
    modal True
    style_prefix "thorax_setup"

    default input_result = ""
    default return_action = [Hide("ThoraxStepScreen"), Return(None)]

    python:
        if show_input:
            return_action = [Hide("ThoraxStepScreen"), Return(input_result)]

    key "K_RETURN" action return_action

    if not ca_supports_blur():
        add "System/Library/Desktop Pictures/McWay Falls.png" at blur, truecenter:
            size (1280, 720)
            fit "cover"
    else:
        add "System/Library/Desktop Pictures/McWay Falls.png" at truecenter:
            blur CABlurType["strong"]
            size (1280, 720)
            fit "cover"

    frame:
        xalign 0.5
        yalign 0.5
        maximum 750, 650
        xfill True
        yfill True

        has vbox:
            xalign 0.5

            vbox:
                style_prefix "thorax_setup_header"

                frame:
                    has vbox:
                        label "[name]"

            frame:
                style "thorax_setup_detail_frame"

                text "[detail]"

                vbox:
                    align (0.5, 1.0)
                    spacing 24
                    xfill True

                    if show_input:
                        input default "" value ScreenVariableInputValue("input_result")
                        null height 48

                    textbutton _("Next ›") action return_action:
                        xalign 1.0

                    text _("Click 'Next' or press Return/Enter on your keyboard to continue."):
                        xalign 0.5
                        style "thorax_setup_hidden"


style thorax_setup_frame is frame:
    margin (0, 0)
    padding (0, 0)
    background "#f4f4f4"

style thorax_setup_text is ASSystemRegularFont:
    color "#191919"
    size 22

style thorax_setup_hidden is thorax_setup_text:
    color "#666666"
    size 16

style thorax_setup_header_frame is frame:
    margin (0, 0)
    padding (24, 32)
    xfill True
    background "#CFCBB8"

style thorax_setup_header_label is label
style thorax_setup_header_label_text is ASSystemMediumFont:
    size 36
    color "#191919"

style thorax_setup_detail_frame is frame:
    margin (0, 0)
    padding (32, 24)
    background "#f4f4f4"

style thorax_setup_button is button
style thorax_setup_button_text is ASSystemRegularFont:
    size 28
    idle_color "#EF7E45"
    hover_color "#EF7E45"

style thorax_setup_input is input:
    color "#333333"
