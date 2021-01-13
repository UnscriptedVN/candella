#
# ASInterfaceRadio.rpy
# Candella
#
# Created by Marquis Kurt on 9/19/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

style ASInterfaceRadio_button is bui_button

style ASInterfaceRadio_button:
    foreground AS_FRAMEWORK_DIR("ScreenKit") + "Resources/Radios/Idle.png"
    selected_foreground AS_FRAMEWORK_DIR("ScreenKit") + "Resources/Radios/Selected.png"
    xpadding 28

style ASInterfaceRadio_text is ASInterface_text

style ASInterfaceRadio_button_text is ASInterface_text:
    size 20
