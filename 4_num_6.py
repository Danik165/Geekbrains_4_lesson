from itertools import count
from itertools import cycle

for el in count(int(input('Введите стартовое число '))):
    print(el)


my_list = [True, 'ABC', 123, None]
for i in cycle(my_list):
    print(i)
