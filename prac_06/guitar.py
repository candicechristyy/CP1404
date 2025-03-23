"""
CP1404/CP5632 Practical
Guitar Class
"""
CURRENT_YEAR = 2025
VINTAGE_AGE = 50
class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE


    def __str__(self):
        """Return string of Guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"