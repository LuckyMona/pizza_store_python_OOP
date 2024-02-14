from typing import Callable
from controllers import MenuManagement, OptionType
from controller_item import CustomizedPizzaItem, Ingredient, Menu, PizzaRecipe, PizzaSize, PizzaType, SideDishItem, SideDishType
from app_utils import LibraryAppUtils, NumberType

utils = LibraryAppUtils()

class GenerialView:
    @staticmethod
    def process_operation_res(is_success: bool, operation_name: str):
        if is_success:
            print(f"{operation_name} has been done!")
        else:
            print(f"{operation_name} failed!")

class RecipeMngView:
    @staticmethod
    def add_recipe()-> PizzaRecipe:
        recipe_name = input("Enter recipe name: ")
        ingredients = []
        while True:
            ingredient_name = input("Enter ingredient name: ")
            quantity = utils.get_number_input("quantity", NumberType.FLOAT)
            unit = input("Enter unit: ")
            reorder_level = int(utils.get_number_input("reorder level", NumberType.INT))
            ingredients.append(Ingredient(ingredient_name, quantity, unit, reorder_level))
            if input("Do you want to add more ingredients? (y/n): ") == "n":
                break
        recipe = PizzaRecipe(recipe_name, ingredients)
        return recipe
    
    @staticmethod
    def update_recipe()-> tuple[str, str, dict[str, str|float|int]]:
        recipe_name = input("Enter the recipe name you want to update: ")
        ingredient_name = input("Enter ingredient name you want to update: ")
        new_data = InventoryMngView.get_ingredient_new_content()
        return (recipe_name, ingredient_name, new_data)
    
    @staticmethod
    def get_remove_recipe_name():
        recipe_name = input("Enter the recipe name you want to remove: ")
        return recipe_name
   

class InventoryMngView:
    @staticmethod
    def add_ingredient()-> Ingredient:
        ingredient_name = input("Enter ingredient name: ")
        quantity = utils.get_number_input("quantity", NumberType.FLOAT)
        unit = input("Enter unit: ")
        reorder_level = int(utils.get_number_input("reorder level", NumberType.INT))
        return Ingredient(ingredient_name, quantity, unit, reorder_level)
    
    @staticmethod
    def get_ingredient_new_content():
        new_data = {}
        while True:
            print("1. Update quantity")
            print("2. Update unit")
            print("3. Update reorder level")
            print("4. Exit")
            cmd = input("Enter command: ")
            if cmd == "1":
                new_data['quantity'] = utils.get_number_input("quantity", NumberType.FLOAT)
            elif cmd == "2":
                new_data['unit'] = input("Enter unit: ")
            elif cmd == "3":
                new_data['reorder_level'] = int(utils.get_number_input("reorder level", NumberType.INT))
            elif cmd == "4":
                break
            else:
                print("Invalid command!")
        return new_data
    
    @staticmethod
    def update_ingredient()-> tuple[str, dict[str, str|float|int]]:
        ingredient_name = input("Enter ingredient name you want to update: ")
        new_data = InventoryMngView.get_ingredient_new_content()
        return (ingredient_name, new_data)

