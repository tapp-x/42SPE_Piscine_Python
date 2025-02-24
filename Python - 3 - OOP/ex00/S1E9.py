from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class that can take a first_name as first parameter,
    is_alive as second non mandatory parameter set
    to True by default and can change the health state
    of the character with a method
    """

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Constructor of the class
        """
        pass

    @abstractmethod
    def die(self):
        """
        Method that changes the health state of the character to False
        """
        pass


class Stark(Character):
    """
    Class that inherits from Character
    """
    def __init__(self, first_name=None, is_alive=True):
        """
        Constructor of the class
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Method that changes the health state of the character to False
        """
        self.is_alive = False
