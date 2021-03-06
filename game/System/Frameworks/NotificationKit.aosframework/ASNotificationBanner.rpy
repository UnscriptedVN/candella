#
# ASNotificationBanner.rpy
# Candella
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init screen ASNotificationBanner(applet=None, message, withDetails, responseCallback=Return('didClickRespond')):
    tag ASNotificationBanner
    zorder 100
    style_prefix "ASNotificationBanner"

    timer 5.0 action Return('notificationTimedOut')

    frame at ASNotificationBannerTransition:
        style "ASNotificationBannerFrame"
        padding (24, 16)
        align (1.0, 0.025)
        xsize 550

        vbox:
            python:
                _app_icon = CADesign.get_app_mask(
                    applet.icons[24] if applet else AS_FRAMEWORK_DIR("NotificationKit") + "Resources/appMissingIcon.png",
                    24
                )
                _app_name = (
                    applet.get_name() if isinstance(applet, CAApplication) else applet.bundleName) if applet \
                    else "Unknown Bundle"
            hbox:
                xfill True

                hbox:
                    add _app_icon
                    text "[_app_name]":
                        style "ASNotificationBannerSource"
                textbutton _("Respond") action [Hide("ASNotificationBanner"), responseCallback]:
                    style "ASNotificationBannerButton"
                    xalign 1.0

            text message:
                style "ASNotificationBannerTitle"
            text withDetails:
                style "ASNotificationBannerDetail"
