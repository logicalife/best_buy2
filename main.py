import sys
import products
import store

product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
              ]


def start(store_name):
    """This function shows available tasks to perform for gthe store and acts as
       per user input"""
    while True:
      print(""" \n   Store Menu
   ------------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit""")
      try:
        user_choice = int(input("Please choose a number:"))
      except ValueError:
        print("Error with your choice! Try again!")
        continue
      if user_choice == 1:
        print("------")
        for i,item in enumerate(store_name.get_all_products(),start=1):
          print(f'{i}. {item.show()}')
        print("------")
      if user_choice == 2:
        print(f'Total of {store_name.get_total_quantity()} items in store')
      if user_choice == 3:
        active_products = store_name.get_all_products()
        shopping_list = []
        print("------")
        for i,item in enumerate(store_name.get_all_products(),start=1):
          print(f'{i}. {item.show()}')
        print("------")
        print("When you want to finish order, enter empty text.")
        while True:
          product = input("\nWhich product # do you want?")
          quantity = input("What amount do you want?")
          if product =="" or quantity == "":
            if len(shopping_list) == 0:
              break
            print(f'Order made! Total payment: {store_name.order(shopping_list)}')
            break
          try:
            item_and_quantity = [active_products[int(product)-1],int(quantity)]
            if active_products[int(product)-1].get_quantity() < int(quantity):
              print("Error while making order! Quantity larger than what exists")
              continue
            shopping_list.append(tuple(item_and_quantity))
            print("Product added to list!")
          except:
            print("Error adding product!")
      if user_choice == 4:
        sys.exit()


def main():
    try:
        best_buy = store.Store(product_list)
    except:
        print("Error in product data")
    start(best_buy)


if __name__ == "__main__":
    main()
