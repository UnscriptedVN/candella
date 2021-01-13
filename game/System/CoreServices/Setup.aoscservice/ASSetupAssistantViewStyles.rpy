#
# ASSetupAssistantViewStyles.rpy
# Candella
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init:
    style ASSetupAssistantViewFrame is ASInterface_frame:
        xalign 0.5
        yalign 0.5

    style ASSetupAssistantViewTitle is ASInterface_label_text:
        font AS_FONTS_DIR + "Bold.ttf"
        size 28
        color "#ffffff"

    style ASSetupAssistantViewDetail is ASInterface_text:
        size 18
        color "#ffffff"

    style ASSetupAssistantViewSmallerDetail is ASInterface_text:
        size 10
        color "#999999"

    style ASSetupAssistantViewInput is ASInterface_text:
        size 20
        color "#ffffff"
