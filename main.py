

from pprint import pprint
cook_book = {}
with open('recipes.txt', encoding = 'utf-8') as f:
    for line in f:
        dish = line.strip()
        count = f.readline()
        recipe = []
        for ingredients in range(int(count)):
            ingredient, quantity, measure = f.readline().strip().split('|')
            recipe.append({'ingredient_name': ingredient, 'quantity': quantity, 'measure': measure})
        cook_book.setdefault(dish, recipe)
        skip = f.readline()
pprint(cook_book, sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    total = {}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                result = {}
                if ing['ingredient_name'] not in total:
                    result.setdefault(ing['ingredient_name'], {'measure': ing['measure'], 'quantity': int(ing['quantity']) * person_count })
                    total.update(result)
                else:
                    total[ing['ingredient_name']]['quantity'] = total[ing['ingredient_name']]['quantity'] + int(ing['quantity'])*person_count
        else:
            print(f'Этого блюда нет в списке:(')
    return total


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

