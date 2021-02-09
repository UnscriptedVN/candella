#
# Inventories.rpy
# Candella
#
# Created by Marquis Kurt on 9/13/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

init 5 python:
    import logging

    class ASInventories(CAApplication):
        inventory = []

        def __init__(self):
            CAApplication.__init__(self, AS_DEFAULT_APP_DIR + "Inventories.aosapp/")

        @property
        def empty(self):
            return self.isEmpty()

        def applicationWillLaunch(self):
            renpy.show_screen("ASInventoryManagerView")
            return

        def callRecentItems(self):
            renpy.show_screen("ASInventorySubView")
            return

        def call_recent_items(self):
            self.callRecentItems()

        def isEmpty(self):
            return len(self.inventory) == 0

        def retrieve(self):
            clog.warn("ASInventories.retrieve is deprecated. Please use ASInventories.export instead.")
            return self.export()

        def export(self, filter=None):
            new_inventory = self.inventory.copy()
            if callable(filter):
                new_inventory = map(filter, new_inventory)
            return new_inventory

        def containsItem(self, item):
            return item in self.inventory

        def contains_item(self, item):
            return self.containsItem(self, item)

        def getItemById(self, itemId):
            for item in self.inventory:
                if item.itemId == itemId:
                    return item
            return None

        def get_item_by_id(self, itemId):
            return self.getItemById(itemId)

        def getItemByName(self, name):
            for item in self.inventory:
                if item.name == name:
                    return item
            return None

        def get_item_by_name(self, name):
            return self.getItemByName(name)

        def addItem(self, item, silent=False):
            if not isinstance(item, ASInventoryItem):
                raise TypeError("Expected item to be ASInventoryItem, but received %s" % (type(item)))
            self.inventory.append(item)
            if not silent:
                shouldDisplayItem = self.applicationWillRequestNotification("%s received!" % (item.name), "Go to Inventories to learn more.")

                if shouldDisplayItem == "didClickRespond":
                    renpy.show_screen("ASInventoryManagerView", currentItem=item)

        def add_item(self, item, silent=False):
            self.addItem(item, silent=silent)

        def useItem(self, item):
            if item not in self.inventory:
                raise KeyError("Item not found in the inventory: %s" % (item,) )
            shouldDispose = item.useItem()

            if shouldDispose:
                self.inventory.remove(item)

        def use_item(self, item):
            self.useItem(item)

        def removeItem(self, item):
            if item not in self.inventory:
                raise KeyError("Item not found in the inventory: %s" % (item,) )
            self.inventory.remove(item)

        def remove_item(self, item):
            self.removeItem(item)

        def importFromList(self, list):
            listAsInventoryChecks = map(lambda x: isinstance(x, ASInventoryItem), list)
            isInventoryReal = reduce(lambda x, y: x and y, listAsInventoryChecks)

            if not isInventoryReal:
                raise TypeError("List contains non-ASInventoryItem items.")

            for item in list:
                self.inventory.append(item)

        def import_from_list(self, list):
            self.importFromList(list)

    inventory = ASInventories()
