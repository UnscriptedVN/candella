#
# ASDyanmicBlur.rpy
# Candella
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#
# MARK: Dynamic Blur Effects
init -1 python:
    def SetThumbnailFull():
        config.thumbnail_width = config.screen_width
        config.thumbnail_height = config.screen_height

    def SetThumbnailOriginal():
        config.thumbnail_width = 256
        config.thumbnail_height = 144


init:
    transform blur(child):
        contains:
            child
            alpha 1.0
        contains:
            child
            alpha 0.2 xoffset -3
        contains:
            child
            alpha 0.2 xoffset 3
        contains:
            child
            alpha 0.2 yoffset -3
        contains:
            child
            alpha 0.2 yoffset 3

    transform ASDynamicBlurTransition:
        on show:
            alpha 0.0
            easein 0.5 alpha 1.0
        on hide:
            alpha 1.0
            easeout 0.5 alpha 0.0

    style ASDynamicBlurFrame:
        background Frame([AS_LIBRARY_DIR + "Effects/ASDynamicBlur/ASDynamicBlurBackground.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        xalign 0.5
        yalign 0.5
