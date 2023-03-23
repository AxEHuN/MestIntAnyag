import random

from problem import *

def breadth_first_tree_search(problem):
    pass

class Digits(Problem):

    def __init__(self):
        self.wrong_numbers = [(6,6,6),(6,6,7)]
        self.s4 = 0

        # Complete the implementation of initial function by calling
        # the parent constructor and initialize the initial state and set of goal states
        # Write your code below this line!

        # Write your code above this line! Delete the 'pass' keyword!

    def actions(self, state):
        s1, s2, s3 = state
        acts = []

        # Complete the remaining part of the action function
        # Write your code below this line!

        # Write your code above this line!
        return acts

    def result(self, state, action):
        s1, s2, s3 = state
        # Complete the implementation of result function
        # Write your code below this line!

        # Write your code above this line!


if __name__ == '__main__':
    pass