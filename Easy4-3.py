# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
n = int(input('Введите количество произвольных чисел: '))
m = int(input('Введите предел диапазона(по модулю): '))
list_ = [random.randint(-m, m) for _ in range(n)]
print('Ваш список произвольных чисел =', list_)

new_list_ = []
for el in list_:
    # new_list_.append(list_[el] if list_[el] % 3 == 0 and list_[el] > 0 and list_[el] % 4 != 0)
    print(list_[el])
    if ((list_[el] % 3) == 0) and (list_[el] > 0) and ((list_[el] % 4) != 0):
        new_list_.append(list_[el])

#new_list_ = [list_[el] if list_[el] % 3 == 0 and (list_[el] > 0) and (list_[_] % 4 != 0) for el in list_]

#  and (list_[_] % 2 == 0) and (list_[_] // 4 > 0)
print('Список из элементов исходного, удовлетворяющих условиям =', new_list_)
