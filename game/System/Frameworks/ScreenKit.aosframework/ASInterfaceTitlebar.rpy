#
# ASInterfaceTitlebar.rpy
# Candella
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

screen ASInterfaceTitlebar(name="ASWindow", onClose=Return("didCloseView")):
    hbox:
        style_prefix "ASWindowTitleBar"
        xfill True
        hbox:
            imagebutton auto AS_FRAMEWORK_DIR("ScreenKit") + "Resources/WindowControls/wcClose_%s.png" action onClose
            text _(name)

style ASWindowTitleBar_hbox is hbox:
    xalign 0.0
    yalign 0.5
    spacing 8

style ASWindowTitleBar_text is ASInterface_text:
    size 13
    xalign 0.0
