#
# ASAppManagerStyles.rpy
# Candella
#
# Created by Marquis Kurt on 9/10/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

style ASAppManager_label is gui_label
style ASAppManager_label_text is ASInterface_text:
    font get_font("Ubuntu", variant="Bold")
    size 28

style ASAppManager_AppName_text is ASInterface_text:
    font get_font("Ubuntu", variant="Bold")
    size 16

style ASAppManager_text is ASInterface_text:
    font get_font("Ubuntu")
    size 14

style ASAppManager_button is gui_button:
    hover_background "#333333"

style ASAppManager_DetailedAppName is ASAppManager_label
style ASAppManager_DetailedAppName_text is ASAppManager_label_text:
    size 32

style ASAppManager_DetailedAppAuthor_text is ASAppManager_text:
    size 20

style ASAppManager_DetailedEmphasis_text is ASAppManager_text:
    font get_font("Ubuntu", variant="Bold")

style ASAppManager_viewport is ASInterfaceScrollbar:
    xsize 300
    yfill True
