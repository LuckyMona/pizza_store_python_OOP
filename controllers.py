from copy import deepcopy
from enum import Enum

from Constants import DEFAULT_PIZZA_BASES,DEFAULT_PIZZA_SAUCES,DEFAULT_PIZZA_TOPPINGS,DEFAULT_ADD_INGREDIENTS, ORDER_FILEPATH, RECIPE_FILEPATH, INGREDIENT_FILEPATH, MENU_FILEPATH, CUSTOMIZED_PIZZA_FILEPATH, SIDE_DISH_FILEPATH, get_path
from repo import Repo
from controller_item import CustomizedPizzaItem, Menu, PizzaRecipe, Ingredient, PizzaSize, PizzaType, SideDishItem, SideDishType
from typing import Optional


# Pizza Recipe Management:
# a. Create, edit, and delete pizza recipes.
# b. Store detailed information about each recipe, including ingredients and quantities.
# c. Categorize recipes based on pizza type (e.g., vegetarian, meat lovers, specialty).
# d. Implement search functionality to easily find specific recipes.


class RecipeManagement:
    def __init__(self) -> None:
        self.__recipes: list[PizzaRecipe] = []
        self.load_from_db()

    def add_recipe(self, recipe: PizzaRecipe) -> bool:
        self.__recipes.append(recipe)
        self.save_to_db()
        return True

    def remove_recipe(self, recipe_name: str) -> bool:
        is_found = False
        for recipe in self.__recipes:
            if recipe.name == recipe_name:
                self.__recipes.remove(recipe)
                self.save_to_db()
                is_found = True
                break
        return is_found

    def update_recipe_by_ingredient(self, recipe_name: str, ingredient_name: str, new_data: dict[str, str|int|float]) -> bool:
        is_Found = False
        for recipe in self.__recipes:
            if recipe.name == recipe_name:
                recipe.update_ingredent(ingredient_name, new_data)
                is_Found = True
                break
        self.save_to_db()
        return is_Found

    def search_recipe_by_name(self, recipe_name: str) -> Optional[PizzaRecipe]:
        for recipe in self.__recipes:
            if recipe.name == recipe_name:
                return recipe
        return None

    def list_recipes(self) -> None:
        if len(self.__recipes) == 0:
            print("No recipes!")
        for recipe in self.__recipes:
            print(recipe.to_json())
    def get_recipes(self) -> list[PizzaRecipe]:
        return deepcopy(self.__recipes)

    def save_to_db(self) -> None:
        recipe_filepath = get_path(RECIPE_FILEPATH)
        repos = Repo(recipe_filepath)
        repos.save_items([recipe.to_json() for recipe in self.__recipes])

    def load_from_db(self) -> None:
        recipe_filepath = get_path(RECIPE_FILEPATH)
        repos = Repo(recipe_filepath)
        data = repos.get_items()
        for recipe in data:
            ingredients = []
            for ingredient in recipe['ingredients']:
                ingredients.append(Ingredient(
                    ingredient['name'], ingredient['quantity'], ingredient['unit'], ingredient['reorder_level']))
            self.__recipes.append(PizzaRecipe(recipe['name'], ingredients))

# Ingredient Inventory Management:
# a. Maintain an inventory of all pizza ingredients.
# b. Track ingredient usage based on recipe requirements.
# c. Generate alerts for low-stock ingredients to ensure adequate supply.


class InventoryManagement:
    def __init__(self) -> None:
        self.__ingredients: dict[str, Ingredient] = {}
        self.load_from_db()

    def add_ingredient(self, ingredient: Ingredient) -> None:
        self.__ingredients[ingredient.name] = ingredient
        self.save_to_db()

    def reduce_ingredient_by_quantity(self, ingredient_name: str, quantity: float) -> None:
        self.__ingredients[ingredient_name].quantity -= quantity
        self.save_to_db()

    def update_ingredient(self, ingredient_name: str, new_data: dict[str, int | str | float]) -> None:
        for key in new_data:
            if key in ['quantity', 'reorder_level', 'unit']:
                setattr(
                    self.__ingredients[ingredient_name], key, new_data[key])
        self.save_to_db()

    def remove_ingredient(self, ingredient_name: str) -> None:
        self.__ingredients.pop(ingredient_name)
        self.save_to_db()

    def use_ingredient_by_recipe(self, recipe: PizzaRecipe) -> None:
        for ingredient in recipe.get_ingredients():
            self.reduce_ingredient_by_quantity(
                ingredient.name, ingredient.quantity)
        self.save_to_db()

    def check_reorder_levels(self) -> None:
        is_low_stock = False
        for ingredient in self.__ingredients.values():
            if ingredient.quantity < ingredient.reorder_level:
                print(
                    f"Low stock for {ingredient.name}! Current stock: {ingredient.quantity}")
                is_low_stock = True
        if not is_low_stock:
            print("No low stock!")

    def print_inventory(self) -> None:
        for name, ingredient in self.__ingredients.items():
            print(ingredient.to_json())

    def save_to_db(self) -> None:
        ingredient_filepath = get_path(INGREDIENT_FILEPATH)
        repos = Repo(ingredient_filepath)
        repos.save_items([ingredient.to_json()
                         for ingredient in self.__ingredients.values()])

    def load_from_db(self) -> None:
        ingredient_filepath = get_path(INGREDIENT_FILEPATH)
        repos = Repo(ingredient_filepath)
        data = repos.get_items()
        for ingredient in data:
            self.__ingredients[ingredient['name']] = Ingredient(
                ingredient['name'], ingredient['quantity'], ingredient['unit'], ingredient['reorder_level'])

    def search_ingredient_by_name(self, ingredient_name: str) -> Optional[Ingredient]:
        if ingredient_name in self.__ingredients:
            return self.__ingredients[ingredient_name]
        return None


