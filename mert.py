import time
import sys
from textx import metamodel_from_file
tank_mm = metamodel_from_file('mert.tx')
tank_model = tank_mm.model_from_file('example1.mert')


class Tank(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.ammo = 0

    def __str__(self):
        return "Position: ({}, {}). Ammo={}".format(self.x, self.y ,self.ammo)

    def interpret(self, model):
        for c in model.commands:
            time.sleep(0.5)
            if (c.__class__.__name__ == "InitCommand"):
                self.x = c.x
                self.y = c.y
                self.ammo = c.ammo
            elif (c.__class__.__name__ == "MoveCommand"):
                dir = c.direc
                sys.stdout.write("Moving {} for {} meters.  ".format(dir, c.meters))

                move = {
                    "North": (0, 1),
                    "South": (0, -1),
                    "West": (-1, 0),
                    "East": (1, 0)
                }[dir]

                self.x += c.meters * move[0]
                self.y += c.meters * move[1]
                
                for i in range(c.meters*2):
                    time.sleep(0.3)
                    sys.stdout.write("-")
                    sys.stdout.flush()
                print()
            else:
                if(self.ammo > 0):
                    print("FIRE!!!")
                    self.ammo -= 1
                    sys.stdout.write("Waiting for cooldown.  ")
                    for i in range(5):
                        time.sleep(0.5)
                        sys.stdout.write("-")
                        sys.stdout.flush()
                    print()
                else:
                    print("Couldn't fire. No ammo left")

            print(self)


tank = Tank()
tank.interpret(tank_model)