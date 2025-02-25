from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King"""

    def __init__(self, first_name):
        """
        Initializes the King
        """
        self.first_name = first_name
        self.family_name = "Baratheon"
        self.is_alive = True
        self.eyes = "brown"
        self.hair = "dark"

    def set_eyes(self, eyes):
        """
        Will change the eyes attribute
        """
        self.eyes = eyes

    def set_hairs(self, hairs):
        """
        Will change the hairs attribute
        """
        self.hair = hairs

    def get_eyes(self):
        """
        Will return the eyes attribute
        """
        return self.eyes

    def get_hairs(self):
        """
        Will return the hairs attribute
        """
        return self.hair
