#
# ASAppManagerView.rpy
# Candella
#
# Created by Marquis Kurt on 9/9/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

screen ASAppManagerView():
    style_prefix "ASInterface"

    python:
        apps = appManager.gather_applications()

    default currentAppView = None

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 900
        ysize 600

        has vbox:
            xalign 0.5
            yfit True

            use ASInterfaceTitlebar("App Manager", onClose=Hide("ASAppManagerView"))

            hbox:
                style_prefix "ASAppManager"
                spacing 8

                vbox:
                    spacing 8
                    label "Applications"

                    viewport:
                        style_prefix "ASInterfaceScrollbar"
                        mousewheel True
                        scrollbars "vertical"
                        style "ASAppManager_viewport"

                        vbox:
                            for app in apps:
                                use ASAppManagerDetailButton(app)


                vbox:
                    xfill True
                    if currentAppView == None:
                        text "Select an app from the left side to view its properties.":
                            xalign 0.5


                    else:
                        hbox:
                            spacing 12

                            add currentAppView.icons[128]:
                                zoom 0.9

                            vbox:
                                $ _app_name = appManager.get_app_name(currentAppView)
                                label "[_app_name]":
                                    style "ASAppManager_DetailedAppName"
                                text "[currentAppView.bundleAuthor]":
                                    style "ASAppManager_DetailedAppAuthor_text"
                                text "Version [currentAppView.bundleVersion] ([currentAppView.bundleId])"
                                null height 8

                                textbutton "Launch" action Function(currentAppView.applicationWillLaunch):
                                    style "ASInterfacePushButton"

                        null height 8

                        vbox:
                            $ currentAppView_description = currentAppView.bundleDescription.strip()
                            text "About this app":
                                style "ASAppManager_DetailedEmphasis_text"
                            text "[currentAppView_description]"
                            null height 16

                            if currentAppView.requires:

                                text "Allow this app to:":
                                    style "ASAppManager_DetailedEmphasis_text"

                                vbox:
                                    style_prefix "ASInterfaceCheckbox"
                                    spacing 8

                                    if AS_REQUIRES_NOTIFICATIONKIT in currentAppView.requires:
                                        textbutton "Send notifications" action ToggleDict(persistent.AS_PERMISSIONS[currentAppView.bundleId], AS_REQUIRES_NOTIFICATIONKIT, True, False)
                                        text "Notifications may include banners, alerts, and sounds.":
                                            style "ASAppManager_text"

                                    if AS_REQUIRES_FULL_DISK_ACCESS in currentAppView.requires:
                                        textbutton "Access your files" action ToggleDict(persistent.AS_PERMISSIONS[currentAppView.bundleId], AS_REQUIRES_FULL_DISK_ACCESS, True, False)
                                        text "File access may include your Home directory and your Candella installation.":
                                            style "ASAppManager_text"

                                    if AS_REQUIRES_SYSTEM_EVENTS in currentAppView.requires:
                                        textbutton "Change settings and watch system events" action ToggleDict(persistent.AS_PERMISSIONS[currentAppView.bundleId], AS_REQUIRES_SYSTEM_EVENTS, True, False)
                                        text "This may include changing Candella settings or watching system events such as startup.":
                                            style "ASAppManager_text"
                            else:
                                text "This app doesn't require any permissions."
                                
screen ASAppManagerDetailButton(app):
    button action SetScreenVariable("currentAppView", app):
        ymaximum 56
        xsize 300
        has hbox:
            spacing 8
    
            add app.icons[48]
            vbox:
                python:
                    _name = appManager.get_app_name(app)
                    _author = app.bundleAuthor if len(app.bundleAuthor) < 32 else app.bundleAuthor[0:31] + "..."
                text "[_name]":
                    style "ASAppManager_AppName_text"
                text "[_author]"