class MenuView:
    @staticmethod
    def add_menu() -> Menu:
        menu_name = input("Enter menu name: ")
        menu_description = input("Enter menu description: ")
        menu_price = utils.get_number_input("menu price", NumberType.FLOAT)
        
        menu_size_cmd = utils.get_number_input("Enter menu size: 1. Medium 2. Large 3. Extra Large", NumberType.INT)
        menu_type_cmd = utils.get_number_input("menu type: 1. Regular 2. Sicilian", NumberType.INT)
        
        menu_size = PizzaSize.MEDIUM
        menu_type = PizzaType.REGULAR

        if menu_type_cmd == 1:
            menu_type = PizzaType.REGULAR
        elif menu_type_cmd == 2:
            menu_type = PizzaType.SICILIAN

        if menu_size_cmd == 1:
            menu_size = PizzaSize.MEDIUM
        elif menu_size_cmd == 2:
            menu_size = PizzaSize.LARGE
        elif menu_size_cmd == 3:
            menu_size = PizzaSize.EXTRA_LARGE

        ingredients_strs = input("Enter ingredients (separated by comma): ")

        return Menu(menu_name, menu_description, menu_price, ingredients_strs, menu_size, menu_type)
    
    @staticmethod
    def get_menu_new_content() -> dict[str, str|float|int|PizzaSize|PizzaType]:
        new_data = {}
        while True:
            print("1. Update menu description")
            print("2. Update menu price")
            print("3. Update menu size")
            print("4. Update menu type")
            print("5. Update ingredients")
            print("6. Exit")
            cmd = input("Enter command: ")
            
            if cmd == "1":
                new_data['description'] = input("Enter menu description: ")
            elif cmd == "2":
                new_data['price'] = utils.get_number_input("menu price", NumberType.FLOAT)
            elif cmd == "3":
                new_data['size'] = MenuView.get_menu_size()
            elif cmd == "4":
                new_data['type'] = MenuView.get_menu_type()
            elif cmd == "5":
                new_data['ingredients'] = input("Enter ingredients (separated by comma): ")
            elif cmd == "6":
                break
            else:
                print("Invalid command!")
        return new_data

    @staticmethod
    def update_menu() -> tuple[str, dict[str, str|float|int|PizzaSize|PizzaType]]:
        menu_name = input("Enter menu name you want to update: ")
        new_data = MenuView.get_menu_new_content()
        return (menu_name, new_data)
    
    @staticmethod
    def get_menu_type() -> PizzaType:
        menu_type = PizzaType.REGULAR
        while True:
            menu_type_cmd = input("Enter the menu type you want to search: 1. Regular 2. Sicilian:  ")
            if menu_type_cmd == "1":
                menu_type = PizzaType.REGULAR
                break
            elif menu_type_cmd == "2":
                menu_type = PizzaType.SICILIAN
                break
            else:
                print("Invalid command!")
        return menu_type
    @staticmethod
    def get_menu_size()->PizzaSize:
        menu_size = PizzaSize.MEDIUM
        while True:
            menu_size_cmd = input("Enter the menu size you want to search: 1. Medium 2. Large 3. Extra Large:")
            if menu_size_cmd == "1":
                menu_size = PizzaSize.MEDIUM
                break
            elif menu_size_cmd == "2":
                menu_size = PizzaSize.LARGE
                break
            elif menu_size_cmd == "3":
                menu_size = PizzaSize.EXTRA_LARGE
                break
            else:
                print("Invalid command!")
        return menu_size
    
class CustomizedPizzaView:
    @staticmethod
    def get_option_type() -> OptionType:
        opt_type = OptionType.bases
        while True:
            opt_type_cmd = input("Enter the option type: 1. Bases 2. Sauses 3. Toppings 4. Additional Ingredients: ")
            if opt_type_cmd == "1":
                opt_type = OptionType.bases
                break
            elif opt_type_cmd == "2":
                opt_type = OptionType.sauses
                break
            elif opt_type_cmd == "3":
                opt_type = OptionType.toppings
                break
            elif opt_type_cmd == "4":
                opt_type = OptionType.add_ingredients
                break
            else:
                print("Invalid command!")
        return opt_type

    @staticmethod
    def add_option() -> tuple[OptionType, CustomizedPizzaItem]:

        opt_type = CustomizedPizzaView.get_option_type()
        new_opt_name = input("Enter option name: ")
        new_opt_price = utils.get_number_input("option price", NumberType.FLOAT)

        return (opt_type, CustomizedPizzaItem(new_opt_name, new_opt_price, 0))
    
    @staticmethod
    def update_option() -> tuple[OptionType, str, float]:
        opt_type = CustomizedPizzaView.get_option_type()
        opt_name = input("Enter the option name you want to update: ")
        opt_price = utils.get_number_input("option price", NumberType.FLOAT)
        return (opt_type, opt_name, opt_price)
    
    @staticmethod
    def remove_option() -> tuple[OptionType, str]:
        opt_type = CustomizedPizzaView.get_option_type()
        opt_name = input("Enter the option name you want to remove: ")
        return (opt_type, opt_name)

    @staticmethod
    def print_pizza_options(opt_type: OptionType, options) -> None:
        print(f"Pizza {opt_type.name}:")
        for opt in options:
            if isinstance(opt, CustomizedPizzaItem):
                print(f"{opt.name} - ${opt.price}")
            else:
                print(f"{opt['name']} - ${opt['price']}")
        print()
    @staticmethod
    def print_all_pizza_options(json_data) -> None:
        for opt_type in OptionType:
            CustomizedPizzaView.print_pizza_options(opt_type, json_data[opt_type.name])
