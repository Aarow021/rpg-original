from ShopItem import *
from Potion import *

class Shop:
    # Shop items
    items = {}
    def addItem(self, item):
        self.items[item.name] = item

    def buyItem(self, buyer, itemName):  
        if itemName not in self.items:
            print(f"Item \"{itemName}\" not in shop")
            return -1
        item = self.items[itemName]
        if buyer.gold < item.cost:
            print("Insufficient gold.")
            return -1
        item.bind(buyer)
        buyer.gold -= item.cost
    