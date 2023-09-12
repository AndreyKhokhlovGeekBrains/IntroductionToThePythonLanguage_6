# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def get_arithmetic_progression_array(start: int, step: int, elements_num: int) -> list[int]:
    my_array = [start + i * step for i in range(elements_num)]
    return my_array
a = int(input('Введите значение первого члена арифметической прогрессии: '))
d = int(input('Введите значение шага: '))
n = int(input('Введите необходимое количество элементов прогрессии: '))
print(f'Массив элементов арифметической прогрессии: {get_arithmetic_progression_array(a, d, n)}')
