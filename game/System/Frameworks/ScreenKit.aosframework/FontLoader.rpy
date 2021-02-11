#
# FontLoader.rpy
# Candella
#
# Created by Marquis Kurt on 02/10/21.
# Copyright © 2021 Marquis Kurt. All rights reserved.
#

init offset = -100
init python:

    def get_font(name, variant="Regular"):
        path = AS_FONTS_DIR + name + "/" + variant + ".ttf"
        if not renpy.loadable(path):
            return AS_FONTS_DIR + "Interface/Regular.ttf"
        return path