class SideDishView:
    @staticmethod
    def get_side_dish_type() -> SideDishType:
        side_dish_type = SideDishType.APPETIZERS
        while True:
            side_dish_type_cmd = input("Enter the side dish type: 1. Appetizers 2. Desserts 3. Beverages: ")
            if side_dish_type_cmd == "1":
                side_dish_type = SideDishType.APPETIZERS
                break
            elif side_dish_type_cmd == "2":
                side_dish_type = SideDishType.DESSERTS
                break
            elif side_dish_type_cmd == "3":
                side_dish_type = SideDishType.BEVERAGES
                break
            else:
                print("Invalid command!")
        return side_dish_type
    @staticmethod
    def get_side_dish_new_content() -> dict[str, str|float|SideDishType]:
        new_data = {}
        new_data["description"] = input("Enter side dish description: ")
        new_data["price"] = utils.get_number_input("side dish price", NumberType.FLOAT)
        new_data["type"] = SideDishView.get_side_dish_type()
        return new_data
    @staticmethod
    def add_side_dish() -> SideDishItem:
        side_dish_name = input("Enter side dish name: ")
        new_data = SideDishView.get_side_dish_new_content()
        return SideDishItem(side_dish_name, str(new_data["description"]), new_data["price"], new_data["type"])  # type: ignore

    @staticmethod
    def update_side_dish()-> tuple[str, dict[str, str|float|SideDishType]]:
        side_dish_name = input("Enter side dish name you want to update: ")
        new_data = SideDishView.get_side_dish_new_content()
        return (side_dish_name, new_data)
    @staticmethod
    def print_side_dishes(dishes: list[SideDishItem])->None:
        if len(dishes) == 0:
            print("No side dishes!")
            return
        for dish in dishes:
            # print(f"Name: {dish["name"]}, Description: {dish["description"]}, Price: {dish["price"]}, Type: {dish["type"].name}")  # type: ignore
            print(dish.to_json())
        print()

