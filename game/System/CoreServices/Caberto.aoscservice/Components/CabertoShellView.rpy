#
# CabertoShellView.rpy
# Caberto Desktop Shell
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

screen CabertoShellView(wallpaper, apps):
    tag desktop
    modal False
    
    # Display the desktop wallpaper of choice.
    default wall = wallpaper
    add wall:
        size (1280, 720)
    
    # Display the top bar and the launcher on the side.
    use CabertoTopBar
    use CabertoLauncher(apps=apps)
    
    # Listen for changes on the set wallpaper and refresh the wallpaper.
    timer 0.25 action SetScreenVariable("wall", caberto._wallpaper) repeat True