"""
CP1404/CP5632 Practical
Programming Language Class
"""

class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name="", typing="", reflection=True, year=0):
        """Initialise a ProgrammingLanguage instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if typing is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string of ProgrammingLanguage object"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"