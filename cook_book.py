# Домашнее задание к лекции 2.1 «Открытие и чтение файла, запись в файл»
# Необходимо написать программу для кулинарной книги.
#
# Список рецептов должен храниться в отдельном файле в следующем формате:
#
# Название блюда
# Kоличество ингредиентов в блюде
# Название ингредиента | Количество | Единица измерения
# Название ингредиента | Количество | Единица измерения
# ...

# В одном файле может быть произвольное количество блюд.
# Читать список рецептов из этого файла.
# Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.

# Задача №1
# Должен получится следующий словарь
#
# cook_book = {
#   'Омлет': [
#     {'ingridient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingridient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingridient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingridient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingridient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingridient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingridient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
#     {'ingridient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }


def load_book_from_file(book_file='recipes.txt'):
    # Читаем и преобразуем данные в заданный словарь из файла
    with open(book_file) as book:
        cook_dict = dict()
        key_ingridient_dict = ['ingridient_name', 'quantity', 'measure']

        book.seek(0, 2)  # Определяем конец файла и возвращаем указатель в начало файла
        eof = book.tell()
        book.seek(0, 0)

        while book.tell() != eof:  # Проверяем конец файла
            ingridient_list = []
            key = book.readline().strip() # Наименование блюда

            for ingridient in range(int(book.readline().strip())):
                value_ingridient_dict = book.readline().strip().split(' | ')
                value_ingridient_dict[1] = int(value_ingridient_dict[1])
                ingridient_list.append(dict(zip(key_ingridient_dict, value_ingridient_dict)))
            cook_dict.setdefault(key, ingridient_list)
            book.readline()

    return cook_dict


