#
# ASDyanmicBlur.rpy
# Candella
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#
# MARK: Dynamic Blur Effects
init -1 python:
    from store.CADeprecated import available

    def SetThumbnailFull():
        config.thumbnail_width = config.screen_width
        config.thumbnail_height = config.screen_height

    def SetThumbnailOriginal():
        config.thumbnail_width = 256
        config.thumbnail_height = 144
        
    @available('*', introduced="apple-cinnamon")
    def ca_supports_blur():
        return renpy.version(tuple=True) > (7, 4, 0) and config.gl2


init:
    # Newer versions of Ren'Py come with a native blur property. This blur property is left over from AliceOS,
    # so this is kept in here for compatibility reasons. This feature is also available if model-based rendering
    # via OpenGL is disabled.
    if not ca_supports_blur():
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
    
    # This dictionary contains the different "strength" types for blurring. This is used to denote importance
    # in a blurred context.
    define CABlurType = {
        "strong": 32,
        "default": 16,
        "weak": 8
    }

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
