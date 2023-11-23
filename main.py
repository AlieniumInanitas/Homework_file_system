class CookBook:
    """Наполнить словарь данными из переданного файла"""
    def __init__ (self):
        self.cook_book = {}
    
    def load_recipe (self, file_name:str):
        is_end_of_file = False
        with open(file_name, encoding= 'utf-8') as f:
            while is_end_of_file == False:
                count = 0
                recipe = []
                while count == 0:
                    line = f.readline()
                    if line == '\n':
                        count += 1
                    elif line == '':
                        is_end_of_file = True
                        break
                    else:
                        recipe.append(line)
                self.__add_recipe(recipe)

    def __add_recipe(self, recipe:list):
        self.cook_book.setdefault(recipe[0].strip(), [])
        for ingredient in recipe[-int(recipe[1]):]:
            item = {}
            splitted_ingr = ingredient.split('|')
            item['ingredient_name'] = splitted_ingr[0].strip()
            item['quantity'] = splitted_ingr[1].strip()
            item['measure'] = splitted_ingr[2].strip()
            self.cook_book[recipe[0].strip()].append(item)


class IngredientCounter:
    """Рассчитать количество ингридиентов на указанное количество персон"""
    def __init__(self, reciptes:CookBook):
        self.list_by_dishes = {}
        self.cook_book = reciptes.cook_book

    def get_shop_list_by_dishes(self, dishes:list, person_count:int):
        """ """
        for dish in dishes:
            if dish in self.cook_book:
               self.__add_ingredient_dictionary(dish, person_count)
        return self.list_by_dishes           

    def __add_ingredient_dictionary(self, dish, person_count):
        for ingredient in self.cook_book[dish]:
            quantities = {}
            if ingredient['ingredient_name'] not in self.list_by_dishes:
                quantities['quantity'] = int(ingredient['quantity']) * person_count
                quantities['measure'] = ingredient['measure']
                self.list_by_dishes.setdefault(ingredient['ingredient_name'], quantities)
            else:   
                self.list_by_dishes[ingredient['ingredient_name']]['quantity'] += (int(ingredient['quantity']) * person_count)


reciptes = CookBook()
reciptes.load_recipe('recipes.txt')
recipte_two = IngredientCounter(reciptes)
recipte_two.get_shop_list_by_dishes(['Омлет', 'Фахитос'], 6)
