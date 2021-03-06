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

    drag:
        drag_name "CelesteSettings"
        drag_handle (0, 0, 800, 64)
        xalign 0.5
        yalign 0.5

        frame:
            xysize (800, 400)

            has vbox:
                xalign 0.5
                yfit True

                use ASInterfaceTitlebar("Celeste Settings", onClose=Hide("CelesteSettings"))

                vbox:
                    label "Settings"

                    hbox:
                        spacing 8
                        vbox:
                            style_prefix "CelesteSettings_panel"
                            xsize 360

                            label "Desktop Background"

                            viewport:
                                style_prefix "ASInterfaceScrollbar"
                                scrollbars "vertical"

                                hbox:
                                    spacing 8
                                    box_wrap True

                                    for _wall in CelesteShell.wallpapers():
                                        use CelesteSettingsWallpaperButton(_wall)

                        vbox:
                            style_prefix "CelesteSettings_panel"
                            xsize 360

                            label "Display wallpaper mode"

                            vbox:
                                style_prefix "ASInterfaceRadio"

                                textbutton "Scaled to fit" action Function(celeste._update_wallpaper_display_mode, "contain"):
                                    selected celeste._wall_display_mode == "contain"
                                textbutton "Centered" action Function(celeste._update_wallpaper_display_mode, "cover"):
                                    selected celeste._wall_display_mode == "cover"
                                textbutton "Stretch to fill" action Function(celeste._update_wallpaper_display_mode, "fill"):
                                    selected celeste._wall_display_mode == "fill"

style CelesteSettings_frame is ASInterface_frame
style CelesteSettings_vbox is ASInterface_vbox

style CelesteSettings_label is ASInterface_label
style CelesteSettings_label_text is ASInterface_label_text:
    font get_font("Ubuntu", variant="Bold")
    color "#212121"

style CelesteSettings_text is ASInterface_text:
    size 14

style CelesteSettings_panel_label is CelesteSettings_label
style CelesteSettings_panel_label_text is CelesteSettings_label_text:
    font get_font("Ubuntu", variant="Medium")
    size 18


screen CelesteSettingsWallpaperButton(wallpaper):
    style_prefix "CelesteSettingsWallpaperButton"
    button action [SetScreenVariable("wallpaper", wallpaper), Function(celeste._set_wallpaper, name=wallpaper)]:
        xysize (156, 110)
        vbox:
            add AS_LIBRARY_DIR + "Desktop Pictures/" + wallpaper + ".png":
                size (156, 108)

style CelesteSettingsWallpaperButton_text is ASInterface_text:
    size 12
