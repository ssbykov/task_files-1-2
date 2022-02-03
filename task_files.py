from pathlib import Path

def cook_book (recipes_list):
    cook_book ={}
    n_str = 0
    while n_str < len(recipes_list):
        name_dish = recipes_list[n_str].strip()
        start_list = n_str + 2
        end_list = start_list + int(recipes_list[n_str + 1])
        cook_book[name_dish] = dish_recipe(recipes_list[start_list:end_list])
        n_str = end_list + 1
    return cook_book
    
def dish_recipe(ingridientes):
    list_ingridiente = []
    for ingridiente in ingridientes:
        list_ingridiente.append(dict(zip(['ingredient_name', 'quantity', 'measure'], ingridiente.strip().split(' | '))))
        list_ingridiente[-1]['quantity'] = int(list_ingridiente[-1]['quantity'])
    return list_ingridiente

def get_shop_list_by_dishes(dishes, person_count):
    file_path = str(Path(__file__).parent.absolute()) + '/recipes.txt'
    with open(file_path, 'r', encoding='UTF-8') as recipes:
        recipes_list = recipes.readlines()
    dict_cook_book = cook_book(recipes_list)
# Решение по задаче №1 - выводим кулинарную книгу в виде словаря
    print(dict_cook_book)
    dict_get_shop = {}
    for dish in dishes:
        for  ingridiente in dict_cook_book[dish]:
            if ingridiente['ingredient_name'] in dict_get_shop:
                dict_get_shop[ingridiente['ingredient_name']]['quantity'] += ingridiente['quantity'] * person_count
            else:
                dict_get_shop[ingridiente['ingredient_name']] = {'measure': ingridiente['measure'], 'quantity': ingridiente['quantity'] * person_count}
    print(dict_get_shop)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)   