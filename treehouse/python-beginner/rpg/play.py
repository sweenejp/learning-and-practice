from rpg.thieves import Thief
from rpg.inventory import Inventory
from rpg.items import Item
from rpg.items import Weapon

jimmy = Thief(name="Jimmy", sneaky=False)
print(jimmy.sneaky)
print(jimmy.hide(9))

inventory = Inventory()
coin = Item('coin', 'a gold coin')
sword = Weapon('sword', 'sharp', 100)

inventory.add(coin)
inventory.add(sword)

print(inventory.__len__())
print(inventory.__contains__(sword))
for item in inventory:
    print(item.description)
    print(item.name)

print("**********************")
for item in inventory:
    if isinstance(item, Weapon):
        print(item.power)
