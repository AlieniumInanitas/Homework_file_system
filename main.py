class CookBook:
    '''
    cook
    '''
    def __init__ (self):
        self.cook_book = {}
    
    def load_recipe (self, file_name:str): 
        '''
        blat'
        '''
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
                self.cook_book.setdefault(recipe[0].strip(), [])
                for ingredient in recipe[-int(recipe[1]):]:
                    item = {}
                    splitted_ingr = ingredient.split('|')
                    item['ingredient_name'] = splitted_ingr[0].strip()
                    item['quantity'] = splitted_ingr[1].strip()
                    item['measure'] = splitted_ingr[2].strip()
                    self.cook_book[recipe[0].strip()].append(item)

        print(self.cook_book)


recipte_one = CookBook()
recipte_one.load_recipe('recipes.txt')