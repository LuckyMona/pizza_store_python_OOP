from copy import deepcopy
from enum import Enum


class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str, reorder_level: int):
        self.__name = name
        self.__quantity = quantity
        self.__unit = unit
        self.__reorder_level = reorder_level

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def quantity(self) -> float:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: float) -> None:
        self.__quantity = quantity

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str) -> None:
        self.__unit = unit

    @property
    def reorder_level(self) -> int:
        return self.__reorder_level

    @reorder_level.setter
    def reorder_level(self, reorder_level: int) -> None:
        self.__reorder_level = reorder_level

    def __str__(self) -> str:
        return self.to_json().__str__()

    def to_json(self):
        res = {}
        res['name'] = self.__name
        res['quantity'] = self.__quantity
        res['unit'] = self.__unit
        res['reorder_level'] = self.__reorder_level
        return res


class PizzaRecipe:
    def __init__(self, name: str, ingredients: list[Ingredient]) -> None:
        self.__name = name
        self.__ingredients = ingredients  # List of Ingredient objects

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        res = f"Name: {self.__name}, Ingredients: "
        for ingredient in self.__ingredients:
            res += f"{ingredient}, "
        return res
    

    def __repr__(self) -> str:
        return "{" + str(self) + "}"

    def get_ingredients(self) -> list[Ingredient]:
        return deepcopy(self.__ingredients)

    def update_ingredents(self, ingredients: list[Ingredient]) -> None:
        self.__ingredients = deepcopy(ingredients)
    # def update_ingredent(self, ingredient_name: str, quantity: float, reorder_level:int, unit: str) -> None:

    def update_ingredent(self, ingredient_name: str, new_data: dict[str, str | float | int]) -> None:
        for ingredient in self.__ingredients:
            if ingredient.name == ingredient_name:
                for key in new_data:
                    if key in ['quantity', 'reorder_level', 'unit']:
                        setattr(ingredient, key, new_data[key])

    def get_ingredient_names(self) -> str:
        return ','.join([ingredient.name for ingredient in self.__ingredients])

    def to_json(self):
        res = {}
        res['name'] = self.__name
        res['ingredients'] = []
        for ingredient in self.__ingredients:
            res['ingredients'].append(ingredient.to_json())
        return res

# Standard Menu Management:
# a. Create and manage a standard menu of pizzas.
# b. Display each pizza with its name, description, ingredients, and price.
# c. Categorize pizzas based on type, size, or other relevant criteria.


class PizzaSize(Enum):
    MEDIUM = 2
    LARGE = 3
    EXTRA_LARGE = 4


class PizzaType(Enum):
    REGULAR = 1
    SICILIAN = 2


class Menu:
    
    def __init__(self, name: str, description: str, price: float, ingredients_strs: str, size: PizzaSize, type: PizzaType) -> None:
        self.__name = name  # Assume the menu name is the same as the recipe name, so we can use the menu name to find the recipe, 
                            # and recipe name to find the menu. And we don't need to maintain another variable to store the recipe in the menu. 
        self.__description = description
        self.__price = price
        self.__size = size
        self.__ingredients = ingredients_strs   # The ingredients can be different from the recipe,
                                                # because you don't need to show all the ingredients to the customer
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def size(self) -> PizzaSize:
        return self.__size

    @size.setter
    def size(self, size: PizzaSize) -> None:
        self.__size = size

    @property
    def type(self) -> PizzaType:
        return self.__type

    @type.setter
    def type(self, type: PizzaType) -> None:
        self.__type = type

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        self.__description = description

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        self.__price = price

    @property
    def ingredients(self) -> str:
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients: str) -> None:
        self.__ingredients = ingredients

    def __str__(self) -> str:
        type_str = self.type.name if isinstance(self.type, PizzaType) else self.type
        size_str = self.size.name if isinstance(self.size, PizzaSize) else self.size
        return f"Name: {self.name}, Description: {self.description}, Price: {self.price}, Size: {size_str}, Ingredients: {self.ingredients}, Type: {type_str}\n"

    def __repr__(self)-> str:
        return "{" + str(self) + "}"

    def to_json(self):
        res = {}
        res['name'] = self.__name
        res['description'] = self.__description
        res['price'] = self.__price
        res['size'] = self.__size.name if isinstance(self.__size, PizzaSize) else self.__size
        res['ingredients'] = self.__ingredients
        res['type'] = self.__type.name if isinstance(self.__type, PizzaType) else self.__type
        return res

    def display(self) -> None:
        print(f"{self.__name} - {self.__description}")
        print(f"Price: {self.__price}")
        print(f"Size: {self.__size.name}")
        print(f"Type: {self.__type.name}")
        print("Ingredients:")
        print(','.join(self.__ingredients))

# Customer-Customized Pizza Ordering:
# a. Provide customers with the option to create their own pizzas.
# b. Offer a selection of pizza bases, sauces, toppings, and additional ingredients.
# c. Allow customers to customize the quantity of each ingredient.
# d. Display the total price of the customized pizza based on ingredient choices.
class CustomizedPizzaItem:
    def __init__(self,name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    @property
    def price(self) -> float:
        return self.__price
    @price.setter
    def price(self, price: float) -> None:
        self.__price = price
    @property
    def quantity(self) -> int:
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int) -> None:
        self.__quantity = quantity

    def to_json(self):
        res = {}
        res['name'] = self.__name
        res['price'] = self.__price
        res['quantity'] = self.__quantity
        return res
    def __repr__(self) -> dict[str, str|float|int]:
        return self.to_json()

# Side Dish Management:
# a. Create and manage a menu of side dishes.
# b. Display each side dish with its name, description, and price.
# c. Categorize side dishes based on type (e.g., appetizers, desserts, beverages).
class SideDishType(Enum):
    APPETIZERS = 1
    DESSERTS = 2
    BEVERAGES = 3
class SideDishItem:
    def __init__(self, name: str, description: str, price: float, dish_type: SideDishType) -> None:
        self.__name = name
        self.__description = description
        self.__price = price
        self.__type = dish_type

    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    @property
    def description(self) -> str:
        return self.__description
    @description.setter
    def description(self, description: str) -> None:
        self.__description = description
    @property
    def price(self) -> float:
        return self.__price
    @price.setter
    def price(self, price: float) -> None:
        self.__price = price
    @property
    def type(self) -> SideDishType:
        return self.__type
    @type.setter
    def type(self, type: SideDishType) -> None:
        self.__type = type
    def to_json(self):
        res = {}
        res['name'] = self.__name
        res['description'] = self.__description
        res['price'] = self.__price
        res['type'] = self.__type.name
        return res
    def __str__(self) -> str:
        type_str = self.type.name if isinstance(self.type, SideDishType) else self.type
        str = f"Name: {self.name}, Description: {self.description}, Price: {self.price}, Type: {type_str}\n"
        return str
    def __repr__(self) -> str:
        return self.__str__()
        
    

