from additional_data import MENU
from art import logo
import time
pantry = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}


def coffee_machine():
    coffee = ''
    change = 0
    machine_input = ''
    while machine_input != 'off':
        print(logo)
        machine_input = input('What would you like? (espresso/latte/cappuccino):')
        if machine_input == 'report':
            return print(f'Ingredients left {pantry}')
        coffee = machine_input
        if machine_input == 'off':
            return None
        if pantry['water'] < MENU[coffee]['ingredients']['water'] or pantry['milk'] < MENU[coffee]['ingredients']['milk'] or pantry['coffee'] < MENU[coffee]['ingredients']['coffee']:
            return print("I am sorry, we are out of ingredients for your coffee 😔 ")
        price = MENU[coffee]['cost']
        print(f'Your {coffee} costs ${price}, Please enter the coins:\n')
        quarters = int(input('Enter quarters:'))
        dimes = int(input('dimes:'))
        nickles = int(input('Enter nickles:'))
        pennies = int(input('Enter pennies:'))
        total = (quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01)
        if MENU[coffee]['cost'] > total:
            print("Sorry the coins entered aren't enough for the coffee")
            print(f"Please take your coins back, Refunded ${total}")
            return None
        elif MENU[coffee]['cost'] == total:
            pantry['water'] -= MENU[coffee]['ingredients']['water']
            pantry['milk'] -= MENU[coffee]['ingredients']['milk']
            pantry['coffee'] -= MENU[coffee]['ingredients']['coffee']
            pantry['money'] += total
            print('Enjoy your coffee: ☕')
            time.sleep(3)
            print('\n'*100)
        elif MENU[coffee]['cost'] < total:
            change = total-MENU[coffee]['cost']
            pantry['water'] -= MENU[coffee]['ingredients']['water']
            pantry['milk'] -= MENU[coffee]['ingredients']['milk']
            pantry['coffee'] -= MENU[coffee]['ingredients']['coffee']
            pantry['money'] += total
            print(f"Please take your change : 🪙{change}")
            print('Enjoy your coffee: ☕')
            time.sleep(3)
            print('\n' * 100)



coffee_machine()