# Standard Menu Management:
# a. Create and manage a standard menu of pizzas.
# b. Display each pizza with its name, description, ingredients, and price.
# c. Categorize pizzas based on type, size, or other relevant criteria.
class MenuManagement:
    def __init__(self) -> None:
        self.__menus: list[Menu] = []
        self.load_from_db()

    def get_menus(self) -> list[Menu]:
        return deepcopy(self.__menus)
    
    def to_json(self) -> list[dict[str, str | int | float | PizzaSize | PizzaType]]:
        return [menu.to_json() for menu in self.__menus]
    
    # def get_menu_names(self) -> list[str]:
    #     return [menu.name for menu in self.__menus]

    def check_menu_exist(self, name: str) ->bool:
        for menu in self.__menus:
            if menu.name == name:
                return True
        return False
    
    def __str__(self) -> str:
        str = ""
        for menu in self.__menus:
            str += menu.__str__() + '\n'
        return str
    
    def __repr__(self) -> str:
        return str(self.to_json())

    def add_menu(self, menu: Menu) -> None:
        self.__menus.append(menu)
        self.save_to_db()

    def remove_menu(self, menu_name: str) -> None:
        is_Found = False
        for menu in self.__menus:
            if menu.name == menu_name:
                self.__menus.remove(menu)
                self.save_to_db()
                is_Found = True
                break
        if not is_Found:
            print("Menu not found!")

    def update_menu(self, menu_name: str, new_data: dict[str, str | int | float | PizzaSize | PizzaType]) -> None:
        for menu in self.__menus:
            if menu.name == menu_name:
                for key in new_data:
                    if key in ['description', 'type', 'size', 'price', 'ingredients']:
                        setattr(menu, key, new_data[key])
                self.save_to_db()
                break

    def search_menu_by_name(self, menu_name: str) -> Optional[Menu]:
        for menu in self.__menus:
            if menu.name == menu_name:
                return menu
        return None

    def get_menu_by_type(self, pizza_type: PizzaType) -> list[Menu]:
        menus: list[Menu] = []
        for menu in self.__menus:
            if menu.type == pizza_type:
                menus.append(menu)
        return menus

    def get_menu_by_size(self, size: PizzaSize) -> list[Menu]:
        menus: list[Menu] = []
        for menu in self.__menus:
            if menu.size == size:
                menus.append(menu)
        return menus

    def print_menu(self) -> None:
        for menu in self.__menus:
            print(menu.to_json())

    def save_to_db(self) -> None:
        menu_filepath = get_path(MENU_FILEPATH)
        repos = Repo(menu_filepath)
        repos.save_items([menu.to_json() for menu in self.__menus])

    def load_from_db(self) -> None:
        menu_filepath = get_path(MENU_FILEPATH)
        repos = Repo(menu_filepath)
        data = repos.get_items()
        for menu in data:
            self.__menus.append(Menu(menu['name'], menu['description'],
                                menu['price'], menu['ingredients'], menu['size'], menu['type']))


# Customer-Customized Pizza Ordering:
# a. Provide customers with the option to create their own pizzas.
# b. Offer a selection of pizza bases, sauces, toppings, and additional ingredients.
# c. Allow customers to customize the quantity of each ingredient.
# d. Display the total price of the customized pizza based on ingredient choices.



class OptionType(Enum):
    bases = 1
    sauses = 2
    toppings = 3
    add_ingredients = 4


