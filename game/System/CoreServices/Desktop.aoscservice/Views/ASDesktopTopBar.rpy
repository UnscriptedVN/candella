#
# ASDesktopTopBar.rpy
# Candella
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init screen ASDesktopTopBar():
    tag ASDesktopTopBar
    zorder 500
    modal False

    add ASDesktop.bundleDir + "Resources/Elements/TopBar.png"

    vbox:
        xfill True
        ysize 48

        hbox:
            xfill True
            yfill True

            if renpy.get_screen("ASDesktopLaunchpadView"):
                textbutton _("Activities") action Hide("ASDesktopLaunchpadView"):
                    style "ASDesktopTopBarButton"
                    xalign 0.025
                    yalign 0.5

            else:
                textbutton _("Activities") action Show("ASDesktopLaunchpadView"):
                    style "ASDesktopTopBarButton"
                    xalign 0.025
                    yalign 0.5

            hbox:
                xalign 0.955
                yalign 0.4

                $ store.currentDesktopTime = ASDesktop.gatherCurrentTime()

                text store.currentDesktopTime:
                    style "ASDesktopTopBarStaticText"

                null width 8

                imagebutton:
                    idle ASDesktop.bundleDir + "Resources/Elements/ExitToApp.png"
                    hover ASDesktop.bundleDir + "Resources/Elements/ExitToAppHover.png"
                    action [Hide("ASDesktopLaunchpadView"), Return('didExitShell')]
                    xysize (20, 20)

        timer 1 action SetVariable("store.currentDesktopTime", ASDesktop.gatherCurrentTime()) repeat True
