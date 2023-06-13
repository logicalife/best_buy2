import sys
import products
import store
import promotions

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)


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
                product_num = input("\nWhich product # do you want?")
                quantity = input("What amount do you want?")
                if product_num =="" or quantity == "":
                    if len(shopping_list) == 0:
                        break
                    print(f'\nOrder made! Total payment: {store_name.order(shopping_list)}')
                    break
                product_name = active_products[int(product_num) - 1]
                try:
                    item_and_quantity = [product_name,int(quantity)]
                    if str(type(product_name)) == "<class 'products.Product'>" and \
                            int(quantity) > product_name.get_quantity():
                        print("Error while making order! Quantity larger than what exists")
                        continue
                    if str(type(product_name)) == "<class 'products.LimitedProduct'>":
                        if int(quantity) > product_name.maximum or \
                                sum([item[1] for item in shopping_list if item[0] == product_name]) >= product_name.maximum:
                            print(f"Error while making order! Only {product_name.maximum} is allowed per order")
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
