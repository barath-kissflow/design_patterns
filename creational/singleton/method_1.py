# Created by Barath M at 04/08/22


__author__ = "Barath M"


class Logger:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Logger.__instance is None:
            Logger()
        return Logger.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Logger.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Logger.__instance = self


s = Logger()
print(s)

s = Logger.get_instance()
print(s)

s = Logger.get_instance()
print(s)
