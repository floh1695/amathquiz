#!/usr/bin/python

from random import choice, randrange

class Question:
    """
    Container for managing the individual questions.
    """

    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y}

    def __init__(self, operators=None, lower=0, upper=10, sort=True):
        self.operator = None
        if operators:
            self.operator = choice(operators)
        else:
            self.operator = choice(list(Question.operators.keys()))

        random_number = lambda: randrange(lower, upper)
        self.a = random_number()
        self.b = random_number()
        if sort:
            self.a, self.b = max(self.a, self.b), min(self.a, self.b)
        self.answer = Question.operators[self.operator](self.a, self.b)

    def __str__(self):
        return '{} {} {}'.format(self.a, self.operator, self.b)
