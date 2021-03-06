#
# CelesteDrawer.rpy
# Celeste Desktop Shell
#
# (C) 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init screen CelesteDrawer():
    style_prefix "CelesteDrawer"
    modal False

    default all_apps = []
    default app_filter = ""

    python:
        X = sorted(
            celeste.get_all_applications(),
            key=lambda app: app.get_name() if isinstance(app, CAApplication) else app.bundleName
        )
        all_apps = [app for app in X if celeste.include_in_search(app_filter, app)]

    key "K_ESCAPE" action Function(celeste.drawer)

    frame:
        xsize 700
        yfill True

        has vbox:
            spacing 32

            $ _search_offset = 0 if app_filter else -22
            vbox:
                yoffset _search_offset
                if not app_filter:
                    text "Search...":
                        style "CelesteDrawer_input"
                        yoffset 22
                input default "" value ScreenVariableInputValue("app_filter"):
                    xfill True

            hbox:
                box_wrap True

                for app in all_apps:
                    python:
                        _app_name = app.get_name() if isinstance(app, CAApplication) else app.bundleName

                        if len(_app_name) > 36:
                            _app_name = _app_name[:34] + "..."

                    button action [
                        Function(celeste.drawer), Function(celeste.launch_app_bundle, app_bundle=app)
                    ]:
                        xysize(96, 128)
                        sensitive True

                        vbox:
                            xfill True
                            yfill True

                            add CADesign.get_app_mask(app.icons[64], 64):
                                xalign 0.5
                            text "[_app_name]":
                                xalign 0.5
                                text_align 0.5



style CelesteDrawer_frame is frame:
    margin (0, 0)
    top_margin 28
    left_margin 72
    padding(24, 16)
    background "#080808EE"

style CelesteDrawer_text is text:
    font get_font("Ubuntu", "Regular")
    size 16

style CelesteDrawer_input is CelesteDrawer_text:
    color "#999999"
    size 20
