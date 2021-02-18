#
# CelesteTopBar.rpy
# Celeste Desktop Shell
#
# (C) 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

screen CelesteTopBar():
    tag desktop
    modal False
    style_prefix "CelesteTopBar"

    default _CurrentTime = "Tue. 9:41 AM"
    default _Username = "User"
    default _CurrentApp = ""

    python:
        _CurrentTime = CelesteShell.current_time()
        _user = CAAccountsService.get_logged_in_user()
        _Username = _user.display_name
        _CurrentApp = celeste._current_app_name

    timer 0.5 action [SetScreenVariable("_CurrentApp", celeste._current_app_name), SetScreenVariable("_CurrentTime", CelesteShell.current_time())] repeat True

    frame:
        xfill True
        ysize 28

        has hbox:
            xfill True
            text "[_CurrentApp]":
                style "CelesteTopBar_AppName"

            hbox:
                xalign 1.0
                spacing 8

                textbutton "[_Username]" action Function(celeste.start_acct_manager)
                text "[_CurrentTime]"

                button action Show("CelesteSettings"):
                    xysize (24, 18)
                    add celeste.bundleDir + "Resources/settings.png":
                        size (18, 18)
                        align (0.5, 0.5)

                button action Return("CelesteShellView"):
                    xysize (24, 18)
                    add celeste.bundleDir + "Resources/logoff.png":
                        size (18, 18)
                        align (0.5, 0.5)

style CelesteTopBar_frame is frame:
    background Frame("#191919", Borders(0, 0, 0, 0), tile=True)
    margin (0, 0)
    xpadding 8
    ypadding 4

style CelesteTopBar_hbox is hbox:
    spacing 8

style CelesteTopBar_text is text:
    font get_font("Ubuntu", "Light")
    color "#ffffff"
    size 16

style CelesteTopBar_AppName is text:
    font get_font("Ubuntu", "Medium")
    color "#ffffff"
    size 16

style CelesteTopBar_button is button:
    padding (0, 0)
style CelesteTopBar_button_text is CelesteTopBar_text
