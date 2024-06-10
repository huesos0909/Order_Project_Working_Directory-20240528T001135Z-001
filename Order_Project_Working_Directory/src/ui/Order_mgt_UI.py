
#import sys



# FROM THE FILE:
'''
sys.path.append("../..")
import os
#from src import order_app_logic_pkg
from src.order_app_logic_pkg.Order import Order
from src.order_app_logic_pkg.OrderItem import OrderItem
from src.order_app_logic_pkg.Customer import Customer
from src.order_app_logic_pkg.Products import Products
from src.order_app_logic_pkg.Postal_Order import Postal_Order
from src.db_logic_pkg.Order_DB import Order_DB
'''
# main:
#import order_app_logic_pkg
from order_app_logic_pkg.Order import Order
from order_app_logic_pkg.OrderItem import OrderItem
from order_app_logic_pkg.Customer import Customer
from order_app_logic_pkg.Products import Products
from order_app_logic_pkg.Postal_Order import Postal_Order
from db_logic_pkg.Order_DB import Order_DB



class Order_mgt_UI:
    # def __init__(self):
    #     self.cust_name=self.get_cust_name()
    #     self.cust_email=self.get_cust_email()
        #testing below: Creation of a regular Order and a Postal Order
        #self.orders=[self.create_postal_order()]   
            
            
        #self.orders=[self.create_postal_order()]

    def __init__(self):
        self.cust_name = self.get_cust_name()
        self.cust_email = self.get_cust_email()
        #self.orders=[self.create_order(),self.create_postal_order()]
        #self.orders=[self.create_order()]
        self.orders = []

    def initialize_customer(self):
        if not self.cust_name:
            self.cust_name = self.get_cust_name()
        if not self.cust_email:
            self.cust_email = self.get_cust_email()

    # existing methods remain unchanged

    def get_cust_name(self)->type[str]:
        done=False
        while not done:
            done=True
            name= input("Enter your name. 3-10 chars. No white space chars allowed: ")
            if len(name) <=3 or len(name)>=10:
                    print("Name should be between 3-10 chars. Try again")
                    done=False
            forbidden = [' ', '\n','\r','\t','\b']
            # Check if any forbidden characters are in the name
            #'any' returns true if any of the forbidden char is in name
            if any(a_char in name for a_char in forbidden):
                    print("You have used white space chars. Try again")
                    done=False
        return name
    
    def get_cust_email(self)->type[str]:
        done=False
        while not done:
            done=True
            email= input("Enter your email. 6-20 chars with an @. No white space chars allowed: ")
            if len(email) <=6 or len(email)>=20:
                    print("Email should be between 6-20 chars. Try again")
                    done=False
            forbidden = [' ', '\n','\r','\t','\b']
            if any(a_char in email for a_char in forbidden):
                    print("You have used white space chars. Try again")
                    done=False
            if email[0]=='@' or email.count('@')!=1:
                print("An in-between @ char expected in email. Try again")
                done=False
        return email
 
    def create_postal_order(self)->Postal_Order:
        a_customer = Customer(self.cust_name,self.cust_email)
        a_postal_order = Postal_Order(a_customer)
        done=False
        while not done:
            done=True
            a_postal_order.add_item(self.create_order_item())
            correct_more=False
            while not correct_more:
                correct_more=True
                more = input("Do you want to order another item Y/N: ")
                more = more.strip()
                if more not in ['Y', 'y','N','n']:
                     print("You did not enter Y or N. Please try again")
                     correct_more=False
            if more in ['Y','y']:
                 done=False
        return a_postal_order
    #class OrderManagement:


    def create_order(self)->Order:

        a_customer = Customer(self.cust_name,self.cust_email)
        an_order = Order(a_customer)
        print(f'Customer id: {an_order.customer.cust_id}')
        done=False
        while not done:
            done=True
            an_order.add_item(self.create_order_item())
            correct_more=False
            while not correct_more:
                correct_more=True
                more = input("Do you want to order another item Y/N: ")
                more = more.strip()
                if more not in ['Y', 'y','N','n']:
                     print("You did not enter Y or N. Please try again")
                     correct_more=False
            if more in ['Y','y']:
                done=False
            if more.lower() == 'n':
                correct_more = True
        # while not done:
        #     an_order.add_item(self.create_order_item())
        #     correct_more = False
        # while not correct_more:
        #     more = input("Do you want to order another item Y/N: ").strip().lower()  # Normalize the input
        #     if more not in ['y', 'n']:
        #         print("You did not enter Y or N. Please try again")
        # else:
        #     correct_more = True
        #     if more == 'n':
        #         return an_order  # Set done to True to break the outer loop

        #need to add code here to save the order via an Order_DB object         
        order_db = Order_DB(an_order, a_customer)
        try:
            order_db.save()
            
        except Exception as e:
             raise Exception('Error here: ', e)
        # return an_order


    def create_order_item(self)->OrderItem:
        item_id=None
        item_name=None
        item_unit_price=None
        item_qty=None
        p=Products()
        print(str(p))#Available products
        correct_choice=False
        # item_name = Products.ALL_PRODUCTS[item_id-1]["name"]
        # item_unit_price = Products.ALL_PRODUCTS[item_id-1]["unit_price"]
        while not correct_choice:
            correct_choice=True
            
            choice=int(input("Enter your choice "))
            if choice not in [int(x) for x in range(1, len(Products.ALL_PRODUCTS) +1)]:
                print("Your entry was incorrect. Try again")
                correct_choice=False
        item_id=int(choice)
        item_name=Products.ALL_PRODUCTS[item_id-1].name 
        item_unit_price=Products.ALL_PRODUCTS[item_id-1].unit_price
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity
        correct_qty=False
        while not correct_qty:
            correct_qty=True
            while True:
                try:
                    item_qty=input("Input the quanity. Positive integers only: ")
                    item_qty=int(item_qty)
                    break
                except Exception as e:
                    print("You did not enter an integer. Try again")
                    correct_qty=False
            if item_qty<0:
                print("You did not enter a positive integer. Try again")
                correct_qty=False
            
        anItem = OrderItem(item_name, item_unit_price, item_qty)


        return anItem
    
    def update_an_order(self):
        # order_db = Order_DB.read_order()  # Suppose it reads an existing order
        # print("Current order:", order_db)
        # new_details = input("Enter new details for the order: ")
        # order_db.order['details'] = new_details  # Update the order details
        # order_db.update_this_order_in_file()


        is_updated = False
        order = Order(Customer(self.cust_name, self.cust_email))
        
        name = input("Enter the id of the order to update: ")
        order.order_id = name
        order_db = Order_DB()
        order_db.read_all_orders()

        print(f'all orders: {order_db.all_orders}')
        for order in order_db.all_orders:
            print(order.order_id)
        for p in order_db.all_orders:
            if name == p.order_id:
                print("The current details are: ")
                print(str(p))
                try:
                    # change_items_num = input("Do you want to change the number of items (Y/N)? ").strip().lower()
                    # if change_items_num not in ['y', 'n']:
                    #     raise ValueError("Please type 'Y' for yes or 'N' for no.")
                    # if change_items_num == 'y':
                    #     while True:
                    #         try:
                    #             p.unit_price = float(input("Enter new unit price: "))
                    #             break
                    #         except Exception as e:
                    #             print("Please use only numbers for the unit price.")

                    # change_stock = input("Do you want to change the stock count (Y/N)? ").strip().lower()
                    # if change_stock not in ['y', 'n']:
                    #     raise ValueError("Please type 'Y' for yes or 'N' for no.")
                    # if change_stock == 'y':
                    #     while True:
                    #         try:
                    #             p.stock_quantity = int(input("Enter new stock count: "))
                    #             break
                    #         except Exception as e:
                    #             print("Please use only numbers for the stock count.")

                    a_customer = Customer(self.cust_name,self.cust_email)
                    an_order = Order(a_customer)
                    print(f'Customer id: {an_order.customer.cust_id}')
                    done=False
                    while not done:
                        done=True
                        an_order.add_item(self.create_order_item())
                        correct_more=False
                        while not correct_more:
                            correct_more=True
                            more = input("Do you want to order another item Y/N: ")
                            more = more.strip()
                            if more not in ['Y', 'y','N','n']:
                                print("You did not enter Y or N. Please try again")
                                correct_more=False
                        if more in ['Y','y']:
                            done=False
                        if more.lower() == 'n':
                            correct_more = True
                    # while not done:
                    #     an_order.add_item(self.create_order_item())
                    #     correct_more = False
                    # while not correct_more:
                    #     more = input("Do you want to order another item Y/N: ").strip().lower()  # Normalize the input
                    #     if more not in ['y', 'n']:
                    #         print("You did not enter Y or N. Please try again")
                    # else:
                    #     correct_more = True
                    #     if more == 'n':
                    #         return an_order  # Set done to True to break the outer loop

                    #need to add code here to save the order via an Order_DB object         
                    #order_db = Order_DB(an_order, a_customer)

                    an_order.order_id = p.order_id[7:]
                    order_db.order = an_order
                    order_db.update_this_order_in_file()
                    is_updated = True
                    break
                except ValueError as e:
                    print(e)
                    continue
        else:
            print("No existing order")
        return is_updated
        
           
