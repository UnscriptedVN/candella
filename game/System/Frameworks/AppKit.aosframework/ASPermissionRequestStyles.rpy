#
# ASPermissionRequestStyles.rpy
# Candella
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init -1:

    # MARK: Permission Request Styles
    style ASPermissionRequestFrame:
        background Frame([AS_FRAMEWORK_DIR("AppKit") + "Resources/blankFrame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        xalign 0.5
        yalign 0.5

    style ASPermissionRequestTitle is ASSystemBoldFont:
        color "#fff"
        size 28
        text_align 0.5
        xalign 0.5

    style ASPermissionRequestDetail is ASSystemRegularFont:
        color "#fff"
        size 20
        text_align 0.5
        xalign 0.5

    style ASPermissionRequestDeclinedButton is gui_button

    style ASPermissionRequestDeclinedButton_text is ASSystemBoldFont:
        color "#fff"
        size 24
        xalign 0.5

    style ASPermissionRequestAcceptButton is gui_button

    style ASPermissionRequestAcceptButton_text is ASSystemRegularFont:
        color "#fff"
        size 24
        xalign 0.5
