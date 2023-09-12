# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

def get_random_array(size: int) -> list[int]:
	my_array = [random.randint(0, 20) for _ in range(size)]
	return my_array
def get_elements_indexes(start: int, end: int, input_list: list[int]) -> list[int]:
	my_list = []
	for index in range(len(input_list)):
		if start <= input_list[index] <= end:
			my_list.append(index)
	return my_list

n = int(input('Введите необходимое количество элементов для массива: '))
start = int(input('Введите значение начала диапазона: '))
end = int(input('Введите значение конца диапазона: '))
my_array = get_random_array(n)
print(f'Созданный массив: {my_array}')
print(f'Индексы элементов, значения которых принадлежат заданному диапазону: {get_elements_indexes(start, end, my_array)}')
