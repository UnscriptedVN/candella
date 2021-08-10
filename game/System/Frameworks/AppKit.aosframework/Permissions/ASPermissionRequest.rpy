#
# ASPermissionRequest.rpy
# Candella
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init screen ASPermissionRequest(bundleName="AS_APP_BUNDLE", requestingFor, onDeclineRequest=Return(1), onAcceptRequest=Return(0)):
    tag ASPermissionRequest
    style_prefix "ASPermissionRequest"
    zorder 100
    modal True

    on "show":
        action [
            Function(SetThumbnailFull),
            FileTakeScreenshot(),
            Function(SetThumbnailOriginal)
        ]

    if not ca_supports_blur():
        add FileCurrentScreenshot() at blur
    else:
        add FileCurrentScreenshot():
            blur CABlurType["default"]

    frame at ASDynamicBlurTransition:
        style "ASDynamicBlurFrame"
        xalign 0.5
        yalign 0.5
        xfill True
        yfill True

        has vbox:
            xalign 0.5
            yalign 0.5
            xsize 656
            spacing 16

            text bundleName + _(" Would Like To ") + AS_REQUIRE_PERMS_NAME[requestingFor]:
                style "ASPermissionRequestTitle"
            text AS_REQUIRE_PERMS_DESC[requestingFor]:
                style "ASPermissionRequestDetail"

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Don't Allow") action onDeclineRequest:
                    style "ASPermissionRequestDeclinedButton"
                textbutton _("Allow") action onAcceptRequest:
                    style "ASPermissionRequestAcceptButton"
