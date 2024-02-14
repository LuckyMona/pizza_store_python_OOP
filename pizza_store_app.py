from controller_item import Menu, PizzaRecipe
from controllers import CustomizedPizzaManagement, OptionType, OrderManagement, RecipeManagement, InventoryManagement, MenuManagement, SideDishManagement
from app_views import CustomizedPizzaView, GenerialView, InventoryMngView, MenuView, OrderView, RecipeMngView, SideDishView


class PizzaStore:
    def __init__(self) -> None:
        self.__recipe_mgt: RecipeManagement = RecipeManagement()
        self.__inventory_mgt: InventoryManagement = InventoryManagement()
        self.__menu_mgt: MenuManagement = MenuManagement()
        self.__customized_pizza_mgt: CustomizedPizzaManagement = CustomizedPizzaManagement()
        self.__side_dish_mgt: SideDishManagement = SideDishManagement()
        self.__order_mgt: OrderManagement = OrderManagement()

    def show_recipe_menu(self) -> None:
        print("1. Add Recipe")
        print("2. Update Recipe")
        print("3. Remove Recipe")
        print("4. Search Recipe By Name")
        print("5. Print Recipes")
        print("6. Exit")

    def show_inventory_menu(self) -> None:
        print("1. Add Ingredient")
        print("2. Update Ingredient")
        print("3. Remove Ingredient")
        print("4. Check Reorder Levels")
        print("5. Print Inventory")
        print("6. Use Ingredient By Recipe")
        print("7. Search Ingredient By Name")
        print("8. Exit")
    
    def show_menu_menu(self) -> None:
        print("1. Add Menu")
        print("2. Update Menu")
        print("3. Remove Menu")
        print("4. Get Menu By Type")
        print("5. Get Menu By Size")
        print("6. Print Menu")
        print("7. Exit")
    def show_customized_pizza_menu(self) -> None:
        print("1. Add customized pizza ingredient option")
        print("2. Update customized pizza ingredient option")
        print("3. Remove customized pizza ingredient option")
        print("4. Print all pizza base options")
        print("5. Print all pizza sauce options")
        print("6. Print all pizza topping options")
        print("7. Print all pizza additional ingredients options")
        print("8. Print all pizza options")
        print("0. Exit")
    def show_side_dish_menu(self) -> None:
        print("1. Add Side Dish")
        print("2. Update Side Dish")
        print("3. Remove Side Dish")
        print("4. Get Side Dish By Type")
        print("5. Print All Side Dishes")
        print("0. Exit")
    
    def show_order_menu(self) -> None:
        print("1. Add Order")
        print("2. Display Order Details")
        print("3. Generate order slips for kitchen staff")
        print("0. Exit")
    
    def process_recipe_menu(self) -> None:
        while True:
            self.show_recipe_menu()
            cmd = input("Enter command: ")
            if cmd == "1":
                recipe: PizzaRecipe = RecipeMngView.add_recipe()
                add_res = self.__recipe_mgt.add_recipe(recipe)
                GenerialView.process_operation_res(add_res, "Add recipe")

            elif cmd == "2":
                (recipe_name, ingredient_name, new_data) = RecipeMngView.update_recipe()
                update_res = self.__recipe_mgt.update_recipe_by_ingredient(recipe_name,ingredient_name, new_data )
                GenerialView.process_operation_res(update_res, "Update recipe")

            elif cmd == "3":
                rm_recipe_name = RecipeMngView.get_remove_recipe_name()
                rm_recipe_res = self.__recipe_mgt.remove_recipe(rm_recipe_name)
                GenerialView.process_operation_res(rm_recipe_res, "Remove recipe")

            elif cmd == "4":
                srch_recipe_name = input("Enter the recipe name you want to search: ")
                srch_res = self.__recipe_mgt.search_recipe_by_name(srch_recipe_name)
                if srch_res is not None:
                    print(srch_res)
                else:
                    print("Recipe not found!")

            elif cmd == "5":
                self.__recipe_mgt.list_recipes()

            elif cmd == "6":
                break

            else:
                print("Invalid command!")

    def process_inventory_menu(self) -> None:
        while True:
            self.show_inventory_menu()
            inventory_cmd = input("Enter command: ")
            if inventory_cmd == "1":
                new_ingredient = InventoryMngView.add_ingredient()
                self.__inventory_mgt.add_ingredient(new_ingredient)
                print("Ingredient has been added!")

            elif inventory_cmd == "2":
                (update_ingredient_name, new_data) = InventoryMngView.update_ingredient()
                self.__inventory_mgt.update_ingredient(update_ingredient_name, new_data)
                print("Ingredient has been updated!")
                self.__inventory_mgt.check_reorder_levels()

            elif inventory_cmd == "3":
                rm_ingredient_name = input("Enter the ingredient name you want to remove: ")
                self.__inventory_mgt.remove_ingredient(rm_ingredient_name)
                print("Ingredient has been removed!")

            elif inventory_cmd == "4":
                self.__inventory_mgt.check_reorder_levels()

            elif inventory_cmd == "5":
                self.__inventory_mgt.print_inventory()

            elif inventory_cmd == "6":
                recipe_name = input("Enter the recipe name you want to use: ")
                recipe = self.__recipe_mgt.search_recipe_by_name(recipe_name)
                if recipe is not None:
                    self.__inventory_mgt.use_ingredient_by_recipe(recipe)
                    print("Ingredient has been used!")
                    self.__inventory_mgt.check_reorder_levels()
                else:
                    print("Recipe not found!")

            elif inventory_cmd == "7":
                srch_ingredient_name = input("Enter the ingredient name you want to search: ")
                srch_res = self.__inventory_mgt.search_ingredient_by_name(srch_ingredient_name)
                if srch_res is not None:
                    print(srch_res)
                else:
                    print("Ingredient not found!")
                    
            elif inventory_cmd == "8":
                break
            else:
                print("Invalid command!")
    
    def process_menu_menu(self) -> None:
        # print("1. Add Menu")
        # print("2. Update Menu")
        # print("3. Remove Menu")
        # print("4. Get Menu By Type")
        # print("5. Get Menu By Size")
        # print("6. Print Menu")
        # print("7. Exit")
        while True:
            self.show_menu_menu()
            cmd = input("Enter command: ")
            if cmd == "1":
                new_menu = MenuView.add_menu()
                self.__menu_mgt.add_menu(new_menu)
                print("Menu has been added!")

            elif cmd == "2":
                (menu_name, new_data ) = MenuView.update_menu()
                self.__menu_mgt.update_menu(menu_name, new_data)
                print("Menu has been updated!")

            elif cmd == "3":
                rm_menu_name = input("Enter the menu name you want to remove: ")
                self.__menu_mgt.remove_menu(rm_menu_name)
                print("Menu has been removed!")

            elif cmd == "4":
                menu_type = MenuView.get_menu_type()
                menus = self.__menu_mgt.get_menu_by_type(menu_type)
                if len(menus) > 0:
                    for menu in menus:
                        print(menu.to_json())
                else:
                    print("Menu not found!")

            elif cmd == "5":
                menu_size = MenuView.get_menu_size()
                menus_by_size: list[Menu] = self.__menu_mgt.get_menu_by_size(menu_size)
                if len(menus_by_size) > 0:
                    for menu in menus_by_size:
                        print(menu.to_json())
                else:
                    print("Menu not found!")
            elif cmd == "6":
                self.__menu_mgt.print_menu()
                pass
            elif cmd == "7":
                break
            else:
                print("Invalid command!")

    def process_customized_pizza_menu(self) -> None:
        while True:
            self.show_customized_pizza_menu()
            cmd = input("Enter command: ")
            if cmd == "1":
                (option_type, new_option) = CustomizedPizzaView.add_option()
                add_res = self.__customized_pizza_mgt.add_option(option_type, new_option)
                GenerialView.process_operation_res(add_res, "Add option")
            elif cmd == "2":
                (option_type, option_name, option_price) = CustomizedPizzaView.update_option()
                update_res = self.__customized_pizza_mgt.update_option(option_type, option_name, option_price)
                GenerialView.process_operation_res(update_res, "Update option")
            elif cmd == "3":
                (option_type, option_name) = CustomizedPizzaView.remove_option()
                rm_res = self.__customized_pizza_mgt.remove_option(option_type, option_name)
                GenerialView.process_operation_res(rm_res, "Remove option")
            elif cmd == "4":
                CustomizedPizzaView.print_pizza_options(OptionType.bases, self.__customized_pizza_mgt.get_bases())
            elif cmd == "5":
                CustomizedPizzaView.print_pizza_options(OptionType.sauses, self.__customized_pizza_mgt.get_sauses())
            elif cmd == "6":
                CustomizedPizzaView.print_pizza_options(OptionType.toppings, self.__customized_pizza_mgt.get_toppings())
            elif cmd == "7":
                CustomizedPizzaView.print_pizza_options(OptionType.add_ingredients, self.__customized_pizza_mgt.get_add_ingredients())
            elif cmd == "8":
                CustomizedPizzaView.print_all_pizza_options(self.__customized_pizza_mgt.to_json())
            elif cmd == "0":
                break
            else:
                print("Invalid command!")

    def process_side_dish_menu(self) -> None:
        while True:
            self.show_side_dish_menu()
            cmd = input("Enter command: ")
            if cmd == "1":
                sidedish = SideDishView.add_side_dish()
                add_res = self.__side_dish_mgt.add_side_dish(sidedish)
                GenerialView.process_operation_res(add_res, "Add side dish")

            elif cmd == "2":
                (side_dish_name, new_data) = SideDishView.update_side_dish()
                update_res = self.__side_dish_mgt.update_side_dish(side_dish_name, new_data)
                GenerialView.process_operation_res(update_res, "Update side dish")

            elif cmd == "3":
                rm_side_dish_name = input("Enter the side dish name you want to remove: ")
                rm_res = self.__side_dish_mgt.rm_side_dish(rm_side_dish_name)
                GenerialView.process_operation_res(rm_res, "Remove side dish")

            elif cmd == "4":
                side_dish_type = SideDishView.get_side_dish_type()
                side_dishes = self.__side_dish_mgt.get_side_dish_by_type(side_dish_type)
                if len(side_dishes) > 0:
                    for side_dish in side_dishes:
                        print(side_dish.to_json())
                else:
                    print("Side dish not found!")
            elif cmd == "5":
                SideDishView.print_side_dishes(self.__side_dish_mgt.get_all_side_dishes())
            elif cmd == "0":
                break
            else:
                print("Invalid command!")

    def process_order_menu(self) -> None:

        while True:
            self.show_order_menu()
            cmd = input("Enter command: ")
            if cmd == "1":
                menus = self.__menu_mgt.get_menus()
                customized = self.__customized_pizza_mgt.to_json()
                side_dishes = self.__side_dish_mgt.get_all_side_dishes()
                order_data = OrderView.place_order(menus, customized, side_dishes)
                add_res = self.__order_mgt.add_order(order_data)
                GenerialView.process_operation_res(add_res, "Add order")

            elif cmd == "2":
                order_ids = self.__order_mgt.get_order_ids()
                order_id = OrderView.get_order_id(order_ids)
                if order_id=='' or order_id is None:
                    print("Order not found!")
                    continue
                order = self.__order_mgt.get_order_by_id(int(order_id))
                if order is not None:
                    OrderView.display_order(order)
                else:
                    print("Order not found!")
            elif cmd == "3":
                order_ids = self.__order_mgt.get_order_ids()
                order_id = OrderView.get_order_id(order_ids)
                recipes = self.__recipe_mgt.get_recipes()
                kitchen_str = self.__order_mgt.get_orders_for_kitchen(recipes, order_id)
                if kitchen_str == '':
                    print("Order not found!")
                print(kitchen_str)
            elif cmd == "0":
                break
            else:
                print("Invalid command!")
def main_menu():
    pizza_store = PizzaStore()
    while True:
        print("1. Recipe Management")
        print("2. Inventory Management")
        print("3. Menu Management")
        print("4. Customized Pizza Menu Management")
        print("5. Side Dish Management")
        print("6. Order Management")
        print("0. Exit")
        cmd = input("Enter command: ")
        if cmd == "1":
            pizza_store.process_recipe_menu()
        elif cmd == "2":
            pizza_store.process_inventory_menu()
        elif cmd == "3":
            pizza_store.process_menu_menu()
        elif cmd == "4":
            pizza_store.process_customized_pizza_menu()
        elif cmd == "5":
            pizza_store.process_side_dish_menu()
        elif cmd == "6":
            pizza_store.process_order_menu()
        elif cmd == "0":
            print("Bye~")
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main_menu()