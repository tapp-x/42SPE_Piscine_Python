from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""

    def __init__(self, first_name):
        """
        Initializes the Baratheon family
        """
        self.first_name = first_name
        self.family_name = "Baratheon"
        self.is_alive = True
        self.eyes = "brown"
        self.hair = "dark"

    def die(self):
        """
        Will change the is_alive attribute to False
        """
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family"""

    def __init__(self, first_name):
        """Initializes the Lannister family"""
        self.first_name = first_name
        self.family_name = "Lannister"
        self.is_alive = True
        self.eyes = "blue"
        self.hair = "light"

    def die(self):
        """
        Will change the is_alive attribute to False
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """
        Factory method to create a Lannister
        """
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance
