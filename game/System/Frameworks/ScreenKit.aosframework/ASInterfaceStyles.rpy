#
# ASInterfaceStyles.rpy
# Candella
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init offset = 10

style ASInterface_frame:
    background Frame([AS_FRAMEWORK_DIR("ScreenKit") + "Resources/Frames/FrameChrome.png"], Borders(8,12,8,8), tile=False)
    padding (16, 16)
    xalign 0.5
    yalign 0.5
    xmaximum 1248
    ymaximum 688

style ASInterface_vbox is vbox:
    spacing 8

style ASInterface_hbox is hbox:
    spacing 8

style ASInterface_text:
    font get_font("Ubuntu")
    color "#212121"
    size 14

style ASInterface_button is gui_button
style ASInterface_button_text:
    font get_font("Ubuntu", variant="Bold")