class OrderView:
    @staticmethod
    def place_order(menus: list[Menu], customized_data, side_dishes) -> dict[str, list[str]|str|float|int]:
        order_data = {}
        print("Do you want order standard pizzas? (y/n)")
        while True:
            cmd = input("Enter command: ")
            if cmd == "y":
                if len(menus) == 0:
                    print("No standard pizzas in menu, please tell shop owner to add standard pizzas to menu!\n")
                    break
                order_data["standard_pizzas"] = OrderView.get_standard_pizzas(menus)
                break
            elif cmd == "n":
                break
            else:
                print("Invalid command!")
        
        print("Do you want order customized pizzas? (y/n)")
        while True:
            cmd = input("Enter command: ")
            if cmd == "y":
                order_data["customized_pizzas"] = OrderView.get_customized_pizzas(customized_data)
                break
            elif cmd == "n":
                break
            else:
                print("Invalid command!")
        
        print("Do you want order side dishes? (y/n)")
        while True:
            cmd = input("Enter command: ")
            if cmd == "y":
                if len(side_dishes) == 0:
                    print("No side dishes in menu, please tell shop owner to add side dishes to menu!\n")
                    break
                order_data["side_dishes"] = OrderView.get_side_dishes(side_dishes)
                break
            elif cmd == "n":
                break
            else:
                print("Invalid command!")

        order_data['total'] = 0
        if 'standard_pizzas' in order_data:
            order_data['total'] += float(order_data['standard_pizzas']['total']) # type: ignore
        if 'customized_pizzas' in order_data:
            order_data['total'] += float(order_data['customized_pizzas']['total']) # type: ignore
        if 'side_dishes' in order_data:
            order_data['total'] += float(order_data['side_dishes']['total']) # type: ignore
        
        display_order_cmd = input("Do you want to display the order details? (y/n)")
        if display_order_cmd == "y":
            OrderView.display_order(order_data)
        
        return order_data

    @staticmethod
    def get_standard_pizzas(menus: list[Menu]) -> dict[str, list[Menu]|float]:
        standard_pizzas = []
        while True:
            print("Please select the menu name for your pizza:")

            for menu in menus:
                print(f"{menu}")
            menu_name_cmd = input("Enter the menu name: ")
            menu_ordered = None
            for _menu in menus:
                if _menu.name == menu_name_cmd:
                    menu_ordered = _menu.to_json()
                    break
            if menu_ordered is None:
                print("Invalid menu name!")
                continue
            else:
                menu_ordered['quantity'] = utils.get_number_input("quantity", NumberType.INT) # type: ignore
                standard_pizzas.append(menu_ordered)
            print(f"Do you want to add more standard pizzas? (y/n)")
            if input("Enter command: ") == "y":
                continue
            else:
                break
        total = sum([float(_pizza['price']) for _pizza in standard_pizzas])
        return {"standard_pizzas": standard_pizzas, "total": total}
    
    @staticmethod
    def get_customized_pizza_part(options, part_name: str) -> dict[str, str|float|int]:
        while True:
            print(f"\nPlease select the {part_name} name for your pizza: ")
            for option in options:
                print(f"Name: {option['name']}, Price: ${option['price']}") # type: ignore
            print()
            part_name_cmd = input(f"Enter the {part_name} name: ")
            part = None
            for _opt in options:
                if _opt['name'] == part_name_cmd: # type: ignore
                    part = _opt
                    break
            if part is None:
                print("Invalid sause name!")
                continue
            else:
                return part
    
    @staticmethod
    def get_customized_pizza_parts(parts: list[CustomizedPizzaItem], part_name: str) -> list[dict[str, str|float|int]]:
        customized_parts = []
        while True:
            t = {}
            t['name'] = OrderView.get_customized_pizza_part(parts, part_name)['name'] # type: ignore
            t['quantity'] = utils.get_number_input("quantity", NumberType.INT)
            t['price'] = [_part['price'] for _part in parts if _part['name'] == t['name']][0] # type: ignore
            t['total'] = float(t['price']) * float(t['quantity'])
            customized_parts.append(t)
            print(f"Do you want to add more {part_name}? (y/n)")
            if input("Enter command: ") == "y":
                continue
            else:
                break
        return customized_parts
    
    @staticmethod
    def get_customized_pizzas(customized_data) -> dict[str, list[dict[str, str|float|int]]|float]:
        customized_pizzas = []
        while True:
            cus_pizza = {}
            # Assume that the user can select one base, one sause, multiple toppings and multiple additional ingredients for each customized pizza
            cus_pizza["base"] = OrderView.get_customized_pizza_part(customized_data["bases"], 'base')
            cus_pizza["sause"] = OrderView.get_customized_pizza_part(customized_data["sauses"], 'sause')
            cus_pizza["toppings"] = OrderView.get_customized_pizza_parts(customized_data["toppings"], 'topping')
            cus_pizza["add_ingredients"] = OrderView.get_customized_pizza_parts(customized_data["add_ingredients"], 'additional ingredient')
            cus_pizza["total"] = float(cus_pizza['base']['price']) + float(cus_pizza["sause"]['price']) + sum([float(_topping['total']) for _topping in cus_pizza["toppings"]]) + sum([float(_ingredient['total']) for _ingredient in cus_pizza["add_ingredients"]]) # type: ignore
            customized_pizzas.append(cus_pizza)
            print(f"Do you want to add more customized pizzas? (y/n)")
            if input("Enter command: ") == "y":
                continue
            else:
                break
        total = sum([float(_pizza['total']) for _pizza in customized_pizzas])
        return {"customized_pizzas": customized_pizzas, "total": total}
    
    @staticmethod
    def get_side_dishes(side_dishes: list[SideDishItem]) -> dict[str, list[SideDishItem] | float]:
        order_side_dishes = []
        dish = None
        while True:
            while True:
                for s in side_dishes:
                    print(f"Name: {s.name}, Description: {s.description}, Price: ${s.price}, Type: {s.type.name}\n")
                dish_name_cmd = input("Enter the side dish name you want to order: ")
                for d in side_dishes:
                    if d.name == dish_name_cmd:
                        dish = d.to_json()
                        break
                if dish is None:
                    print("Invalid side dish name!")
                    continue
                else:
                    dish['quantity'] = utils.get_number_input("quantity", NumberType.INT)
                    order_side_dishes.append(dish)
                    break
            print(f"Do you want to add more side dishes? (y/n)")
            if input("Enter command: ") == "y":
                continue
            else:
                break
        total = sum([float(_dish['price']) for _dish in order_side_dishes])
        return {"side_dishes": order_side_dishes, "total": total}

    @staticmethod
    def display_order(order):
        print("Order details:")
        if 'standard_pizzas' in order:
            print(f"Standard pizzas: ")
            data = order['standard_pizzas']
            for pizza in data['standard_pizzas']:
                print(f"\tName: {pizza['name']}, Description: {pizza['description']}, Price: ${pizza['price']}, Size: {pizza['size']}, Type: {pizza['type']}")
            print(f"\tSub Total: ${data['total']}\n")
        
        if 'customized_pizzas' in order:
            print(f"Customized pizzas:\n")
            data = order['customized_pizzas']
            for pizza in data['customized_pizzas']:
                print(f"\tBase: {pizza['base']['name']}")
                print(f"\tSause: {pizza['sause']['name']}")
                print(f"\tToppings: ")
                for topping in pizza['toppings']:
                    print(f"\t\tName: {topping['name']}, Price: ${topping['price']}, Quantity: {topping['quantity']}, Total: ${topping['total']}")
                print(f"\tAdditional ingredients: ")
                for ingredient in pizza['add_ingredients']:
                    print(f"\t\tName: {ingredient['name']}, Price: ${ingredient['price']}, Quantity: {ingredient['quantity']}, Total: ${ingredient['total']}")
                print(f"\tSub Total: ${pizza['total']}\n")
        
        if 'side_dishes' in order:
            print(f"Side dishes:\n")
            data = order['side_dishes']
            for dish in data['side_dishes']:
                print(f"\tName: {dish['name']}, Description: {dish['description']}, Price: ${dish['price']}, Type: {dish['type']}")
            print(f"\tSub Total: ${data['total']}\n")
            
        print(f"Total: ${order['total']}")
    
    @staticmethod
    def get_order_id(order_ids) -> str:
        if len(order_ids) == 0:
            print("No order!")
            return ""
        print("Please select the order id:")
        for order_id in order_ids:
            print(order_id)

        return input("Enter the order id: ")
    

   

    
        
            
        