from os import path


def get_path(filename) -> str:
    cur_path: str = path.abspath(__file__)
    return path.join(path.dirname(cur_path), filename)

RECIPE_FILEPATH = get_path('json_recipe.json')
INGREDIENT_FILEPATH = get_path('json_ingredient.json')
MENU_FILEPATH = get_path('json_menu.json')
CUSTOMIZED_PIZZA_FILEPATH = get_path('json_customized_pizza.json')
SIDE_DISH_FILEPATH = get_path('json_side_dish.json')
ORDER_FILEPATH = get_path('json_order.json')


# customized_pizza_default
DEFAULT_PIZZA_BASES = [{'name': 'Thin', 'price': 1.00, 'quantity': 0},
                       {'name': 'Thick', 'price': 2.00, 'quantity': 0}]


DEFAULT_PIZZA_SAUCES = [{'name': 'Tomato', 'price': 1.00, 'quantity': 0},
                        {'name': 'BBQ', 'price': 1.00, 'quantity': 0},
                        {'name': 'Garlic', 'price': 1.00, 'quantity': 0}]


DEFAULT_PIZZA_TOPPINGS = [{'name': 'Pepperoni', 'price': 1.00, 'quantity': 0},
                          {'name': 'Ham', 'price': 1.00, 'quantity': 0},
                          {'name': 'Bacon', 'price': 1.00, 'quantity': 0},
                          {'name': 'Mushrooms', 'price': 1.00, 'quantity': 0},
                          {'name': 'Onion', 'price': 1.00, 'quantity': 0},
                          {'name': 'Black_olives', 'price': 1.00, 'quantity': 0},
                          {'name': 'Tomato_slices', 'price': 1.00, 'quantity': 0},
                          {'name': 'Pineapple', 'price': 1.00, 'quantity': 0}]

DEFAULT_ADD_INGREDIENTS = [{'name': 'Extra_cheese', 'price': 1.00, 'quantity': 0},
                           {'name': 'Extra_meat', 'price': 1.00, 'quantity': 0},
                           {'name': 'Extra_veggies', 'price': 1.00, 'quantity': 0}]




# {
#     "bases": [
#         {"name": "Thin", "price": 1.00, "quantity": 0},
#         {"name": "Thick", "price": 1.00, "quantity": 0}
#     ],
#     "sauses": [
#         {"name": "Tomato", "price": 1.00, "quantity": 0},
#         {"name": "BBQ", "price": 1.00, "quantity": 0},
#         {"name": "Garlic", "price": 1.00, "quantity": 0}
#     ],
#     "toppings": [
#         {
#             "name": "Pepperoni",
#             "price": 1.0,
#             "quantity": 0
#         },
#         {
#             "name": "Ham",
#             "price": 1.0,
#             "quantity": 0
#         },
#         {
#             "name": "Bacon",
#             "price": 1.0,
#             "quantity": 0
#         },
#         {
#             "name": "Mushrooms",
#             "price": 1.0,
#             "quantity": 0
#         },
#         {
#             "name": "Onion",
#             "price": 1.0,
#             "quantity": 0
#         },
#         {
#             "name": "Black_olives",
#             "price": 1.0,
#             "quantity": 0
#         },
#         {
#             "name": "Tomato_slices",
#             "price": 1.0,
#             "quantity": 0
#         },
#         {
#             "name": "Pineapple",
#             "price": 1.0,
#             "quantity": 0
#         }
#     ],

#     "add_ingredients": [
#         {
#             "name": "Extra_cheese",
#             "price": 1.0,
#             "quantity": 0
#         },
#         {
#             "name": "Extra_meat",
#             "price": 1.0,
#             "quantity": 0
#         },
#         {
#             "name": "Extra_veggies",
#             "price": 1.0,
#             "quantity": 0
#         }
#     ]
# }