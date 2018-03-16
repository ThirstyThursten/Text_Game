class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

class BrownBear(Enemy):
    def __init__(self):
        self.name = "Brown Bear"
        self.hp = 70
        self.damage = 10

class GrayWolf(Enemy):
    def __init__(self):
        self.name = "Gray Wolf"
        self.hp = 50
        self.damage = 8

class Bunny(Enemy):
    def __init__(self):
        self.name = "Bunny"
        self.hp = 10
        self.damage = 3

class RedFox(Enemy):
    def __init__(self):
        self.name = "Red Fox"
        self.hp = 30
        self.damage = 5
