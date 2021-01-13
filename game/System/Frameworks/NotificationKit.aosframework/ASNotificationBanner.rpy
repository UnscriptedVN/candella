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
        xpadding 24
        ypadding 16
        xalign 0.5
        yalign 0.025
        xsize 676

        vbox:
            hbox:
                xsize 628

                if not applet:
                    hbox:
                        add AS_FRAMEWORK_DIR("NotificationKit") + "Resources/appMissingIcon.png"
                        text "Unknown Bundle":
                            style "ASNotificationBannerSource"
                else:
                    hbox:
                        add applet.icons[24]
                        text applet.bundleName:
                            style "ASNotificationBannerSource"

                textbutton _("Respond") action responseCallback:
                    style "ASNotificationBannerButton"
                    xalign 1.0
            null height 2
            text message:
                style "ASNotificationBannerTitle"
            text withDetails:
                style "ASNotificationBannerDetail"
