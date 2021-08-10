#
# ASInventorySubView.rpy
# Candella
#
# Created by Marquis Kurt on 9/13/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

screen ASInventorySubView():
    style_prefix "ASInterface"
    zorder 100
    modal True

    default top_items = []

    python:
        if len(inventory.retrieve()) > 0:
            for item in inventory.export():
                top_items.append(item)

            if len(top_items) > 4:
                top_items = top_items[:5]


    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 900
        ymaximum 180

        hbox:
            yfill True
            for item in top_items:
                button action [Function(inventory.useItem, item), Hide("ASInventorySubView")]:
                    style "ASInventorySubButton"
                    has vbox:
                        yfit True
                        add item.imageName

                        text "[item.name]":
                            xalign 0.5
            button action [Show("ASInventoryManagerView"), Hide("ASInventorySubView")]:
                    style "ASInventorySubButton"
                    has vbox:
                        yfit True
                        add AS_DEFAULT_APP_DIR + "Inventories.aosapp/Resources/OpenMore.png"

                        text _("More Items..."):
                            xalign 0.5

style ASInventorySubButton:
    hover_background "#333333"
