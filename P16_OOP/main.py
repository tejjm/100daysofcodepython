
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time
cf = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
user_input = ''
while user_input != False:
    user_input =input(f"Welcome to Teju Coffee, What would you like? \n{menu.get_items()}\n")
    if user_input == "report":
        cf.report()
        money.report()
        time.sleep(2)
        print("\n" * 60)
    elif user_input == "off":
        user_input = False
    else:
        order = menu.find_drink(user_input)
        if cf.is_resource_sufficient(order):
            if money.make_payment(order.cost):
                cf.make_coffee(order)
                time.sleep(2)
                print("\n" * 60)



