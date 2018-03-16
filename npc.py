import items


class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name


class Merchant(NonPlayableCharacter):
    def __init__(self):
        self.name = "Merchant"
        self.gold = 100
        self.inventory = [items.CrustyBread(),
                            items.Raspberries(),
                            items.Raspberries(),
                            items.BlueBerries(),
                            items.BlueBerries(),
                            items.Toadstools(),
                            items.Toadstools(),]