class CustomizedPizzaManagement:
    def __init__(self) -> None:
        self.__bases: list[CustomizedPizzaItem] = []
        self.__sauses: list[CustomizedPizzaItem] = []
        self.__toppings: list[CustomizedPizzaItem] = []
        self.__add_ingredients: list[CustomizedPizzaItem] = []
        self.load_from_default_db()

    def get_bases(self) -> list[CustomizedPizzaItem]:
        return deepcopy(self.__bases)

    def get_sauses(self) -> list[CustomizedPizzaItem]:
        return deepcopy(self.__sauses)

    def get_toppings(self) -> list[CustomizedPizzaItem]:
        return deepcopy(self.__toppings)

    def get_add_ingredients(self) -> list[CustomizedPizzaItem]:
        return deepcopy(self.__add_ingredients)

    def add_option(self, option_type: OptionType, option: CustomizedPizzaItem) -> bool:
        private_name = f"_{self.__class__.__name__}__{option_type.name}"
        getattr(self, private_name).append(option)
        self.save_to_db()
        return True

    def remove_option(self, option_type: OptionType, option_name: str) -> bool:
        is_found = False
        private_name = f"_{self.__class__.__name__}__{option_type.name}"
        options = getattr(self, private_name)
        for option in options:
            _name = option.name if isinstance(option, CustomizedPizzaItem) else option['name']
            if _name == option_name:
                options.remove(option)
                is_found = True
                break
        if is_found:
            self.save_to_db()
        return is_found

    def update_option(self, type: OptionType, option_name: str, option_price: float) -> bool:
        is_found = False
        private_name = f"_{self.__class__.__name__}__{type.name}"
        options = getattr(self, private_name)
        for option in options:
            _name =  option.name if isinstance(option, CustomizedPizzaItem) else option['name']
            if _name == option_name:
                if isinstance(option, CustomizedPizzaItem):
                    option.price = option_price
                else:
                    option['price'] = option_price
                is_found = True
                break
        if is_found:
            self.save_to_db()
        return is_found

    def get_total_price(self, options: list[dict[str, str | int | float]]) -> float:
        total_price = 0
        for option in options:
            total_price += float(option['price']) * int(option['quantity'])
        return total_price

    def to_json(self) -> dict[str, list[dict[str, str | int | float]]]:
        return {
            'bases': [base.to_json() if isinstance(base, CustomizedPizzaItem) else base for base in self.__bases],
            'sauses': [sause.to_json() if isinstance(sause, CustomizedPizzaItem) else sause for sause in self.__sauses],
            'toppings': [topping.to_json() if isinstance(topping, CustomizedPizzaItem) else topping for topping in self.__toppings],
            'add_ingredients': [add_ingredient.to_json() if isinstance(add_ingredient, CustomizedPizzaItem) else add_ingredient for add_ingredient in self.__add_ingredients]
        }

    def save_to_db(self) -> None:
        repos = Repo(CUSTOMIZED_PIZZA_FILEPATH)
        repos.save_items(self.to_json())

    def load_from_db(self, is_default: bool) -> None:
        data = {}
        if not is_default:
            repos = Repo(CUSTOMIZED_PIZZA_FILEPATH)
            data = repos.get_items()
        else:
            data = {
                'bases': DEFAULT_PIZZA_BASES,
                'sauses': DEFAULT_PIZZA_SAUCES,
                'toppings': DEFAULT_PIZZA_TOPPINGS,
                'add_ingredients': DEFAULT_ADD_INGREDIENTS
            }
        self.__bases = [CustomizedPizzaItem(base['name'], base['price'], base['quantity']) for base in data['bases']]
        self.__sauses = [CustomizedPizzaItem(sause['name'], sause['price'], sause['quantity']) for sause in data['sauses']]
        self.__toppings = [CustomizedPizzaItem(topping['name'], topping['price'], topping['quantity']) for topping in data['toppings']]
        self.__add_ingredients = [CustomizedPizzaItem(add_ingredient['name'], add_ingredient['price'], add_ingredient['quantity']) for add_ingredient in data['add_ingredients']]

    def load_from_default_db(self) -> None:
        self.load_from_db(True)
        self.save_to_db()
        
