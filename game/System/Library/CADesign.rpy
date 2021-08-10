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
    from store.CADeprecated import available

    @available("*", introduced="apple-cinnamon")
    def get_app_mask_frame():
        """Returns a frame with a mask of an application's borders."""
        return Frame("System/Library/Design/app_mask.png")

    @available("*", introduced="apple-cinnamon")
    def get_app_mask(image, size):
        """Returns an AlphaMask of an application's borders."""
        return AlphaMask(image, get_app_mask_frame(), xysize=(size, size))
