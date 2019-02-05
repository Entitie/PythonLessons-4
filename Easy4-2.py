# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
import random

or_list = ['Апельсин', 'Яблоко', 'Мандарин', 'Банан', 'Груша', 'Киви', 'Персик', 'Абрикос', 'Ананас', 'Слива']
print('Оригинальный список фруктов = ', or_list)

list1_ = [random.randint(0, 9) for _ in range(5)]
print('Первые случайные 5 чисел списка:', list1_)
list1_ = [or_list[list1_[i]] for i in range(len(list1_))]
print('Замена номеров на фрукты, первый список:', list1_)

list2_ = [random.randint(0, 9) for _ in range(5)]
print('Вторые случайные 5 чисел списка:', list2_)
list2_ = [or_list[list2_[i]] for i in range(len(list2_))]
print('Замена номеров на фрукты, второй список:', list2_)

list1_ = set(list1_)
list2_ = set(list2_)
print('Фрукты присутствующие в первом и втором списках:', list1_ & list2_)
