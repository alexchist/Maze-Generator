import generate
import curses


class Person:
    def __init__(self, maze):
        self.field = maze

    def close_term(self, stdscr):
        for i in range(self.field.n * 2 + 2):
            for j in range(self.field.m * 2 + 2):
                stdscr.addch(i, j, ' ')
        curses.echo()
        curses.nocbreak()
        curses.curs_set(True)
        curses.endwin()

    def play(self):
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(False)
        self.field.init_player((1, 1))
        stdscr.addstr(0, 0, "write q for quit and wasd for move")
        while True:
            self.field.print_on_terminal(stdscr)
            move = stdscr.getch()
            stdscr.addstr(1, 1, str(move))
            if move == 113:
                self.field.del_player()
                self.close_term(stdscr)
                return False
            if move == 119:
                self.field.get_move(self.field.Orient.UP)
            elif move == 100:
                self.field.get_move(self.field.Orient.RIGHT)
            elif move == 115:
                self.field.get_move(self.field.Orient.DOWN)
            elif move == 97:
                self.field.get_move(self.field.Orient.LEFT)
            if self.field.coord_player == (self.field.n * 2 - 1, self.field.m * 2 - 1):
                self.close_term(stdscr)
                return True


class Game:
    def __init__(self):
        self.Maze_gen = generate.GenerateMaze()
        self.field = self.Maze_gen.generate_maze()
        while True:
            print(
                "Введите P, если хотети пройти лабиринт, S, если хотите сохранить лабиринт G, если хотите сгенерировать новый лабиринт, V, чтобы посмотреть на лабиринт и любой символ, чтобы выйти")
            move = input()
            if move == 'P':
                self.game = Person(self.field)
                self.game.play()
            elif move == 'S':
                self.field.save_field()
            elif move == 'G':
                self.field = self.Maze_gen.generate_maze()
            elif move == 'V':
                self.field.print()
            else:
                return


