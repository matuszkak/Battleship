from battleshipspvp import BattleshipsPVP
from computer import Computer
from player import Player


class BattleshipsCOMP(BattleshipsPVP):
    def __init__(self):
        start = input("Begin? (y or n) -----> ")
        if start in ["y", "Y"]:
            self.playCOMP()
        else:
            print("Aborted...")

    def playCOMP(self):
        pname = input("Player 1, state your name! -----> ")
        p = Player(pname)
        p.set_fleet()
        p.view_console()
        self.clear_screen()

        c = Computer()
        print("Computer setting its fleet...")
        c.set_compu_fleet()
        self.clear_screen()

        flag = True
        while flag is True:
            p.strike(c)
            if self.fleet_sunk(c) is True:
                self.victory_message(p, c)
                flag = False
            else:
                self.clear_screen()

                c.compu_strike(p)
                if self.fleet_sunk(p) is True:
                    self.victory_message(c, p)
                    flag = False
                else:
                    self.clear_screen()
        print("\nThanks for playing!")