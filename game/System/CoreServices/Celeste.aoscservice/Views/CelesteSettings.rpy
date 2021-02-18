#
# CelesteSettings.rpy
# Celeste Desktop Shell
#
# (C) 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

screen CelesteSettings():
    zorder 100
    style_prefix "CelesteSettings"
    modal False

    default wallpaper = "Candella"

    frame:
        xalign 0.5
        yalign 0.5
        xysize (800, 400)

        has vbox:
            xalign 0.5
            yfit True

            use ASInterfaceTitlebar("", onClose=Hide("CelesteSettings"))

            vbox:
                label "Settings"

                hbox:
                    vbox:
                        style_prefix "CelesteSettings_panel"
                        xsize 420

                        label "Desktop Background"

                        hbox:
                            spacing 8
                            box_wrap True

                            for _wall in CelesteShell.wallpapers():
                                use CelesteSettingsWallpaperButton(_wall)

style CelesteSettings_frame is ASInterface_frame
style CelesteSettings_vbox is ASInterface_vbox

style CelesteSettings_label is ASInterface_label
style CelesteSettings_label_text is ASInterface_label_text:
    font get_font("Interface", variant="Bold")

style CelesteSettings_text is ASInterface_text:
    size 14

style CelesteSettings_panel_label is ASInterface_label
style CelesteSettings_panel_label_text is ASInterface_label_text:
    font get_font("Interface", variant="Medium")
    size 18


screen CelesteSettingsWallpaperButton(wallpaper):
    style_prefix "CelesteSettingsWallpaperButton"
    button action [SetScreenVariable("wallpaper", wallpaper), Function(celeste._set_wallpaper, name=wallpaper)]:
        xysize (144, 90)
        vbox:
            add AS_LIBRARY_DIR + "Desktop Pictures/" + wallpaper + ".png":
                size (144, 82)

style CelesteSettingsWallpaperButton_text is ASInterface_text:
    size 12
