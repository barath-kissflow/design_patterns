# Created by Barath M at 11/08/22


__author__ = "Barath M"

"""Facade pattern with an example of WashingMachine"""


class Washing:
    """Subsystem # 1"""

    def wash(self):
        print("Washing...")


class Rinsing:
    """Subsystem # 2"""

    def rinse(self):
        print("Rinsing...")


class Spinning:
    """Subsystem # 3"""

    def spin(self):
        print("Spinning...")


class WashingMachine:
    """Facade"""

    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def start_washing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()


""" main method """
if __name__ == "__main__":
    washingMachine = WashingMachine()
    washingMachine.start_washing()
