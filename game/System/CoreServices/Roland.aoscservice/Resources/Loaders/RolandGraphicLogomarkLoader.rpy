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

    vbox:
        align (0.5, 0.5)

        add "System/Library/Branding/logomark.png":
            zoom 0.5
