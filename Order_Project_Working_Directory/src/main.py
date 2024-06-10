
from ui.Order_mgt_UI import Order_mgt_UI
from ui.All_Products_UI import All_Products_UI
from order_app_logic_pkg.Postal_Order import Postal_Order



while True:
    try:
        n = int(input("""Enter number: 
            1 - add new product
            2 - update product
            3 - make an order 
            4 - update an order
            5 - display all products
            6 - save postal order
            7 - exit\n"""))
        # o_ui=Order_mgt_UI()
        # all_products = All_Products_UI()
        if n == 1: 
            print('add product')
            all_products = All_Products_UI()
            all_products.input_a_product()
        elif n == 2: 
            print('update product')
            all_products = All_Products_UI()
            is_updated =all_products.update_a_product()

        elif n == 3:
            print('make an order')
            o_ui=Order_mgt_UI()
            o_ui.create_order()
            for order in o_ui.orders:
                print(str(order))
        elif n == 4:
            print('update an order')
            o_ui=Order_mgt_UI()
    
            update_order = o_ui.update_an_order()

        elif n == 5:
            print('display all products')
            all_products = All_Products_UI()
            display_products1 =all_products.display_products()
            
        
        elif n == 6:
            print('Handle postal order')
            try:
                postal_order = Postal_Order.create_from_input()
                postal_order.save()
            except Exception as e:
                print(f"Error occurred: {e}")
        elif n == 7:
            break
    except ValueError as e:
        print('Value error: try again')


# try:
#     all_products = All_Products_UI()
#     all_products.input_a_product()

#     is_updated =all_products.update_a_product()
#     #print(is_updated)
# except Exception as e:
#      raise Exception('Promlem here: ', e)


# try:
#     o_ui=Order_mgt_UI()
#     for order in o_ui.orders:
#                 print(str(order))
# except Exception as e:
#      raise Exception('Promlem here: ', e)




         
# #Remove an item
# #order.remove_item(item1)
# #order.display_order()


# password = input("Enter your password ")

# password_len =len(password)

# index=0
# invalid = False

# if password_len>2:
#     while  (index < password_len) and not invalid:
#         a= password[index]
#         if index % 3 ==0:
#             if a not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
#                 invalid=True
#         elif index % 3 == 1:
#             if a not in "0123456789":
#                 invalid=True
#         elif index % 3 == 2:
#             if a not in "#_@-!":
#                 invalid =True
#         index = index + 1
#         if invalid:
#             print ("Invalid password")
#     if index==password_len and not invalid:
#         print ("Valid password")
# else:
#     print ("Invalid password")   

