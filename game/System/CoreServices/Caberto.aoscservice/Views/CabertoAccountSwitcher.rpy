#
# CabertoAccountSwitcher.rpy
# Caberto Shell - Account Switcher
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = 5

screen CabertoAccountSwitcher(users):
    tag CabertoAccounts
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
    