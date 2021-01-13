#
# ASBootloaderView.rpy
# Candella
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

# MARK: ASBootloaderView screen entry point
init screen ASBootloaderView(timeout=5):
    tag ASBootloaderView
    zorder 100
    modal True

    add ASBootloader.bundleDir + "Resources/Elements/PureBlackBoot.png"
    add ASBootloader.bundleDir + "Resources/Elements/Background.png"

    frame at ASDynamicBlurTransition:
        style "ASDynamicBlurFrame"

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 32

            add ASBootloader.bundleDir + "Resources/Elements/BootLogo.png"

    timer timeout action Return('didBoot')
