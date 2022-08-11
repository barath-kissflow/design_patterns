# Created by Barath M at 11/08/22
# src : https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_template.htm

from abc import ABC, abstractmethod


class MakeMeal(ABC):

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def slice(self):
        pass

    def go(self):
        self.prepare()
        self.cook()
        self.slice()
        self.eat()


class MakePizza(MakeMeal):
    def prepare(self):
        print("Prepare Pizza")

    def cook(self):
        print("Cook Pizza")

    def eat(self):
        print("Eat Pizza")

    def slice(self):
        print("Slice Pizza")


class MakeTea(MakeMeal):
    def prepare(self):
        print("Prepare Tea")

    def cook(self):
        print("Cook Tea")

    def eat(self):
        print("Eat Tea")


if __name__ == "__main__":
    make_meal = MakePizza()
    make_meal.go()
    print(25 * "+")
    make_meal = MakeTea()
    make_meal.go()
