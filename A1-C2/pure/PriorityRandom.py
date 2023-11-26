from itertools import repeat
from random import shuffle, choice
from pprint import pprint


class PriorityRandom:
    """
    items = [
        (item1, 2), (item2, 1), (item3, 8), (item4, 2), ...
    ]
    """
    
    def __init__(self, items):
        self.items = items
        self.the_list = self.make_the_list(items)
    
    @classmethod
    def make_the_list(cls, items):
        the_list = []
        for index, item in enumerate(items):
            the_list.extend(
                list(
                    repeat(index, item[1]) # item[1] == Priority
                )
            )
        shuffle(the_list)
        return the_list
    
    def choice(self):
        index = choice(self.the_list)
        return self.items[index][0]
    
    def choices(self, n):
        return list(
            item() for item in repeat(self.choice, n)
        )


class PR(PriorityRandom):
    pass


# EXAMPLE
"""
items = [
    ('item1', 1),
    ('item2', 3),
    ('item3', 5),
    ('item4', 10),
    ('item5', 15),
]

pr = PriorityRandom(items)

pprint(pr.choices(10))
"""
