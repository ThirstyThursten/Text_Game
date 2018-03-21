class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name

class Crafting:
    def __init__(self):
        raise NotImplementedError("Do not create raw Crafting items.")

    def __str__(self):
        self.name

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__ (self):
        return "{} (+{} HP)".format(self.name, self.healing_value)

class Craftable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Craftable items.")

    def __str__(self):
        return self.name

class RawMeat:
    def __init__(self):
        raise NotImplementedError("Don't create raw RawMeat items.")

    def __str__ (self):
        return "{} (+{} HP)".format(self.name, self.healing_value)

class CookedMeat:
    def __init__(self):
        raise NotImplementedError("Don't create any raw CookedMeat items.")

    def __str__ (self):
        return "{} (+{} HP)".format(self.name, self.healing_value)



class Rock(Weapon, Crafting):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5
        self.value = 1

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust here and there. " \
                            "Somewhat more dangerous than a rock."
        self.damage = 10
        self.value = 20

class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing its age, " \
                            "but still has some fight in it."
        self.damage = 20
        self.value = 100

class Axe(Weapon):
    def __init__(self):
        self.name = "Axe"
        self.description = "An axe, made for chopping trees, " \
                            "but it might be able to chop more than just trees.."
        self.damage = 15
        self.value = 80

class CrossBow(Weapon):
    def __init__(self):
        self.name = "Crossbow"
        self.description = "An old Crossbow its a little worn, " \
                            "but it still has a pretty good range."
        self.damage = 35
        self.value = 120



class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 20
        self.value = 12

class BlueBerries(Consumable):
    def __init__(self):
        self.name = "Blue Berries"
        self.healing_value = 18
        self.value = 15

class Raspberries(Consumable):
    def __init__(self):
        self.name = "Raspberries"
        self.healing_value = 10
        self.value = 10

class Toadstools(Consumable):
    def __init__(self):
        self.name = "Toadstools"
        self.healing_value = -5
        self.value = 10



class RawBunnyMeat(RawMeat, Consumable):
    def __init__(self):
        self.name = "Raw Bunny meat"
        self.healing_value = 10
        self.value = 20
        self.id = 1

class RawFoxMeat(RawMeat, Consumable):
    def __init__(self):
        self.name = "Raw Fox meat"
        self.healing_value = 15
        self.value = 25
        self.id = 2

class RawWolfMeat(RawMeat, Consumable):
    def __init__(self):
        self.name = "Wolf meat"
        self.healing_value = 20
        self.value = 30
        self.id = 3

class RawBearMeat(RawMeat, Consumable):
    def __init__(self):
        self.name = "Bear meat"
        self.healing_value = 35
        self.value = 40
        self.id = 4

class CookedBunnyMeat(CookedMeat, Consumable):
    def __init__(self):
        self.name = "Cooked Bunny meat"
        self.healing_value = 25
        self.value = 30
        self.id = 5

class CookedFoxMeat(CookedMeat, Consumable):
    def __init__(self):
        self.name = "Cooked Fox meat"
        self.healing_value = 30
        self.value = 35
        self.id = 6

class CookedWolfMeat(CookedMeat, Consumable):
    def __init__(self):
        self.name = "Cooked Wolf meat"
        self.healing_value = 35
        self.value = 40
        self.id = 7

class CookedBearMeat(CookedMeat, Consumable):
    def __init__(self):
        self.name = "Cooked Bear meat"
        self.healing_value = 50
        self.value = 50
        self.id = 8


class FirePit(Craftable):
    def __init__(self):
        self.name = "Firepit"



class Stick(Crafting):
    def __init__(self):
        self.name = "Stick"
