def cookbook_read():
  cook_book = {}
  with open('recipes.txt') as file:
    for line in file:
            key = line.strip()
            ingredients_count = file.readline().strip()
            ingredients = []
            for i in range(int(ingredients_count)):
                value = file.readline().strip()
                ingr = value.split(' | ')
                ingredients.append({'ingredient_name': ingr[0],
                'quantity': int(ingr[1]), 'measure': ingr[2]})
            file.readline()
            cook_book[key] = ingredients
    return cook_book

#print('\n', 'Задание_1:', '\n', '\n', cookbook_read(), '\n', sep = '')

def get_shop_list_by_dishes(cook_book, person_count):
  dishes = list(cook_book.keys())
  ingredients_dict = {}
  for dish in dishes:
    if dish in cook_book:
      for ingr in cook_book[dish]:
        if ingr['ingredient_name'] not in ingredients_dict.keys():
          ingredients_dict[ingr['ingredient_name']] = {'measure': ingr['measure'],'quantity': ingr['quantity'] * person_count}
        else:
          ingredients_dict[ingr['ingredient_name']]['quantity'] += ingr['quantity'] * person_count
  return ingredients_dict

print(f"Задание_2:\n\n {get_shop_list_by_dishes(cookbook_read(), int(input('Введите кол-во персон: ')))}", sep='')
