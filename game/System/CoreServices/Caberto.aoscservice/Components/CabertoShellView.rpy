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
    add wallpaper
    
    # Display the top bar and the launcher on the side.
    use CabertoTopBar
    use CabertoLauncher(apps=apps)