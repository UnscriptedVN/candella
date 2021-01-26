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
            
        def __eq__(self, other):
            return isinstance(other, ASInventoryItem) and (self.itemId == other.itemId or self.name == other.name)
            
        def __ne__(self, other):
            return not self.__eq__(other)
            
        def __repr__(self):
            return "ASInventoryItem(%s, %s)" % (self.name, self.description)
        
        def __str__(self):
            return self.__repr__()

        def useItem(self):
            if not self.canBeUsed:
                logging.warn("This item cannot be used.")
                return False
        
            if self.runSpecialUseCase is not None:
                self.runSpecialUseCase()
            
            if self.canBeUsedOnce:
                self.canBeUsed = False
                return True
