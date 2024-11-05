'''Задача 3. Модуль для нахождения уникальных для обоих списков
элементов
Создайте модуль с функцией, которая принимает два списка и возвращает
список, содержащий только элементы, которые уникальны для обоих списков.'''



def uniq_elem(str_1: list, str_2: list) -> list:
    set_1, set_2 = set(str_1), set(str_2)
    unique_elem = list(set_1 | set_2)
    return unique_elem


str_1 = ('a', 'b', 's', 'b')
str_2 = ('a', 'd', 's', 'r', 'b')
new_list = uniq_elem(str_1, str_2)
print(new_list)
