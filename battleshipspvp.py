from player import Player
import os

# Player versus player mode


class BattleshipsPVP:
    """creates a game of battlehsips"""
    def __init__(self):
        start = input("Begin? (y or n) -----> ")
        if start in ["y", "Y"]:
            self.playPVP()
        else:
            print("Aborted...")

    def playPVP(self):
        p1name = input("Player 1, state your name! -----> ")
        p1 = Player(p1name)
        p1.set_fleet()
        p1.view_console()
        self.clear_screen()

        p2name = input("\n\nPlayer 2, state your name! -----> ")
        p2 = Player(p2name)
        p2.set_fleet()
        p2.view_console()
        self.clear_screen()

        flag = True
        while flag is True:
            p1.strike(p2)
            if self.fleet_sunk(p2) is True:
                self.victory_message(p1, p2)
                flag = False
            else:
                self.clear_screen()

                p2.strike(p1)
                if self.fleet_sunk(p1) is True:
                    self.victory_message(p2, p1)
                    flag = False
                else:
                    self.clear_screen()
        print("\nThanks for playing!")

    # Function checks remaining ship counters on a player's board

    def fleet_sunk(self, player):
        ship_counters = 0
        """Traverses grid looking for 's' counters"""
        for row in range(len(player.ocean.ocean)):
            for col in range(len(player.ocean.ocean)):
                if player.ocean.ocean[row][col] == "S":
                    ship_counters += 1
        if ship_counters == 0:
            return True
        else:
            return False

    def clear_screen(self):
        input("\nNext Turn?")
        os.system('clear')

    def victory_message(self, winner, loser):
        print("\n\n\n*****************************************")
        print("%s's fleet has been destroyed, %s wins!" %
              (loser.name, winner.name))
        print("*****************************************")