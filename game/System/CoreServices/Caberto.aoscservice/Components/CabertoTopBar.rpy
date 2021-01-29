#
# CabertoTopBar.rpy
# Caberto Desktop Shell
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

screen CabertoTopBar():
    tag desktop
    modal False
    style_prefix "CabertoTopBar"
    
    default _CurrentTime = "Tue. 9:41 AM"
    default _Username = "User"
    default _CurrentApp = ""
    
    python:
        _CurrentTime = CabertoShell.current_time()
        _user = CAAccountsService.get_logged_in_user()
        _Username = _user.display_name
        _CurrentApp = caberto._current_app_name
        
    timer 0.5 action [SetScreenVariable("_CurrentApp", caberto._current_app_name), SetScreenVariable("_CurrentTime", CabertoShell.current_time())] repeat True
        
    frame:
        xfill True
        ysize 28
        
        has hbox:
            xfill True
            text "[_CurrentApp]":
                style "CabertoTopBar_AppName"
            
            hbox:
                xalign 1.0
                spacing 8
                
                text "[_Username]"
                text "[_CurrentTime]"
                
                button action Show("CabertoSettings"):
                    xysize (24, 18)
                    add caberto.bundleDir + "Resources/settings.png":
                        size (18, 18)
                        align (0.5, 0.5)
                
                button action Return("CabertoShellView"):
                    xysize (24, 18)
                    add caberto.bundleDir + "Resources/logoff.png":
                        size (18, 18)
                        align (0.5, 0.5)
            
style CabertoTopBar_frame is frame:
    margin (0, 0)
    xpadding 8
    background "#191919"
    
style CabertoTopBar_hbox is hbox:
    spacing 8
    
style CabertoTopBar_text is ASSystemRegularFont:
    size 16

style CabertoTopBar_AppName is ASSystemMediumFont:
    size 16