# Side Dish Management:
# a. Create and manage a menu of side dishes.
# b. Display each side dish with its name, description, and price.
# c. Categorize side dishes based on type (e.g., appetizers, desserts, beverages).
class SideDishManagement:
    def __init__(self) -> None:
        self.__side_dishes: list[SideDishItem] = []
        self.load_from_db()

    def get_all_side_dishes(self) -> list[SideDishItem]:
        return deepcopy(self.__side_dishes)
    
    def add_side_dish(self, side_dish: SideDishItem) -> bool:
        self.__side_dishes.append(side_dish)
        self.save_to_db()
        return True
    def rm_side_dish(self, side_dish_name: str) -> bool:
        is_found = False
        for side_dish in self.__side_dishes:
            if side_dish.name == side_dish_name:
                self.__side_dishes.remove(side_dish)
                self.save_to_db()
                is_found = True
                break
        return is_found

    def update_side_dish(self, side_dish_name: str, new_data: dict[str, str | float | SideDishType]) -> bool:
        is_found = False
        for side_dish in self.__side_dishes:
            if side_dish.name == side_dish_name:
                for key in new_data:
                    if key in ['description', 'price', 'type']:
                        setattr(side_dish, key, new_data[key])
                self.save_to_db()
                is_found = True
                break
        return is_found
    def get_side_dish_by_type(self, side_dish_type: SideDishType) -> list[SideDishItem]:
        side_dishes: list[SideDishItem] = []
        for side_dish in self.__side_dishes:
            if side_dish.type == side_dish_type:
                side_dishes.append(side_dish)
        return side_dishes
    
    def save_to_db(self) -> None:
        repos = Repo(SIDE_DISH_FILEPATH)
        repos.save_items([side_dish.to_json() for side_dish in self.__side_dishes])
                         
    def load_from_db(self) -> None:
        repos = Repo(SIDE_DISH_FILEPATH)
        data = repos.get_items()
        for side_dish in data:
            self.__side_dishes.append(SideDishItem(side_dish['name'], side_dish['description'], side_dish['price'], SideDishType[side_dish['type']]))
    
class OrderManagement:
    def __init__(self) -> None:
        self.__orders = []
        self.__id = 0
        self.load_from_db()

    def add_order(self, order) -> bool:
        order['id'] = self.__id
        self.__orders.append(order)
        self.__id += 1
        self.save_to_db()
        return True
    
    def get_orders(self) -> list[dict[str, str | int | float]]:
        return deepcopy(self.__orders)

    def get_order_ids(self) -> list[int]:
        return [order['id'] for order in self.__orders]
    
    def get_order_by_id(self, id: int) -> Optional[dict[str, str | int | float]]:
        for order in self.__orders:
            if order['id'] == id:
                return deepcopy(order)
        return None
    
    def get_orders_for_kitchen(self, recipes: list[PizzaRecipe], order_id) -> str:
        orders = [order for order in self.__orders if int(order['id']) == int(order_id)]
        if len(orders) == 0:
            return ""
        order = orders[0]
        order_strs_for_kitchen = ""
        
        order_strs_for_kitchen += f"Order ID: {order['id']}\n"

        if 'standard_pizzas' in order:
            order_strs_for_kitchen += "\tStandard Pizzas:\n"
            standard_pizzas = order['standard_pizzas']['standard_pizzas']
            for pizza in standard_pizzas:
                order_strs_for_kitchen += f"\t\tName: {pizza['name']}, Size: {pizza['size']}, Type: {pizza['type']}\n"
                recipe =[re for re in recipes if re.name == pizza['name']][0]
                order_strs_for_kitchen += f"\t\tRecipe: {recipe}\n"
        
        if 'customized_pizzas' in order:
            order_strs_for_kitchen += "\tCustomized Pizzas:\n"
            customized_pizzas = order['customized_pizzas']['customized_pizzas']
            for customized_pizza in customized_pizzas:
                bases = customized_pizza['base']
                sauce = customized_pizza['sause']
                toppings = customized_pizza['toppings']
                add_ingredients = customized_pizza['add_ingredients']

                order_strs_for_kitchen += f"\t\tBase: {bases['name']}\n"
                order_strs_for_kitchen += f"\t\tSauce: {sauce['name']}\n"
                order_strs_for_kitchen += "\t\tToppings:\n"
                for topping in toppings:
                    order_strs_for_kitchen += f"\t\t\tName: {topping['name']}, Quantity: {topping['quantity']}\n"
                order_strs_for_kitchen += "\t\tAdded Ingredients:\n"
                for add_ingredient in add_ingredients:
                    order_strs_for_kitchen += f"\t\t\tName: {add_ingredient['name']}, Quantity: {add_ingredient['quantity']}\n"

        if 'side_dishes' in order:
            order_strs_for_kitchen += "\tSide Dishes:\n"
            side_dishes = order['side_dishes']['side_dishes']
            for side_dish in side_dishes:
                order_strs_for_kitchen += f"\t\tName: {side_dish['name']}, Quantity: {side_dish['quantity']}\n"
        return order_strs_for_kitchen

    def load_from_db(self) -> None:
        repo = Repo(ORDER_FILEPATH)
        data = repo.get_items()
        self.__orders = data['orders']
        self.__id = data['id']
        
    def save_to_db(self) -> None:
        repo = Repo(ORDER_FILEPATH)
        repo.save_items({
            "orders": self.__orders,
            "id": self.__id
        })


    