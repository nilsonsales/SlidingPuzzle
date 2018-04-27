"""
Search Tree with 3x3 Sliding Puzzle
@author: nilsonsales
"""

from Node import Node

frontier = []
i = 0


def isFinal(combination):
    if (combination == [[1,2,3],
                        [4,5,6],
                        [7,8,0]]):
        print("FINAL STATE")
        return True


def search(game):  # widthFirstSearch
    global frontier
    global i
    i += 1

    print("iterations = %d" % i)
    print("frontier size = %d" % len(frontier))

    # verifies if the matrix is the final state desired
    if isFinal(game.matrix):
        while game.parent is not None:  # prints the reverse game
            game.print()
            game = game.parent
        return game

    else:
        if frontier:  # if the frontier is not null, removes the 1st element and generates children
            frontier.pop(0)

        # finds where the zero (blank piece) is and adds children to the frontier
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

        search(frontier[0])  # calls the function again with the new frontier


# pieces = [[2,4,3],
#           [1,0,6],
#           [7,5,8]]

pieces = [[],
          [],
          []]

print("Enter a valid initial combination")
pieces[0] = input('1st line: ')
pieces[1] = input('2nd line: ')
pieces[2] = input('3rd line: ')


for line in range(3):
    pieces[line] = pieces[line].split(",")
    pieces[line] = list(map(int, pieces[line]))

puzzle = Node(pieces, None)  # (matrix, parent)

print("INITIAL STATE")
puzzle.print()

search(puzzle)
