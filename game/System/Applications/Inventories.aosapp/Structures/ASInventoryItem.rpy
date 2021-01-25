#
# ASInventoryItem.rpy
# Candella
#
# Created by Marquis Kurt on 9/13/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

init 10 python:
    import logging
    class ASInventoryItem(object):

        def __init__(self, itemId=None, name="Item", description="", canBeUsed=True, specialUseCase=None, canBeUsedOnce=False, imageName=ASInventories.bundleDir + "Resources/Item.png"):
            self.name = name
            self.description = description
            self.canBeUsed = canBeUsed
            self.canBeUsedOnce = canBeUsedOnce
            self.runSpecialUseCase = specialUseCase if callable(specialUseCase) else None
            self.imageName = imageName
            self.itemId = itemId

        def useItem(self):
            if self.canBeUsed:
                if self.runSpecialUseCase is not None:
                    self.runSpecialUseCase()
                if self.canBeUsedOnce:
                    self.canBeUsed = False
                    return True

            else:
                logging.warn("This item cannot be used.")
                return False
