#
# ASSysInfoViewStyles.rpy
# Candella
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

style ASSysInfoTitle_text:
    font get_font("Interface", variant="Bold")
    size 34

style ASSysInfoTitle_text_nobold is ASSysInfoTitle_text:
    font get_font("Interface")

style ASSysInfoVersion_text is ASInterface_text:
    size 24

style ASSysInfoProperty_text:
    font get_font("Interface")
    size 17

style ASSysInfoProperty_text_bold is ASSysInfoProperty_text:
    font get_font("Interface", variant="Bold")

style ASSysInfoCopyright_text:
    font get_font("Interface")
    size 14
    color "#666666"
