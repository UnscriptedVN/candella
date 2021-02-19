#
# RolandGraphicLogomarkLoader.rpy
# Candella
#
# Created by Marquis Kurt on 02/14/21.
# Copyright © 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

screen RolandGraphicalLogomarkLoader():
    tag bootloader
    zorder 200
    modal False

    add "#191919"

    default services = []

    python:
        services = roland._get_services()

    vbox:
        xfill True
        yfill True

        null height 8

        add "System/Library/Branding/logomark.png":
            align (0.5, 0.5)
            zoom 0.5

        hbox:
            align (0.5, 0.9)
            spacing 8

            for service in services:
                add AlphaMask(service.icons[32], celeste.get_app_mask(), xysize=(32, 32)):
                    size (32, 32)
