my_list = [2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_cool_list = [i for num, i in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Стырый: {my_list}, новый: {my_cool_list}')