#
# ASSysInfoView.rpy
# Candella
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init offset = 10

screen ASSysInfoView():
    style_prefix "ASInterface"

    drag:
        drag_name "ASSysInfoView"
        drag_handle (0, 0, 800, 64)
        xalign 0.5
        yalign 0.5

        frame:
            xmaximum 800

            has vbox:
                use ASInterfaceTitlebar("About [AS_SYS_INFO[NAME]]", onClose=Hide("ASSysInfoView"))

                hbox:
                    spacing 32

                    add "System/Library/Branding/sprite.png":
                        size (202.24, 256)
                        nearest True
                        xoffset 16

                    vbox:
                        text "[AS_SYS_INFO[NAME]] [AS_SYS_INFO[VERSION]]":
                            style "ASSysInfoTitle_text"
                        text "v[AS_SYS_INFO[VERSION]]-[AS_SYS_INFO[BUILD_ID]] ([AS_SYS_INFO[COMMON_NAME]])":
                            style "ASSysInfoVersion_text"
                        text "{=ASSysInfoProperty_text_bold}Distribution Channel{/}: [AS_SYS_INFO[CHANNEL]]":
                            style "ASSysInfoProperty_text"
                        null height 16
                        text "{=ASSysInfoProperty_text_bold}Built for Ren'Py{/} [renpy.version_only]":
                            style "ASSysInfoProperty_text"
                        null height 24
                        text "© 2018-2021 Project Alice and UnscriptedVN team.\n[AS_SYS_INFO[NAME]] is free and open-source software licensed under the BSD 2-Clause License.":
                            style "ASSysInfoCopyright_text"
                            yalign 1.0
