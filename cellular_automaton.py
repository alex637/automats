__author__ = 'student'


class automat:
    def __init__(self, start,rule):
        """
        :param start: name of txt file with the 1-st condition of the field
        :param rule: name of txt file with the Wolfram code
        :return:
        """
        self.field = [None]
        with open(start) as f:
            line = f.readline().strip()
            self.n = len(line)
            self.field.extend([int(x) for x in line])
            self.field[0] = self.field[-1]
            self.field.append(self.field[1])
        self.print_field()
        n_wolfram = int(open(rule).readline().strip())
        line = bin(n_wolfram)[2:]
        line = line[::-1]
        if len(line) < 8:
            line = line + '0' * (8 - len(line))
        self.rules = [int(x) for x in line]
        # print('rules:', self.rules)
                    
    def cell_calculate(self, left, current, right):
        return self.rules[int(str(left) + str(current) + str(right), base=2)]

    def calculate_field(self):
        new_field = [0] * (self.n + 2)
        for i in range(1, self.n + 1):
            new_field[i] = self.cell_calculate(self.field[i - 1], self.field[i], self.field[i + 1])
        new_field[-1] = new_field[1]
        new_field[0] = new_field[-2]

        self.field[:] = new_field
        # print('self:',self.field)
        # print('new: ', new_field)

    def print_field(self):
        for x in self.field[1:self.n + 1]:
            if x == 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

    def update(self):
        self.calculate_field()
        self.print_field()


def modelling():
    """ цикл моделирования клеточного автомата """
    field = automat('start_wolfram_code.txt', 'rules_wolfram_code.txt')
    for t in range(50):
        field.update()

if __name__ == '__main__':
    modelling()
