#
# CADesign.rpy
# Candella
#
# Created by Marquis Kurt on 02/19/21.
# Copyright © 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -50
init python in CADesign:
    from store import Frame, AlphaMask

    def get_app_mask_frame():
        return Frame("System/Library/Design/app_mask.png")


    def get_app_mask(image, size):
        return AlphaMask(image, get_app_mask_frame(), xysize=(size, size))
