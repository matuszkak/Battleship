from ocean import Ocean
from radar import Radar
from ship import Ship
import os


class Player:

    ships = {
        "Aircraft Carrier": 5,
        "Crusier": 4,
        "Destroyer": 3,
        "Submarine": 2
    }

    def __init__(self, name):
        self.ocean = Ocean()
        self.radar = Radar()
        self.name = name
        self.fleet = []

# Function uses player input to set up fleet positions on a player board.
# For each ship, a ship object containing relevant coordinates is appended to self.fleet

    def set_fleet(self):
        input(
            "Pick a coordinate between 0 and 9 for the columns and rows on your board"
        )
        input("Boats are placed form right to left.")
        for ship, size in self.ships.items():

            flag = True
            while flag:
                self.view_console()
                try:
                    print("Place your %s" % (ship))
                    row = int(input("Pick a row -----> "))
                    col = int(input("Pick a column -----> "))
                    orientation = str(
                        input(
                            "Vertical or Horizontal? (choose v or h) -----> "))

                    if orientation in ["v", "V"]:
                        if self.ocean.can_use_row(row, col, size):
                            self.ocean.set_ship_row(row, col, size)
                            boat = Ship(ship, size)
                            boat.plot_vertical(row, col)
                            self.fleet.append(boat)
                            flag = False
                        else:
                            input("Overlapping ships, try again")

                    elif orientation in ["h", "H"]:
                        if self.ocean.can_use_col(row, col, size):
                            self.ocean.set_ship_col(row, col, size)
                            boat = Ship(ship, size)
                            boat.plot_horizontal(row, col)
                            self.fleet.append(boat)
                            flag = False
                        else:
                            input("Overlapping ships, try agin")

                    else:
                        continue

                    self.view_console()
                    input()
                    os.system('clear')

                except ValueError:
                    print(
                        "Don't you remember your training?\nType a number..\n")

    # Function displays player ocean/radar in readable format

    def view_console(self):
        self.radar.view_radar()
        print("|                 |")
        self.ocean.view_ocean()

    # Function checks status of ship objects within player fleet

    def register_hit(self, row, col):
        for boat in self.fleet:
            if (row, col) in boat.coords:
                boat.coords.remove((row, col))
                if boat.check_status():
                    self.fleet.remove(boat)
                    print("%s's %s has been sunk!" %
                          (self.name, boat.ship_type))

    # Player interface for initiating in-game strikes,
    # updates the state of the boards of both players

    def strike(self, target):
        self.view_console()
        try:
            print("\n%s Pick your target..." % (self.name))
            row = int(input("Pick a row -----> "))
            col = int(input("Pick a column -----> "))

            if self.ocean.valid_row(row) and self.ocean.valid_col(col):
                if target.ocean.ocean[row][col] == "S":
                    print("DIRECT HIT!!!")
                    target.ocean.ocean[row][col] = "X"
                    target.register_hit(row, col)
                    self.radar.radar[row][col] = "X"

                else:
                    if self.radar.radar[row][col] == "O":
                        print("Area already hit....Check your radar!")
                        self.strike(target)
                    else:
                        print("Negative...")
                        self.radar.radar[row][col] = "O"

            else:
                print("Coordinates out of range...")
                self.strike(target)

        except ValueError:
            print("You need to provide a number....\n")
            self.strike(target)
        input()
        os.system('clear')