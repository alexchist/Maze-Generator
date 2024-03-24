# Maze-Generator

## Возможности
Возможность генерировать лабиринты с помощью DFS, поиска остовного дерева и [алгоритма Эллера](https://habr.com/ru/articles/667576/). Возможность сохранять сгенерированный лабиринт в .txt файл. Возможность загружать лабиринт из .txt файл (с проверкой корректности) и проходить его. Возможность решать лабиринт

## Немного об архитектуре

class DSU // СНМ для генерации с помощью остовного дерева
void init(int n) // инициализировать размером n
int get_parent(int u) // служебная функция
bool unite(int u, int v) // 0 - лежали в одной компоненте, 1 - лежали в разных

class Adapter // Для вывода/ввода на консоль/куда угодно

char get_char()

void put_char()


class Field // для обработки поля (хз, надо ли, но, мне кажется, там будет удобнее, понятее + легче доделывать новые форматы)

int get_num(tuple(int, int)) // вернёт номер клетки по координатам

void init(int n, int m) // инициализировать лабиринт n*m

void delete_wall(tuple(int, int) first_coord, tuple(int, int) second_coord)

void print() // отобразить вывести лабиринт

void save(srtring file_name) // сохранить

void init_person(tuple(int, int) coord) // поставить игрока

void get_move(enum orient) // сделать ход игроком

void remote_person() // удалить игрока


class Generate_maze

Field generate_dsu(int n, int m) // сгененирировать с помощью остовного дерева

Field generate_dfs(int n, int m) // сгененирировать с помощью dfs

void dfs(tuple(int, int)pos, [[bool]]used) // служебная функция

Field generate_eller(int n, int m_ // сгенерировать с помощью Эллера

Field generate_maze() // спросит у пользователя способ генерации и размер

class Person // для прохождения лабиринта

void init(Field maze)

bool play() // внутри while(True) пока игрок играет. Возвращает 1 - человек выиграл, 0 - сдался

class Game 
bool load_maze(string filename) // считать из файла + проверить на корректность 1 - получилось, 0 - ошибка
void do_game() // обработка ввода пользователя. Сначала надо как-то задать лабиринт (из файла или сгенерировать, потом играть или показать решение)

