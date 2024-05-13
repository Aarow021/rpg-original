class ShopItem:
    def __init__(self, item, cost, type, displayName=None, description=""):
        if displayName == None:
            displayName = item.name
        self.item = item
        self.cost = cost
        self.type = type
        self.displayName = displayName
        self.description = description
        self.name = item.name
        self.bind = item.bind
        self.gain = item.gain