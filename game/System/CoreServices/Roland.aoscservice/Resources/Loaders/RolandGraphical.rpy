#
# RolandGraphical.rpy
# Candella
#
# Created by Marquis Kurt on 02/09/21.
# Copyright © 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

screen RolandGraphicalLoader():
    tag bootloader
    zorder 200
    modal False

    add "#191919"

    vbox:
        align (0.5, 0.5)

        if renpy.loadable("gui/window_icon.png"):
            vbox:
                xalign 0.5
                spacing 4
                add "gui/window_icon.png":
                    size (176, 176)
                    xalign 0.5

                text "Powered by [AS_SYS_INFO[NAME]]":
                    text_align 0.5
        else:
            text "candella":
                size 32
