

class Inventory:
    def __init__(self):
        self.slots = []


    def add_item(self, item):
        self.slots.append(item)


class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)
        self.slots.sort()


new_inventory = Inventory()
new_inventory.add_item("chicken")
new_inventory.add_item("beef")

sort_inv = SortedInventory()
sort_inv.add_item("butts")
sort_inv.add_item("apples")
print(new_inventory.slots)
print(sort_inv.slots)
