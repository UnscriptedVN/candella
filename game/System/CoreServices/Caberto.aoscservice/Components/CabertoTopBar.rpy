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
    
    python:
        _CurrentTime = CabertoShell.current_time()
        _user = CAAccountsService.get_logged_in_user()
        _Username = _user.display_name
        
    timer 0.5 action SetScreenVariable("_CurrentTime", CabertoShell.current_time()) repeat True
        
    frame:
        xfill True
        ysize 28
        
        has hbox:
            xalign 1.0
            
            spacing 8
            
            text "[_Username]"
            text "[_CurrentTime]"
            
            button action Return("CabertoShellView"):
                xysize (24, 18)
                add caberto.bundleDir + "Resources/logoff.png":
                    size (18, 18)
                    align (0.5, 0.5)
            
style CabertoTopBar_frame is frame:
    margin (0, 0)
    xpadding 16
    background "#212121"
    
style CabertoTopBar_hbox is hbox:
    spacing 8
    
style CabertoTopBar_text is ASSystemRegularFont:
    size 16