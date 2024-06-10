from date import datetime
from order_app_logic_pkg import Customer
from order_app_logic_pkg import Postal_Order
class PostalOrderUI:
    def create_postal_order(self):
        # Collect order details from user
        customer_name = input("Enter customer name: ")
        customer_email = input("Enter customer email: ")
        delivery_date = input("Enter delivery date (dd/mm/yyyy): ")
        delivery_date = datetime.strptime(delivery_date, "%d/%m/%Y")

        # Create the Postal_Order object
        customer = Customer(customer_name, customer_email)
        postal_order = Postal_Order(customer)
        postal_order.delivery_date = delivery_date

        # Assume state management is handled internally or via specific prompts
        return postal_order
