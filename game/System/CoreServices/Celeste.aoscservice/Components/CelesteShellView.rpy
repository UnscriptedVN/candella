#
# CelesteShellView.rpy
# Celeste Desktop Shell
#
# (C) 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

screen CelesteShellView(wallpaper, apps):
    tag desktop
    modal False

    # Display the desktop wallpaper of choice.
    default wall = wallpaper
    add wall at truecenter:
        size (1280, 720)
        fit celeste._wall_display_mode

    # Display the top bar and the launcher on the side.
    use CelesteLauncher(apps=apps)
    use CelesteTopBar

    # Listen for changes on the set wallpaper and refresh the wallpaper.
    timer 0.25 action SetScreenVariable("wall", celeste._wallpaper) repeat True
