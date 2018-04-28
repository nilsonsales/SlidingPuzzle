"""
Search Tree with 3x3 Sliding Puzzle
@author: nilsonsales
"""

from Node import Node

import sys
sys.setrecursionlimit(10000)

frontier = []
i = 0
stepBstep = []
puzzle = None
hasChildren = []


default = [[1,2,3],
           [4,5,6],
           [7,8,0]]

default2 = [[1,8,2],
            [0,4,3],
            [7,6,5]]

default3 = [[3,5,2],
            [0,7,6],
            [4,1,2]]


def isFinal(combination):
    if (combination == default):
        print("\nSOLUTION:")
        return True


def search(game):  # widthFirstSearch
    global frontier
    global i
    global stepBstep
    global puzzle
    i += 1

    print("iterations: %d" % i)
    print("frontier size: %d" % len(frontier))
    print("hasChildren: %d" % len(hasChildren))

    # verifies if the matrix is the final state desired
    if isFinal(game.matrix):
        while game.parent is not None:  # prints the game step-by-step
            stepBstep.append(game)
            game = game.parent

        #  adds the original combination and reverses the list
        stepBstep.append(puzzle)
        stepBstep.reverse()

        for element in range(len(stepBstep)):
            stepBstep[element].print()
        return game


    else:
        if frontier:  # if the frontier is not null, removes the 1st element
            frontier.pop(0)

        # sees if the combination has already generated children
        if game.matrix in hasChildren:
            search(frontier[0])

        else:
            # finds where the zero (blank piece) is and adds its children to the frontier
            if game.zero == [1, 1]:
                frontier.append(game.move_left())
                frontier.append(game.move_right())
                frontier.append(game.move_up())
                frontier.append(game.move_down())
            elif game.zero == [0, 0]:
                frontier.append(game.move_right())
                frontier.append(game.move_down())
            elif game.zero == [0, 2]:
                frontier.append(game.move_left())
                frontier.append(game.move_down())
            elif game.zero == [2, 0]:
                frontier.append(game.move_right())
                frontier.append(game.move_up())
            elif game.zero == [2, 2]:
                frontier.append(game.move_left())
                frontier.append(game.move_up())
            elif game.zero == [0, 1]:
                frontier.append(game.move_right())
                frontier.append(game.move_left())
                frontier.append(game.move_down())
            elif game.zero == [1, 0]:
                frontier.append(game.move_right())
                frontier.append(game.move_up())
                frontier.append(game.move_down())
            elif game.zero == [1, 2]:
                frontier.append(game.move_left())
                frontier.append(game.move_up())
                frontier.append(game.move_down())
            elif game.zero == [2, 1]:
                frontier.append(game.move_right())
                frontier.append(game.move_left())
                frontier.append(game.move_up())

            if game not in hasChildren:
                hasChildren.append(game.matrix)

            search(frontier[0])  # calls the function again with the new frontier


# pieces = [[1,8,2],
#           [0,4,3],
#           [7,6,5]]

pieces = [[],
          [],
          []]

print("Enter a valid initial combination separated by space")
pieces[0] = input('1st line: ')
pieces[1] = input('2nd line: ')
pieces[2] = input('3rd line: ')
print("\n")

# Splits the string entered by comma and maps each element to int
for line in range(3):
    pieces[line] = pieces[line].split(" ")
    pieces[line] = list(map(int, pieces[line]))


puzzle = Node(pieces, None)  # (matrix, parent)

print("INITIAL STATE")
puzzle.print()

search(puzzle)
