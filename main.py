def max_number(a, b):
    if a > b or a == b:
        return a
    else:
        return b

def empty_function():
    pass

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

def test_max_number():
    assert max_number(1, 2) == 2, 'Ошибка: 2 > 1'
    assert max_number(-1, -2) == -1, 'Ошибка: -1 > -2'
    assert max_number(22, 22) == 22, 'Ошибка: числа равны'

try:
    print('Максимальное число', max_number(int(input('Первое число: ')), int(input('Второе число: '))))
except ValueError:
    print('Некорректный ввод данных')

for num in even_numbers(30):
    print(num, end=' ')

test_max_number()
print('\nТест пройден без ошибок')
