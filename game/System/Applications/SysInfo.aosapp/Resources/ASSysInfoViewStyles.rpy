#
# ASSysInfoViewStyles.rpy
# Candella
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

style ASSysInfoTitle_text is ASInterface_text:
    font get_font("Ubuntu", variant="Bold")
    size 34

style ASSysInfoTitle_text_nobold is ASSysInfoTitle_text:
    font get_font("Ubuntu")

style ASSysInfoVersion_text is ASInterface_text:
    font get_font("Ubuntu", variant="Mono")
    size 24

style ASSysInfoProperty_text is ASInterface_text:
    font get_font("Ubuntu", variant="Mono")
    size 17

style ASSysInfoProperty_text_bold is ASSysInfoProperty_text:
    font get_font("Ubuntu", variant="Bold")

style ASSysInfoCopyright_text:
    font get_font("Ubuntu", variant="Light")
    size 14
    color "#666666"
