# Напиши два метода класса, которые создают объекты с определёнными ингредиентами:
# margherita — mozzarella, tomatoes;
# hawaiian — mozzarella, tomatoes, ananas, ham.


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        
    @classmethod
    def create_margherita(cls):
        ingredients = ['mozzarella', 'tomatoes']
        return cls(ingredients)
    
    @classmethod
    def create_hawaiian(cls):
        ingredients = ['mozzarella', 'tomatoes', 'ananas', 'ham']
        return cls(ingredients)

print(Pizza.create_margherita().ingredients) # ['mozzarella', 'tomatoes']
print(Pizza.create_hawaiian().ingredients) # ['mozzarella', 'tomatoes', 'ananas', 'ham']