# def update_an_order(self):
#     is_updated = False
#     order = Order(Customer(self.cust_name, self.cust_email))
    
#     name = input("Enter the id of the order to update: ")
#     order.order_id = name
#     order_db = Order_DB()
#     order_db.read_all_orders()

#     if not order_db.all_orders:  # Check if all_orders is empty or None
#         print("No orders available.")
#         return False

#     print(f'all orders: {order_db.all_orders}')
#     for p in order_db.all_orders:
#         if p and name == p.order_id:  # Check if p is not None and names match
#             print("The current details are: ")
#             print(str(p))
#             try:
#                 # Handling unit price changes
#                 change_price = input("Do you want to change the unit price (Y/N)? ").strip().lower()
#                 if change_price == 'y':
#                     while True:
#                         try:
#                             p.unit_price = float(input("Enter new unit price: "))
#                             break
#                         except ValueError:
#                             print("Please use only numbers for the unit price.")
                
#                 # Handling stock quantity changes
#                 change_stock = input("Do you want to change the stock count (Y/N)? ").strip().lower()
#                 if change_stock == 'y':
#                     while True:
#                         try:
#                             p.stock_quantity = int(input("Enter new stock count: "))
#                             break
#                         except ValueError:
#                             print("Please use only numbers for the stock count.")

#                 p.update_this_product_in_file()
#                 is_updated = True
#                 break
#             except ValueError as e:
#                 print(e)
#                 continue
#     else:
#         print("No existing product")

#     return is_updated

