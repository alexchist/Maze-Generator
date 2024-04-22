import random
from enum import Enum


class DSU:
    def __init__(self, n):
        self.list_vert = [i for i in range(n)]

    def get_parent(self, u):
        if u == self.list_vert[u]:
            return u
        self.list_vert[u] = self.get_parent(self.list_vert[u])
        return self.list_vert[u]

    def union(self, u, v):
        u = self.get_parent(u)
        v = self.get_parent(v)
        if u == v:
            return False
        self.list_vert[u] = v
        return True


class Field:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.edges = []
        self.coord_player = (-1, -1)

    def get_num(self, coords):
        return coords[0] * self.m + coords[1]

    def delete_wall(self, first_coord, second_coord):
        self.edges.append((first_coord, second_coord))
        return

    def get_field(self):
        field = [['#' for _ in range(self.n * 2 + 1)] for _ in range(self.m * 2 + 1)]
        for i in range(1, 2 * self.n + 1, 2):
            for j in range(1, 2 * self.m + 1, 2):
                field[i][j] = ' '
        for edge in self.edges:
            x = (edge[0][0] + edge[1][0]) + 1
            y = (edge[0][1] + edge[1][1]) + 1
            field[x][y] = ' '
        if self.coord_player != (-1, -1):
            field[self.coord_player[0]][self.coord_player[1]] = 'P'
        return field

    def print(self):
        field = self.get_field()
        for i in range(self.n * 2 + 1):
            print(*field[i], sep='')

    def print_on_terminal(self, stdscr):
        field = self.get_field()
        for i in range(self.n * 2 + 1):
            for j in range(self.m * 2 + 1):
                stdscr.addch(i + 1, j + 1, field[i][j])

    def init_player(self, coord):
        self.coord_player = coord

    def del_player(self):
        self.coord_player = (-1, -1)

    class Orient(Enum):
        UP = 1
        RIGHT = 2
        DOWN = 3
        LEFT = 4

    def get_move(self, orient):
        new_coord = self.coord_player
        if orient == self.Orient.UP:
            new_coord = (new_coord[0] - 1, new_coord[1])
        elif orient == self.Orient.DOWN:
            new_coord = (new_coord[0] + 1, new_coord[1])
        elif orient == self.Orient.RIGHT:
            new_coord = (new_coord[0], new_coord[1] + 1)
        elif orient == self.Orient.LEFT:
            new_coord = (new_coord[0], new_coord[1] - 1)
        if self.get_field()[new_coord[0]][new_coord[1]] != '#':
            if orient == self.Orient.UP:
                new_coord = (new_coord[0] - 1, new_coord[1])
            elif orient == self.Orient.DOWN:
                new_coord = (new_coord[0] + 1, new_coord[1])
            elif orient == self.Orient.RIGHT:
                new_coord = (new_coord[0], new_coord[1] + 1)
            elif orient == self.Orient.LEFT:
                new_coord = (new_coord[0], new_coord[1] - 1)
            self.coord_player = new_coord

    def save_field(self):
        print("Введите название файла")
        name = input()
        f = open(name, 'w')  # открытие в режиме записи
        text = ""
        for i in self.get_field():
            for j in i:
                text += j
            text += '\n'
        f.write(text)
        f.close()  # закрытие файла


class GenerateMaze:
    def __init__(self):
        self.n = 1
        self.m = 1
        self.field = Field(1, 1)

    def check_coord(self, coord):
        return 0 <= coord[0] < self.n and 0 <= coord[1] < self.m

    def dfs(self, x, y, used):
        used[x][y] = True
        dxdy = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        random.shuffle(dxdy)
        for coord in dxdy:
            # print(coord, self.check_coord(coord))
            if self.check_coord(coord) and not used[coord[0]][coord[1]]:
                self.field.delete_wall((x, y), coord)
                self.dfs(coord[0], coord[1], used)

    def generate_dfs(self):
        used = [[False] * self.m for _ in range(self.n)]
        self.dfs(0, 0, used)
        return self.field

    def generate_dsu(self):
        dsu = DSU(self.n * self.m)
        graph = []
        for i in range(self.n):
            for j in range(self.m):
                if i > 0:
                    graph.append(((i - 1, j), (i, j)))
                if j > 0:
                    graph.append(((i, j - 1), (i, j)))
        random.shuffle(graph)
        for edge in graph:
            if dsu.union(self.field.get_num(edge[0]), self.field.get_num(edge[1])):
                self.field.delete_wall(edge[0], edge[1])
        return self.field

    def generate_maze(self):
        print("Введите длину выбранного поля: ", end='')
        self.n = 1
        while True:
            try:
                self.n = int(input())
                break
            except Exception:
                print()
                print("Введите длину выбранного поля: ", end='')
        print("Введите ширину выбранного поля: ", end='')
        self.m = 1
        while True:
            try:
                self.m = int(input())
                break
            except Exception:
                print()
                print("Введите ширину выбранного поля: ", end='')
        self.field = Field(self.n, self.m)
        print(
            "Выберите способ генерации. Введите 1 для генерации с помощью остовного дерева, 2 для DFS, 3 для алгоритма Эллера (не работает)")
        num = int(input())
        if num == 1:
            return self.generate_dsu()
        elif num == 2:
            return self.generate_dfs()
        elif num == 3:
            pass  # TODO
