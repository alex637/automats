__author__ = 'student'


def cell_calculate(left, current, right):
    return left^right


def calculate_field(tape):
    """tape -- список из N ноликов или единичек"""
    n = len(tape)
    new_tape = [0] * (n + 2)
    for i in range(1, n + 1):
        new_tape[i] = cell_calculate(tape[i - 1], tape[i], tape[i + 1])
    new_tape[n + 1] = new_tape[1]
    new_tape[0] = new_tape[-2]
    return new_tape


def generate_field():
    tape = []
    with open("cellular_tape.txt") as f:
        line = f.readline().strip()
        # n = len(line)
        tape.append(int(line[-1]))
        tape.extend(list(map(int, line)))
        tape.append(int(line[1]))
    return tape


def print_field(field):
    for cell in field:
        print('★' if cell else ' ' , end = '')
    print()


def modelling():
    """ цикл моделирования клеточного автомата """
    field = generate_field()
    print_field(field)
    for t in range(15):
        field = calculate_field(field)
        print_field(field)

if __name__ == '__main__':
    modelling()
