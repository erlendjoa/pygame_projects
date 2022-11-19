from player import Player
from move import Move

class Preset():
    def __init__(self):
        self._playerside = [(100, 500//3, 200, 100), (100, 500//3+120, 200, 20)]
        self._enemyside = [(900-250, 500//3, 200, 100), (900-250, 500//3+120, 200, 20)]
    def check_side(self, bool):
        if bool:
            side = self._playerside
        else:
            side = self._enemyside
        return side

    def get_Po(self, bool):
        po = Player(["xprojekt1", "Assets", "po.webp"], self.check_side(bool), "Po", 100)
        po.set_move(Move("Rock Smash", "ground", 25, 25))
        po.set_move(Move("Psychic Beam", "psychic", 35, 20))
        return po
    def get_TaiLung(self, bool):
        tailung = Player(["xprojekt1", "Assets", "tai_lung.webp"], self.check_side(bool), "Tai Lung", 120)
        tailung.set_move(Move("Hyper Beam", "normal", 10, 5))
        return tailung
    def get_Shifu(self, bool):
        shifu = Player(["xprojekt1", "Assets", "shifu.webp"], self.check_side(bool), "Master Shifu", 75)
        shifu.set_move(Move("Close Combat", "fighting", 45, 5))
        return shifu
