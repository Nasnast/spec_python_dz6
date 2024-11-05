"""Задача 2. Модуль для удаления дублирующихся подряд символов
Напишите модуль с функцией, которая принимает строку и возвращает строку с
удаленными дублирующимися подряд идущими символами. Например, строка
"aabbccaa" должна быть преобразована в "abca"""


def dubl_char(str: list) -> list:

    if len(str) == 0:
        return str

    new_list = str[0]
    for char in str[1:]:
        if char != new_list[-1]:
            new_list += char
    return new_list


if __name__ == "__main__":
    str = "aaabbbccaad"
    print(dubl_char(str))
