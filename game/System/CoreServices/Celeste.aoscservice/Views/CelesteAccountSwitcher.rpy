#
# CelesteAccountSwitcher.rpy
# Celeste Shell - Account Switcher
#
# (C) 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 5

screen CelesteAccountSwitcher(users):
    tag CelesteAccounts
    zorder 105
    modal True
    style_prefix "ASInterface"

    on "show":
        action [
            Function(SetThumbnailFull),
            FileTakeScreenshot(),
            Function(SetThumbnailOriginal)
        ]

    if not ca_supports_blur():
        add FileCurrentScreenshot() at blur
    else:
        add FileCurrentScreenshot():
            blur CABlurType["default"]

    default s_users = [user for user in users if user != CAAccountsService.get_logged_in_user()]

    key "K_ESCAPE" action [Return(None)]

    frame at ASDynamicBlurTransition:
        xalign 0.5
        yalign 0.5
        xmaximum 700
        ymaximum 700
        padding (48, 48)

        has vbox:
            yalign 0.5

            label "Switch user profile"
            text "Select a user to switch to."

            for user in s_users:
                $ _username = user.display_name
                textbutton "[_username] ([user.username])" action [Return(user.username)]

            null height 32

            textbutton "Cancel" action [Return(None)]:
                xalign 0.5
