from player import Player
from move import Move

class Preset():
    def __init__(self):
        self._playerside = [(100, 500//3, 200, 100), (100, 500//3+120, 200, 20)]
        self._enemyside = [(900-250, 500//3, 200, 100), (900-250, 500//3+120, 200, 20)]

        self._rock_smash = Move("Rock Smash", "ground", 20, 25)
        self._psychic_beam = Move("Psychic Beam", "psychic", 35, 20)
        self._grass_knot = Move("Grass Knot", "grass", 30, 15)
        self._bubble = Move("Bubble", "water", 30, 15)
        self._scratch = Move("Scratch", "fighting", 20, 25)
        self._ember = Move("Ember", "fire", 30, 15)

    def check_side(self, bool):
        if bool:
            side = self._playerside
        else:
            side = self._enemyside
        return side

    def get_Po(self, bool):
        po = Player(["BestGameEverMade", "Assets", "po.webp"], self.check_side(bool), "Po", "normal", 500)
        po.set_move(self._rock_smash)
        po.set_move(self._psychic_beam)
        return po
    def get_Turtwig(self, bool):
        turtwig = Player(["BestGameEverMade", "Assets", "turtwig.png"], self.check_side(bool), "Turtwig", "grass", 500)
        turtwig.set_move(self._rock_smash)
        turtwig.set_move(self._grass_knot)
        return turtwig
    def get_Piplup(self, bool):
        piplup = Player(["BestGameEverMade", "Assets", "piplup.png"], self.check_side(bool), "Piplup", "water", 500)
        piplup.set_move(self._bubble)
        return piplup
    def get_Charmander(self, bool):
        charmander = Player(["BestGameEverMade", "Assets", "charmander.png"], self.check_side(bool), "Charmander", "fire", 500)
        charmander.set_move(self._scratch)
        charmander.set_move(self._ember)
        return charmander
