from uke_09_oppg_9 import displayInventory

def addToInventory(inventory,addedItems):
    # lager en kopi som skal ta inn endringene 
    new_inventory = inventory.copy()
    # løper gjennom nøkklene i inventory
    for key in inventory:
        # løper gjennom de nye tingene
        for loot in addedItems:
            # sjekker om en nøkkel tilsvarer til de nye tingene
            if key in loot:
                # legger til 1
                new_inventory[key] += 1
            else:
                # hvis den nye tingen ikke er i inventory legges den til
                if loot not in inventory:
                    new_inventory[loot] = 1
    return new_inventory

inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = addToInventory(inv, dragonLoot)
print(displayInventory(inv))
