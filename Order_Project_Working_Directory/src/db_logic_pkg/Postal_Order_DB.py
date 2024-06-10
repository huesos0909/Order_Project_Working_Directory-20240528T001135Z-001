# import os
# import sys
# sys.path.append("../..")
# from datetime import datetime
# from Order_DB import Order_DB

# class Postal_Order_DB(Order_DB):
#     postal_file_name = 'postal_orders.txt'

#     def save(self):
#         super().save()  # Call the save method from Order_DB to handle the order part

#         # Handle the postal order specifics
#         try:
#             postal_path = Order_DB.file_path + Postal_Order_DB.postal_file_name
#             # Create file if not created already
#             if not os.path.isfile(postal_path):
#                 with open(postal_path, 'x') as f:
#                     pass

#             with open(postal_path, "a") as f:

#                 tracking_info = f"{self.order['order_id']},{datetime.now().strftime('%d%m%Y')},Initiated->Packed->Shipped->Delivered\n"
#                 f.write(tracking_info)      
#         except Exception as e:
#             print("Error in saving postal order: " + str(e))

#     @staticmethod
#     def read_order():
#         # Implementation for reading a postal order
#         pass

#     def update_this_order_in_file(self):
#         # Implementation for updating a postal order in file
#         pass

#     def __str__(self):
#         # Extend the string representation to include postal order details if needed
#         base_str = super().__str__()
#         return base_str + ", Status: Delivered"
from re import template
import sys
import os
from datetime import datetime

class Postal_Order_DB:
     # Define the paths for storing postal order data
    file_path ='.'+os.sep+'assets'+os.sep+'data_files'+os.sep
    file_name = 'postal_orders.txt'
    sys.path.append("../..")    
    @staticmethod
    def save(postal_order):
        # Check if the base path exists and create if not
        base_path = os.path.dirname(Postal_Order_DB.file_path)
        if not os.path.exists(base_path):
            os.makedirs(base_path)

        # Open the file to append data, create if it doesn't exist
        with open(Postal_Order_DB.file_path, 'a') as f:
            # Format the data as per the new specification
            offset_value = f"{postal_order.offset:<15}"  # Offset value needs to be defined in your postal_order instance
            delivery_date_str = postal_order.delivery_date.strftime("%d%m%Y")  # Formatted as DDMMYYYY
            states_sequence = "-".join(postal_order.states).ljust(40)  # Padded or truncated to 40 characters

            # Combine all parts into one formatted record
            template1 = f"{offset_value}{delivery_date_str}{states_sequence}\n"

            # Write the formatted record to the file
            f.write(template1)

            print("Postal order saved successfully.")

    @staticmethod
    def read():
        # Read postal orders from postal_orders.txt
        with open(Postal_Order_DB.postal_orders_file_path, "r") as postal_file:
            for line in postal_file:
                fields = line.split()
                order_id = fields[0].strip()
                delivery_date = datetime.strptime(fields[1], "%d%m%Y")
                states = fields[2].split("->")
                # Construct and return a Postal_Order object
                # Note: This requires further context on how Postal_Order objects are constructed
                print(f"Order ID: {order_id}, Delivery Date: {delivery_date}, States: {states}")

# Usage Example:
# postal_order = Postal_Order(...)
# Postal_Order_DB.save(postal_order)
# Postal_Order_DB.read()
