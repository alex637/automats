__author__ = 'student'

f = open('life_field_start.txt', 'w')
a = [0] * 10
print(10, 10, file=f)
for i in range(10):
    print(*a, file=f)