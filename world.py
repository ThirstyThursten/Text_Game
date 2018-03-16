import enemies
import npc
import random
import items

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass

class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in the middle
        of a nice but gloomy forest.
        You can make out what seems to be four paths,
        that cut through the thick thriving bushes.
        """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.40:
            self.enemy = enemies.Bunny()
            self.alive_text = "A cute little bunny crossed your path! " \
                                "It should be slain before you can continue.."
            self.dead_text = "The dead bunny is just laying there, bleeding.."
            self.loot = items.BunnyMeat()

        elif r < 0.55:
            self.enemy = enemies.RedFox()
            self.alive_text = "A red fox strides across from you!"
            self.dead_text = "The blood of the dead fox mixes well with its fur.."
            self.loot = items.FoxMeat()

        elif r < 0.70:
            self.enemy = enemies.GrayWolf()
            self.alive_text = "You hear a wolf howling, " \
                                "as it gets ready to attack you.."
            self.dead_text = "You try to catch your breath while standing over " \
                                "the wolfs bleeding corpse.."
            self.loot = items.WolfMeat()

        else:
            self.enemy = enemies.BrownBear()
            self.alive_text = "You hear a loud thudding and a boisterous growl.. " \
                                "A bear stands in front of you.."
            self.dead_text = "You swipe the dust off of your clothes as you feel victorious " \
                                "Looking at the dead pile of bear meat.."
            self.loot = items.BearMeat()

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        loot_chance = random.random()
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))
        elif loot_chance < 0.60 and not self.enemy.is_alive():
            player.inventory.append(self.loot)
            print(" The {} dropped {} it's been added to your inventory.".format(self.enemy, self.loot.name))


class ForagingTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        self.item_claimed = False

        if r < 0.50:
            self.item = items.Raspberries()
            self.available_text = "You find some bushes that seems to have " \
                                    "some Raspberries in them, you forage 'em."
            self.nofruit_text = "A beautiful part of the forest... " \
                                        "You must forge onwards."
        elif r < 0.75:
            self.item = items.Toadstools()
            self.available_text = "Some Toadstools grow in the shades of a big tree, " \
                                    "You pick them up, but you don't know what they do.."
            self.nofruit_text = "A beautiful part of the forest... " \
                                        "You must forge onwards."
        else:
            self.item = items.BlueBerries()
            self.available_text = "You see some bushes in front of you, " \
                                    "some Blueberries thrive in them, " \
                                    "you foraged them."
            self.nofruit_text = "A beautiful part of the forest... " \
                                        "You must forge onwards."

        super().__init__(x, y)

    def modify_player(self, player):
        if not self.item_claimed:
            self.item_claimed = True
            player.inventory.append(self.item)
            print(" The {} have been added to your inventory.".format(self.item.name))

    def intro_text(self):
        nofruit = self.nofruit_text
        fruit = self.available_text
        if self.item_claimed:
            return nofruit
        else:
            return fruit

class BoringTile(MapTile):
    def intro_text(self):
        return """
        It's just a straight path... Not so much going on here..
        """

class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        You see a faint light in the far distance..
        ... As you come closer ...
        ... It seems to be an opening,
        a clearing in the forest.
        You're at a nice village where you will be safe.

        Congrats!!! Victory is yours!!
        """

class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(18, 75)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} Gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
            A beautiful part of the forest... You must forge onwards.
            """
        else:
            return """
            Someone dropped some gold! You pick it up!
            """

class MerchantTile(MapTile):
    def __init__(self, x, y):
        self.merchant = npc.Merchant()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("You can spend: {}".format(player.gold))
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.merchant)
            elif user_input in ['S', 's']:
                print("This is what I can afford: {}".format(self.merchant.gold))
                print("And here's what you can sell: ")
                self.trade(buyer=self.merchant, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive..")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Pleasure doing bussiness with you!")

    def intro_text(self):
        return """
        An old man with a long beard is standing in the shade of a tree.
        He clinks his gold coins together. Apparently he's a merchant!
        He looks willing to trade.
        """

class BlackSmithTile(MapTile):
    def __init__(self, x, y):
        self.blacksmith = npc.BlackSmith()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Your Gold: {}".format(player.gold))
                print("Here's what I got available for purchase: ")
                self.trade(buyer=player, seller=self.blacksmith)
            elif user_input in ['S', 's']:
                print("Here's how much I have to spend: {}".format(self.blacksmith.gold))
                print("And this is what you can sell:")
                self.trade(buyer=self.blacksmith, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit.")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("Sorry that's not enough gold.")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Thanks for the bussiness!")

    def intro_text(self):
        return """
        You come across a little cabin,
        it has a hot fire burning in some sort of oven.
        A man is busy forging some metal,
        in what seems to become a sword.
        The Blacksmith seems to be willing to trade.
        """


world_dsl = """
|EN|EN|VT|EN|EN|BS|
|BS|  |  |  |BS|EN|
|FG|MT|FT|FG|EN|FG|
|EN|FG|EN|  |MT|EN|
|MT|FT|ST|FG|EN|FT|
|FG|  |  |  |FG|  |
"""
def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True

tile_type_dict = {"VT": VictoryTile,
                    "EN": EnemyTile,
                    "ST": StartTile,
                    "FG": FindGoldTile,
                    "MT": MerchantTile,
                    "BS": BlackSmithTile,
                    "FT": ForagingTile,
                    "  ": None}

world_map = []

start_tile_location = None

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
