import copy


class Node(object):
    def __init__(self, matrix, parent):
        self.matrix = matrix
        self.parent = parent
        self.movement = None
        self.zero = self.find_zero(matrix)

    def clone(self):
        new = copy.deepcopy(self)
        new.parent = self
        return new
        
    def find_zero(self, matrix):
        for i in range(3):
            for j in range(3):
                if matrix[i][j] is 0:
                    return [i, j]

    def print(self):
        print(self.matrix[0])
        print(self.matrix[1])
        print(self.matrix[2])
        print("\n")

    def move_left(self):
        new_node = self.clone()
        a, b = new_node.zero[0], new_node.zero[1]  # 0 is LINE  | 1 is COLUMN
        new_node.matrix[a][b], new_node.matrix[a][b-1] = new_node.matrix[a][b-1], new_node.matrix[a][b]
        new_node.zero[1] -= 1
        return new_node

    def move_right(self):
        new_node = self.clone()
        a, b = new_node.zero[0], new_node.zero[1]
        new_node.matrix[a][b], new_node.matrix[a][b+1] = new_node.matrix[a][b+1], new_node.matrix[a][b]
        new_node.zero[1] += 1
        return new_node

    def move_up(self):
        new_node = self.clone()
        a, b = new_node.zero[0], new_node.zero[1]
        new_node.matrix[a][b], new_node.matrix[a-1][b] = new_node.matrix[a-1][b], new_node.matrix[a][b]
        new_node.zero[0] -= 1
        return new_node

    def move_down(self):
        new_node = self.clone()
        a, b = new_node.zero[0], new_node.zero[1]
        new_node.matrix[a][b], new_node.matrix[a+1][b] = new_node.matrix[a+1][b], new_node.matrix[a][b]
        new_node.zero[0] += 1
        return new_node
