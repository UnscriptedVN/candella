#
# ASNotificationStyles.rpy
# Candella
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

# MARK: ASNotificationBanner
init:
    style ASNotificationBannerFrame:
        background Frame([AS_FRAMEWORK_DIR("NotificationKit") + "Resources/bannerBackground.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
            # xalign .5
            # yalign .5

    transform ASNotificationBannerTransition:
        on show:
            yalign 0.0 xalign 1.0 xoffset -16
            linear 0.25 ypos 32
        on hide:
            yalign 0.0 ypos 32 xalign 1.0 xoffset -16
            linear 0.25 yalign -1.0

    style ASNotificationBannerSource is ASSystemMediumFont:
        font get_font("Ubuntu", variant="Light")
        size 20
        color "#212121"
        first_indent 8
        text_align 0
        layout "tex"
        xalign 0

    style ASNotificationBannerTitle is ASSystemBoldFont:
        font get_font("Ubuntu")
        size 22
        color "#212121"

    style ASNotificationBannerDetail is ASSystemRegularFont:
        font get_font("Ubuntu", variant="Light")
        size 16
        color "#212121"

    style ASNotificationBannerButton is gui_button

    style ASNotificationBannerButton_text is ASSystemBoldFont:
        font get_font("Ubuntu", variant="Medium")
        size 16
        color "#212121"

    # MARK: ASNotificationAlert

    style ASNotificationAlertTitle is ASSystemBoldFont:
        font get_font("Ubuntu", variant="Bold")
        color "#fff"
        size 28
        text_align 0.5
        xalign 0.5

    style ASNotificationAlertDetail is ASSystemRegularFont:
        font get_font("Ubuntu")
        color "#fff"
        size 20
        text_align 0.5
        xalign 0.5

    style ASNotificationAlertDeclinedButton is gui_button

    style ASNotificationAlertDeclinedButton_text is ASSystemBoldFont:
        font get_font("Ubuntu", variant="Bold")
        color "#fff"
        size 24
        xalign 0.5

    style ASNotificationAlertAcceptButton is gui_button

    style ASNotificationAlertAcceptButton_text is ASSystemRegularFont:
        font get_font("Ubuntu")
        color "#fff"
        size 24
        xalign 0.5
