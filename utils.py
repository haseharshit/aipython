import sys


class Node:
    def __init__(self, state, parent, cost):
        self.state = state
        self.parent = parent
        self.cost = cost


class QueueF:
    def __init__(self):
        stac = []

    def insert(self, x):
        self.stac[-1] = x

    def remove(self):
        if (len(self.stac)):
            k = self.stac[0]
            self.stac = self.stac[1:]
            return k

    def isempty(self):
        return len(self.stack) == 0


class StackF(QueueF):
    def remove(self):
        if (len(self.stac)):
            k = self.stac[-1]
            self.stack = self.stack[0:-1]
            return k


class Maze:
    def __init__(self, path):
        f = open(path, 'r')
        content = f.read()
        self.walls = []
        t = content.splitlines()
        self.l = len(t)
        self.w = 0
        for x in t:
            self.w = len(x) if self.w < len(x) else self.w

        for i in range(self.l):
            row = []
            for j in range(self.w):
                try:
                    val = t[i][j]
                    if (val == 'A'):
                        self.start = (i, j)
                        row.append(False)
                    if (val == 'B'):
                        self.end = (i, j)
                        row.append(False)
                    elif (val == ' '):
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(True)
            self.walls.append(row)
        # at the end of this, we have l, w, walls, start, end

    def solve(self):
        ft = StackF()
        start = Node(self.start, None, 0)
        ft.insert(start)
        while (not ft.isempty()):
            node = ft.remove()


if len(sys.argv) != 2:
    sys.exit("Path is expected")
m = Maze(sys.argv[1])
