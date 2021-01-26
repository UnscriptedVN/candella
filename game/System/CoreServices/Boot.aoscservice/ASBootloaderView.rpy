#
# ASBootloaderView.rpy
# Candella
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

screen ASBootloaderView(timeout=5):
    tag ASBootloaderView
    zorder 100
    modal True
    style_prefix "ASBootloaderView"

    add "#000000"

    frame:
        xalign 0.5
        yalign 0.5
        
        vbox:        
            add ASBootloader.bundleDir + "Resources/Elements/BootLogo.png":
                zoom 0.8

    timer timeout action Return('didBoot')

style ASBootloaderView_frame is frame:
    background None
    margin (0, 0)
    padding (8, 8)