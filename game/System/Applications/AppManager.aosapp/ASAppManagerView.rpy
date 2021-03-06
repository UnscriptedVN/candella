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
        apps = CelesteShell.get_all_applications()

    default currentAppView = None

    drag:
        drag_name "ASAppManagerView"
        drag_handle (0, 0, 900, 64)
        xalign 0.5
        yalign 0.5


        frame:
            xmaximum 900
            ysize 600

            has vbox:
                xalign 0.5
                yfit True

                use ASInterfaceTitlebar("App Manager", onClose=[Hide("ASAppManagerView"), appManager.terminate])

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

                                add CADesign.get_app_mask(currentAppView.icons[128], 128):
                                    zoom 0.9

                                vbox:
                                    $ _app_name = appManager.get_app_name(currentAppView)
                                    label "[_app_name]":
                                        style "ASAppManager_DetailedAppName"
                                    text "[currentAppView.bundleAuthor]":
                                        style "ASAppManager_DetailedAppAuthor_text"
                                    text "Version [currentAppView.bundleVersion] ([currentAppView.bundleId])"
                                    null height 8

                                    hbox:
                                        spacing 8

                                        textbutton "Launch" action Function(currentAppView.applicationWillLaunch):
                                            style "ASInterfacePushButton"

                                        vbox:
                                            style_prefix "ASInterfaceCheckbox"
                                            textbutton "Pin to launcher" action Function(appman._pin_to_shell_dock, app_id=currentAppView.bundleId):
                                                selected celeste.app_exists_in_current_launcher(currentAppView.bundleId)

                            null height 8

                            vbox:
                                $ currentAppView_description = currentAppView.bundleDescription.strip()
                                text "About this app":
                                    style "ASAppManager_DetailedEmphasis_text"
                                text "[currentAppView_description]"
                                null height 16

                                if currentAppView.permissions:

                                    text "Allow this app to:":
                                        style "ASAppManager_DetailedEmphasis_text"

                                    vbox:
                                        style_prefix "ASInterfaceCheckbox"
                                        spacing 8

                                        for _permission in currentAppView.permissions:
                                            $ _perm_class = CA_PERMISSIONS[_permission]
                                            $ _desc = _perm_class.description.split(".")[0]
                                            textbutton "[_perm_class.name!cl]" action ToggleDict(persistent.AS_PERMISSIONS[currentAppView.bundleId], _perm_class.key, True, False)
                                            text "[_desc].":
                                                style "ASAppManager_text"
                                else:
                                    text "This app doesn't require any permissions."

screen ASAppManagerDetailButton(app):
    button action SetScreenVariable("currentAppView", app):
        ymaximum 56
        xsize 300
        has hbox:
            spacing 8

            add CADesign.get_app_mask(app.icons[48], 48)
            vbox:
                python:
                    _name = appManager.get_app_name(app)
                    _ver = app.bundleVersion
                text "[_name]":
                    style "ASAppManager_AppName_text"
                text "v[_ver]"
