import os
import sys
from order_app_logic_pkg.Order import Order
#from order_app_logic_pkg.Customer import Customer
import order_app_logic_pkg.Customer as Customer
import order_app_logic_pkg.Order as Order
import traceback
sys.path.append("../..")


#from src.order_app_logic_pkg.Order import Order



class Order_DB:
    file_path ='.'+os.sep+'assets'+os.sep+'data_files'+os.sep
    #file_path = "\assets\data_files\ "
    file_name = 'orders.txt'
    all_orders = []
    rec_length = 70


    header_template = '{:12},{:8},{:5}\n'
    customer_template = '{:10},{:25},{:30}\n'
    item_template = '{:50},{:10.2f},{:5d}\n'
    def __init__(self, order:Order=None, customer:Customer=None):
        if order:
            self.order = order
            self.customer=customer
        else:
            self.order = {
               'order_id': '',
               'order_date': '',
               'customer_id': '',
               'customer_name': '',
               'customer_email': '',
               'order_items': []
            }
        
    # def save(self):
    #     try:
    #         # Create file if not created already
    #         if not os.path.isfile(Order_DB.file_path + Order_DB.file_name):
    #             f = open(Order_DB.file_path + Order_DB.file_name, 'x')
    #             f.close()
    #         print('file created')
    #         # Open the file in append mode
    #         print(self.order.order_id)
    #         f = open(Order_DB.file_path + Order_DB.file_name, "a")
    #         f.write(Order_DB.header_template.format(self.order.order_id,self.order.order_date,len(self.order.items)))
    #         f.write(Order_DB.customer_template.format(self.customer.cust_id,self.customer.customer_name,self.customer.customer_email))
    #         f.write(Order_DB.item_template.format(self.order.item_name,self.order.item_unit_price,self.order.cust_item_qty))
    #     except Exception as e:
    #         print(f"An error occurred while saving the order: {str(e)}")
    def read_orders(self):
        try:
            with open(Order_DB.file_path + Order_DB.file_name, "r") as f:
                # f.seek(offset, 1)
                # s = f.read(bytes)
                # tokens = s.split(',')
                # if len(tokens) >= 3 and tokens[0].strip().startswith('Order'):
                #     order_id = tokens[0].strip()
                #     order_number = tokens[1].strip()
                #     quantity = int(tokens[2].strip())
                #     return Order(order_id, float(order_number), quantity)
                # else:
                #     return None  # Handle the case where the data doesn't match expected format

                #order = Order()
                order_id = ''
                order_number = 0
                quantity = 0
                for line in f:
                    tokens = line.split(',')

                    if len(tokens) >= 3 and tokens[0].strip().startswith('Order'):
                        order_id = tokens[0].strip()
                        order_number = int(tokens[1].strip())
                        quantity = int(tokens[2].strip())

                    elif len(tokens) >= 3 and tokens[0].strip().startswith('Cust'):
                        cust_id = tokens[0].strip()
                        cust_name = tokens[1].strip()
                        cust_email = tokens[2].strip()

                        customer = Customer.Customer(cust_name, cust_email)
                        customer.cust_id = cust_id[10:]

                        order = Order.Order(customer)
                        order.order_id = order_id[7:]
                        order.order_num = order_number

                        self.all_orders.append(order)
                        
            
        except Exception as e:
            print(traceback.format_exc())
            print("Orders file read error", e)
            return None



    def read_all_orders(self):
        if not os.path.isfile(Order_DB.file_path+ Order_DB.file_name):       
            f = open(Order_DB.file_path+ Order_DB.file_name, 'x')
            f.close()
        self.all_orders.clear()
        offset=0
        done = False
        #to get the size of the file in bytes
        statinfo = os.stat(Order_DB.file_path+ Order_DB.file_name)
        #print(statinfo.st_size)

        # while offset <statinfo.st_size:
        #     try:
        #         order = Order_DB.read_order(offset,bytes=Order_DB.rec_length)
        #         self.all_orders.append(order)
        #         offset=offset+1+70
        #     except Exception as e: #When end of file is encountered, StopIteration exception is raised.
        #         print("Error while reading all recs in orders.txt")
        self.read_orders()

    def update_this_order_in_file(self)->bool:
        offset=0
        is_updated = False
        #to get the size of the file in bytes
        statinfo = os.stat(Order_DB.file_path+ Order_DB.file_name)
        try:
            f=open(Order_DB.file_path+ Order_DB.file_name, "r+")
            #print(statinfo.st_size)
            # while offset <statinfo.st_size and not is_updated:
            #         s= f.read(Order_DB.rec_length)
            #         tokens = s.split(',')
            #         tokens[0]=tokens[0].strip() #name
            #         tokens[1]=tokens[1].strip() #unit price
            #         tokens[2]=tokens[2].strip() #quantity
            #         rec_in_file=Order_DB(tokens[0],float(tokens[1]), int(tokens[2]))
            #         if rec_in_file.name == self.name:                    
            #             f.seek(offset,0)
            #             f.write(Order_DB.header_template.format(self.order.order_id, self.order.order_date, len(self.order.items)))

            #             f.close()                    
            #             is_updated = True
            #         offset=offset+1+Order_DB.rec_length
            
            lines = f.readlines()
            f.close()
            for i in range(len(lines)):
                if lines[i].startswith(self.order.order_id):
                    lines[i] = Order_DB.header_template.format(self.order.order_id, self.order.order_date, len(self.order.items))
            out = open(Order_DB.file_path+ Order_DB.file_name, 'w')
            out.writelines(lines)
            out.close()
            # for line in f:
            #     tokens = line.split(',')

            #     if self.order.order_id == tokens[0].strip():
            #         f.write(Order_DB.header_template.format(self.order.order_id, self.order.order_date, len(self.order.items)))
            #         f.close()
            #         break


                    
        except StopIteration: #When end of file is encountered, StopIteration exception is raised.
            print("File handling error while updating a record in product.txt")
        return is_updated

    def save(self):
        try:
            if not os.path.isfile(Order_DB.file_path + Order_DB.file_name):
                with open(Order_DB.file_path + Order_DB.file_name, 'x') as f:
                    pass  # Just to create the file if it doesn't exist
            with open(Order_DB.file_path + Order_DB.file_name, 'a') as f:
                f.write(Order_DB.header_template.format(self.order.order_id, self.order.order_date, len(self.order.items)))
                if self.customer:
                    f.write(Order_DB.customer_template.format(self.customer.cust_id, self.customer.customer_name, self.customer.customer_email))
                else:
                    print("Warning: No customer information available.")
                # Add additional writes for items etc.
        except Exception as e:
            print(f"An error occurred while saving the order: {str(e)}")

            '''2b
        self.order_id=str(Order.order_num)
        self.customer = customer
        self.order_date= datetime.now()
        self.items = []  # Initialize an empty list to store order items


                ))'''

            f.close()
        except Exception as e:
            raise Exception(e)
           # print("Error: " + str(e))
    def __str__(self):
        return f"Order ID: {self.order['order_id']}, Customer: {self.customer['customer_name']}"
    
