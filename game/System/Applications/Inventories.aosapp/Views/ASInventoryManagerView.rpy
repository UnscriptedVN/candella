#
# ASInventoryManagerView.rpy
# Candella
#
# Created by Marquis Kurt on 9/13/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

screen ASInventoryManagerView(currentItem=None):
    style_prefix "ASInterface"
    zorder 100
    modal True

    $ inv = inventory.export()

    default currentItemView = currentItem

    drag:
        drag_name "ASInventoryManagerView"
        drag_handle (0, 0, 1000, 64)
        xalign 0.5
        yalign 0.5

        frame:
            xmaximum 1000
            ysize 650

            has vbox:
                xalign 0.5
                yfit True

                use ASInterfaceTitlebar(_("Inventories"), onClose=Hide("ASInventoryManagerView"))

                if len(inv) == 0:
                    vbox:
                        xfill True
                        yfill True
                        yalign 0.5

                        null height 1

                        vbox:
                            style_prefix "ASInventories"
                            xalign 0.5

                            add AS_DEFAULT_APP_DIR + "Inventories.aosapp/Resources/Item.png":
                                xalign 0.5
                            label _("No items available."):
                                xalign 0.5
                            text _("You don't have any items in your inventory yet."):
                                xalign 0.5

                        null height 1
                else:
                    hbox:
                        style_prefix "ASInventories"
                        spacing 8

                        vbox:
                            spacing 8
                            label _("Inventory")

                            viewport:
                                style_prefix "ASInterfaceScrollbar"
                                mousewheel True
                                scrollbars "vertical"
                                style "ASInventories_viewport"

                                vbox:
                                    for item in inv:
                                        button action SetScreenVariable("currentItemView", item):
                                            ymaximum 56
                                            xsize 300
                                            sensitive True
                                            style "ASInventories_button"

                                            has hbox:
                                                yalign 0.5

                                                add item.imageName:
                                                    zoom 0.5
                                                    yalign 0.5

                                                label "[item.name]":
                                                    yalign 0.5
                                                    style "ASInventoriesItemName"


                        vbox:
                            xfill True

                            if currentItemView == None:
                                text _("Select an item from the left side to view and use it."):
                                    xalign 0.5

                            else:
                                hbox:
                                    spacing 12

                                    add currentItemView.imageName:
                                        zoom 0.9

                                    vbox:
                                        label "[currentItemView.name]"
                                        null height 8

                                        $ ItemAction = Function(inventory.useItem, currentItemView) if currentItemView.canBeUsed else NullAction()

                                        textbutton _("Use Item") action ItemAction:
                                            style "ASInterfacePushButton"
                                            sensitive currentItemView.canBeUsed

                                        if not currentItemView.canBeUsed:
                                            text _("This item can't be used.")

                                null height 8
                                vbox:
                                    $ ItemDescription = currentItemView.description.strip()
                                    text "[currentItemView.description]"
                                    null height 8



style ASInventories_label is gui_label
style ASInventories_label_text is ASInterface_text:
    font get_font("Ubuntu", variant="Bold")
    size 32

style ASInventories_viewport is ASInterfaceScrollbar:
    xsize 300
    yfill True

style ASInventories_button is gui_button:
    hover_background "#333333"

style ASInventoriesItemName is ASInventories_label
style ASInventoriesItemName_text is ASInventories_label_text:
    size 20

style ASInventories_text is ASInterface_text:
    font get_font("Ubuntu")
