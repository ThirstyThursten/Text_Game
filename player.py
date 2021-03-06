import items
import world
#import crafting


class Player:
    def __init__(self):
        self.inventory = [items.Rock(),
                            items.Dagger(),
                            items.CrustyBread(),
                            items.Raspberries()
                            ]
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 150
        self.gold = 15
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print ("Inventory:")
        for item in self.inventory:
            print('* ' + str(item))
        print("- Gold: {}".format(self.gold))
        print("- Health Points: {}".format(self.hp))

    def heal(self):
        consumables = [item for item in self.inventory
                        if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return

        print("Your HP is: {}".format(self.hp))
        print("Choose an item to use to heal:")
        for i, item in enumerate(consumables, 1):
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(150, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

### CRAFT FUNCTION (WIP)
#    def craft(self):
#        craftables = [item for item in self.inventory
#                        if isinstance(item, items.Crafting)]
#            print("You don't have any Craftable items!")
#            return

#        firepit =
###

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)

    def add_item(self):
        room = world.tile_at(self.x, self.y)
        room.encounter_fruit(self)

    def cook(self):
        room = world.tile_at(self.x, self.y)
        room.check_cook(self)

