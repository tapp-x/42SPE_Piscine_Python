import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15 characters long string"""
    return ''.join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Student class representing a student with the following attributes:
    - name: str
    - surname: str
    - login: str
    - id: str
    - Active: bool

    Method:

    """
    name: str = field(init=True)
    surname: str = field(init=True)
    login: str = field(init=False)
    id: str = field(init=False)
    active: bool = field(default=True)

    def __post_init__(self):
        self.login = f"{self.name[0]}{self.surname.lower()}"
        self.id = generate_id()
