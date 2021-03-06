#
# ASInterfaceCheckbox.rpy
# Candella
#
# Created by Marquis Kurt on 9/10/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

style ASInterfaceCheckbox_button is gui_button

style ASInterfaceCheckbox_button:
    foreground AS_FRAMEWORK_DIR("ScreenKit") + "Resources/Checkboxes/Idle.png"
    selected_foreground AS_FRAMEWORK_DIR("ScreenKit") + "Resources/Checkboxes/Selected.png"
    xpadding 28

style ASInterfaceCheckbox_text is ASInterface_text

style ASInterfaceCheckbox_button_text is ASInterface_text:
    size 20
