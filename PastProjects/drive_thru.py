menu = ['🍔 Cheeseburger', '🍟 Fries', '🥤 Soda', '🍦 Ice Cream', '🍪 Cookie']

def welcome(menu):
  print('Hello! Welcome to McDonalds!')
  print('Here is our menu: ')
  for i in menu:
    print(i)
  print('What would you like to order?')


def get_item(menu):
  while True:
    order = input("Enter item nubmer: ")
    if order.isdigit():
      order = int(order)
      if 0 <= order < len(menu):
        return menu[order - 1]
    print('Invalid choice. Please try again.')

def main():
  welcome(menu)
  print('You ordered: ', get_item(menu))

main()
