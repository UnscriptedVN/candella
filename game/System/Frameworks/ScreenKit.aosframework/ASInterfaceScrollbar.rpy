#
# ASInterfaceScrollbar.rpy
# Candella
#
# Created by Marquis Kurt on 9/10/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

style ASInterfaceScrollbar is viewport
style ASInterfaceScrollbar_text is ASInterface_text

style ASInterfaceScrollbar_vscrollbar:
    bar_vertical True
    bar_resizing False
    base_bar AS_FRAMEWORK_DIR("ScreenKit") + "Resources/Scrollbars/ScrollArea.png"
    thumb AS_FRAMEWORK_DIR("ScreenKit") + "Resources/Scrollbars/ScrollThumb.png"
    unscrollable "hide"
    yfit True

style ASInterfaceScrollbar_scrollbar:
    bar_vertical False
    bar_resizing False
    base_bar Frame(AS_FRAMEWORK_DIR("ScreenKit") + "Resources/Scrollbars/HorizontalScrollArea.png", Borders(6,4,6,4), tile=False)
    thumb Frame(AS_FRAMEWORK_DIR("ScreenKit") + "Resources/Scrollbars/HorizontalScrollThumb.png", Borders(6,4,6,4), tile=False)
    unscrollable "hide"
    yfit True
