def salar():
    try:
        time = float(input('Выработка в часах: '))
        salary = int(input('Ставка: '))
        bonus = int(input('Премия: '))
        res = int(time * salary + bonus)
        print(f'заработная плата сотрудника:  {res} монет(ы)')

    except ValueError:
        return print('Not a number')
salar()
