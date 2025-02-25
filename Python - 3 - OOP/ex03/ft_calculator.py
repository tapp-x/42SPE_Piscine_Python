class calculator:
    """
    calculator class that can perform basic operations
    on vector of scalars.
    """
    def __init__(self, vector) -> None:
        """
        Constructor to initialize the vector
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Overloading the + operator to perform addition
        """
        for i in range(len(self.vector)):
            self.vector[i] += object
        print(self.vector)

    def __mul__(self, object) -> None:
        """
        Overloading the * operator to perform multiplication
        """
        for i in range(len(self.vector)):
            self.vector[i] *= object
        print(self.vector)

    def __sub__(self, object) -> None:
        """
        Overloading the - operator to perform subtraction
        """
        for i in range(len(self.vector)):
            self.vector[i] -= object
        print(self.vector)

    def __truediv__(self, object) -> None:
        """
        Overloading the / operator to perform division
        """
        if object == 0:
            print("Division by zero is not allowed")
            return
        for i in range(len(self.vector)):
            self.vector[i] /= object
        print(self.vector)
