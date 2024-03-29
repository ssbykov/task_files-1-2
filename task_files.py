# https://github.com/netology-code/py-homeworks-basic/tree/master/7.files
"""Здравствуйте. Когда вы открыли файл на чтение, вам нужно подумать как в цикле,
 считывая построчно информацию из файла, последовательно получать данные по каждому блюду,
 добавлять эти данные в список словарей заданной конфигурации.
 В цикле вы в первой строке получаете названия блюда и сохраняете в переменную.
 Во второй строке вы получаете количество ингредиентов, которое тоже сохраняете в переменную.
 Далее идет еще один вложенный цикл в котором вы уже перебираете ингредиенты.
 Количество итераций в этом цикле вы получаете из переменной с количеством ингредиентов.
 Перебирая ингредиенты вы через сплит по символу " | " получаете название ингредиента, количество и единицы измерения.
 Из этих данных вы формируете словарик, который тут же добавляете в список словарей."""

# https://github.com/netology-code/py-homeworks-basic/tree/master/7.files

from pathlib import Path


def cook_book():
    file_path = str(Path(__file__).parent.absolute()) + '/recipes.txt'
    with open(file_path, encoding='utf-8') as recipes:
        cook_book_dict = {}
        for line in recipes:
            dish = line.strip()
            ingredients_count = int(recipes.readline())
            for i in range(ingredients_count):
                ingredients = recipes.readline().split(" | ")
                ingredient = {
                    'ingredient_name': ingredients[0].strip(),
                    'quantity': int(ingredients[1].strip()),
                    'measure': ingredients[2].strip()
                }
                cook_book_dict.setdefault(dish, []).append(ingredient)
            recipes.readline()
    return cook_book_dict

"""
В этом задании вам нужно пройти циклом по входящему списку блюд. На каждой итерации в цикле вы будете получать
название очередного блюда. По названию этого блюда вам нужно из словаря сформированного в предыдущем задании
получить рецепт (список словарей с ингредиентами). Далее вторым вложенным циклом нужно пройти по этому списку
ингредиентов. Получая в цикле словарь по каждому ингредиенту, в новый словарь, структура которого задана в условии,
необходимо добавлять элементы с ключами, соответствующие названию ингредиента и значением являющимися словарями,
содержащими информацию по единицам измерения и количеству. При этом количество нужно рассчитывать умножая 
количество ингредиента из рецепта на количество персон. Так же при добавлении очередного ингредиента в итоговый словарь
нужно делать проверку, есть ли уже этот ингредиент в словаре. Если есть то просто нужно к имеющейся записи добавлять
рассчитанное количество ингредиента.  
"""

def get_shop_list_by_dishes(dishes, person_count):
    dict_cook_book = cook_book()
    # Решение по задаче №1 - выводим кулинарную книгу в виде словаря
    print(dict_cook_book)
    dict_get_shop = {}
    for dish in dishes:
        for ingredient in dict_cook_book[dish]:
            key = ingredient['ingredient_name']
            ingredient_amount = ingredient['quantity'] * person_count
            if dict_get_shop.get(key):
                dict_get_shop[key]['quantity'] += ingredient_amount
            else:
                dict_get_shop[key] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient_amount
                }

    print(dict_get_shop)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)

# еще одно решение
with open('recipes.txt', encoding='utf-8') as recipes:
    cook_book = {}

    while True:
        try:
            cook_book.setdefault(recipes.readline().strip(), [
                {'ingredient_name': stat[0].strip(), 'quantity': int(stat[1].strip()), 'measure': stat[2].strip()}
                for stat in [recipes.readline().split(' | ') for _ in range(int(recipes.readline()))]])
            recipes.readline()
        except:
            break
print(cook_book)
