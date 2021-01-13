#
# ASSetupAssistantView.rpy
# Candella
#
# Created by Marquis Kurt on 7/4/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

# MARK: ASSetupAssistantView screen entry point
init screen ASSetupAssistantView(title="Setup Assistant", instructions="", useInputMethod=False, completed=False):
    tag ASSetupAssistantView
    zorder 100
    modal True
    style_prefix "ASInterface"

    add ASSetup.getFromElements("Background.png")

    frame:
        style "ASSetupAssistantViewFrame"
        xalign 0.5
        yalign 0.5
        ysize 625
        xsize 825
        padding (64, 48)


        has vbox:
            xalign 0.5
            xfill True
            yfill True
            vbox:
                xfill True
                yfit True
                spacing 16
                hbox:
                    xalign 0.5
                    spacing 8
                    text title:
                        style "ASSetupAssistantViewTitle"
                        xalign 0.5

                viewport:
                    style_prefix "ASInterfaceScrollbar"
                    mousewheel True
                    scrollbars "vertical"
                    ymaximum 400
                    xfill True

                    text instructions:
                        style "ASSetupAssistantViewDetail"
                        xalign 0.5

            if useInputMethod:
                input:
                    style "ASSetupAssistantViewInput"
                    xalign 0.5
            else:
                python:
                    button_text = "Finish" if completed else "Next"

                textbutton "[button_text]" action Return('didCompleteStep'):
                    style "ASInterfacePushButton"
                    xalign 0.5
                    yalign 0.85
                    xpadding 64

            if useInputMethod:
                null height 16
                text "To continue, press Return or Enter.":
                    style "ASSetupAssistantViewSmallerDetail"
                    xalign 0.5
                    yalign 0.75
