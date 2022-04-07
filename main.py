


from coffe_machin import CoffeeMaker
from menu import Menu
from money_machin import MoneyMachine
charmander = 'ingresa un nombre'

my_money_machin = MoneyMachine()
my_money_machin.report()

menu = Menu()

coffee_maker = CoffeeMaker()
coffee_maker.report()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'what drink do you want? {options}')

    if is_on == 'off':
        is_on = False
    
    elif choice == 'report':
        coffee_maker.report()
        my_money_machin.report()
    else:
        drink = menu.find_drink(choice)
        coffee_maker.is_resource_sufficient(drink)
        if coffee_maker.is_resource_sufficient(drink) and my_money_machin.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)