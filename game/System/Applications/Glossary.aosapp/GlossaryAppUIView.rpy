#
# GlossaryAppUIView.rpy
# Glossary App UI
#
# Created by Marquis Kurt on 12/03/20.
# Copyright © 2020-2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

screen GlossaryAppUIView(glossary):
    style_prefix "ASInterface"
    zorder 100
    # modal True

    drag:
        drag_name "GlossaryAppUIView"
        drag_handle (0, 0, 800, 64)
        xalign 0.5
        yalign 0.5

        frame:
            xmaximum 800
            ymaximum 450

            has vbox:
                use ASInterfaceTitlebar(_("Glossary"), onClose=[Hide("GlossaryAppUIView"), Function(glossary_app.terminate)])

                viewport:
                    mousewheel True
                    scrollbars "vertical"
                    style_prefix "ASInterfaceScrollbar"

                    vbox:
                        spacing 16
                        if glossary:
                            use GlossaryView(glossary=glossary)
                        else:
                            text _("The glossary is empty or could not be loaded.")

screen GlossaryView(glossary):
    style_prefix "glossary"
    for word in sorted(glossary):
        python:
            _wd = word.replace("_", " ")
            _definition = glossary[word]
        hbox:
            label "[_wd!c]"
            text "[_definition]"

style glossary_label is help_label
style glossary_label_text is help_label_text:
    font get_font("Ubuntu", variant="Bold")
    size 16
style glossary_text is ASInterface_text:
    font get_font("Ubuntu", variant="Light")
    size 16
