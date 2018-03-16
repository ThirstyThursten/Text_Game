class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name

class Rock(Weapon):
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

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__ (self):
        return "{} (+{} HP)".format(self.name, self.healing_value)

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
