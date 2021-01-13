#
# ASSysInfoViewStyles.rpy
# Candella
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

style ASSysInfoTitle_text:
    font AS_FONTS_DIR + "Bold.ttf"
    size 34

style ASSysInfoTitle_text_nobold is ASSysInfoTitle_text:
    font AS_FONTS_DIR + "Regular.ttf"

style ASSysInfoVersion_text is ASInterface_text:
    size 24

style ASSysInfoProperty_text:
    font AS_FONTS_DIR + "Regular.ttf"
    size 17

style ASSysInfoProperty_text_bold is ASSysInfoProperty_text:
    font AS_FONTS_DIR + "Bold.ttf"

style ASSysInfoCopyright_text:
    font AS_FONTS_DIR + "Regular.ttf"
    size 14
    color "#666666"
