"""
class containing the sample example of the implementation of
S-> Single Responsibility Principle also called separation of concerns
from the (S.O.L.I.D) principles
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos - 1]

    def __str__(self):
        return "\n".join(self.entries)


j= Journal()
j.add_entry("I am happy today")
j.add_entry("I found a bug today")
print(f"Journal entries: {j}")
