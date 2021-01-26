#
# CabertoSettings.rpy
# Caberto Desktop Shell
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

screen CabertoSettings():
    zorder 100
    style_prefix "CabertoSettings"
    modal False
    
    default wallpaper = "Candella"
    
    frame:
        xalign 0.5
        yalign 0.5
        xysize (800, 400)
        
        has vbox:
            xalign 0.5
            yfit True
            
            use ASInterfaceTitlebar("", onClose=Hide("CabertoSettings"))
            
            vbox:
                label "Settings"
            
                hbox:
                    vbox:
                        style_prefix "CabertoSettings_panel"
                        xsize 420
                        
                        label "Desktop Background"
                        
                        hbox:
                            spacing 8
                            box_wrap True
                            
                            for _wall in CabertoShell.wallpapers():
                                use CabertoSettingsWallpaperButton(_wall)
                            
style CabertoSettings_frame is ASInterface_frame
style CabertoSettings_vbox is ASInterface_vbox

style CabertoSettings_label is ASInterface_label
style CabertoSettings_label_text is ASInterface_label_text:
    font AS_FONTS_DIR + "Bold.ttf"

style CabertoSettings_text is ASInterface_text:
    size 14

style CabertoSettings_panel_label is ASInterface_label
style CabertoSettings_panel_label_text is ASInterface_label_text:
    font AS_FONTS_DIR + "Medium.ttf"
    size 18
    

screen CabertoSettingsWallpaperButton(wallpaper):
    style_prefix "CabertoSettingsWallpaperButton"
    button action [SetScreenVariable("wallpaper", wallpaper), Function(caberto._set_wallpaper, name=wallpaper)]:
        xysize (144, 90)
        vbox:
            add AS_LIBRARY_DIR + "Desktop Pictures/" + wallpaper + ".png":
                size (144, 82)
                
style CabertoSettingsWallpaperButton_text is ASInterface_text:
    size 12
