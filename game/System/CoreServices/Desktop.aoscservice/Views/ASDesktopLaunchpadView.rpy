#
# ASDesktopLaunchpadView.rpy
# Candella
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init screen ASDesktopLaunchpadView():
    tag ASDesktopLaunchpadView
    modal False

    add ASDesktop.bundleDir + "Resources/Elements/LaunchpadBlur.png"

    use ASDesktopTopBar

    $ appsForLauncher = ASDesktop.gatherAllApplications()

    vbox:
        yalign 0.45
        xalign 0.5

        if appsForLauncher == []:
            text _("No apps installed."):
                style "ASDesktopLaunchpadViewCenteredText"
        else:
            grid len(appsForLauncher) 1:
                for i in range(len(appsForLauncher) * 1):
                    $ slot = i + 1

                    button action [Hide("ASDesktopLaunchpadView"), Function(appsForLauncher[i].applicationWillLaunch)]:
                        maximum (128, 144)
                        sensitive True

                        has vbox:
                            xalign 0.5
                            yalign 0.0

                            if appsForLauncher[i] == None:
                                pass
                            else:
                                add appsForLauncher[i].icons[128] xalign 0.5
                                text _(appsForLauncher[i].bundleName):
                                    style "ASDesktopLaunchpadViewAppText"
                                    xalign 0.5
