__author__ = 'student'

import time


class automat:
    def __init__(self, start):
        """
        automat for the Conway's Game of Life
        :param start: name of txt file with the 1-st condition of the field
        """
        self.field = [None]
        with open(start) as f:
            self.n, self.m = [int(x) for x in f.readline().strip().split()]
            for i in range(self.n):
                line = f.readline().strip()
                a = [int(x) for x in line.strip().split()]
                self.field.append([[a[-1]] + a + [a[0]]])
                # self.field.append([int(x) for x in line.strip().split()])
                self.field[0] = self.field[-1]
            self.field.append(self.field[1])
        self.print_field()

        """
        n_wolfram = int(open(rule).readline().strip())
        line = bin(n_wolfram)[2:]
        line = line[::-1]
        if len(line) < 8:
            line = line + '0' * (8 - len(line))
        self.rules = [int(x) for x in line]
        # print('rules:', self.rules)
        """

    def cell_calculate(self, i, j):
        # i and j are indexes of current cell.
        # Standard rules of Conway's Game of Life.
        number_of_neighbours = (sum(self.field[i - 1][j - 1:j + 1]) + sum(self.field[i + 1][j - 1:j + 1]) +
                                self.field[i][j - 1] + self.field[i][j + 1])
        if self.field[i][j] == 1:
            if 2 <= number_of_neighbours <= 3:
                return 1
            else:
                return 0
        else:
            if number_of_neighbours == 3:
                return 1
            else:
                return 0

        # return self.rules[number_of_neighbours]

    def calculate_field(self):
        new_field = [[None for j in range(self.m + 2)] for i in range(self.n + 2)]
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                new_field[i][j] = self.cell_calculate(i, j)
        """
        new_field[-1][:] = new_field[1]
        new_field[0][:] = new_field[-2]
        """
        self.field[1:self.n + 1] = new_field[1:self.n + 1]
        self.field[-1][:] = new_field[1]
        self.field[0][:] = new_field[-2]

        # print('self:',self.field)
        # print('new: ', new_field)

    def print_field(self):
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                if self.field[i][j] == 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()

    def update(self):
        self.calculate_field()
        self.print_field()


def modelling():
    """ цикл моделирования клеточного автомата """
    field = automat('life_field_start.txt')
    for t in range(30):
        field.update()
        time.sleep(1)
    print('30 sec, program finished')

if __name__ == '__main__':
    modelling()