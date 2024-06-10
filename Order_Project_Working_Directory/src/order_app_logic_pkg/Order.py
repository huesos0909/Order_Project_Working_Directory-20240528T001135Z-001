import sys
sys.path.append("../")
from order_app_logic_pkg import Customer, OrderItem

from datetime import date
from datetime import datetime
class Order:
    order_id_base = "Order_"
    order_num =0#ideally should be from a file

    def __init__(self, customer:Customer):
        Order.order_num +=1
        self.order_id=str(int(round(datetime.now().timestamp())))
        self.customer = customer
        self.order_date= datetime.now()
        self.items = []  # Initialize an empty list to store order items

    @property
    def order_id(self)->type[str]:        
        return self._order_id
    
    @order_id.setter
    def order_id(self, order_num:type[int]):
        self._order_id=Order.order_id_base+'_'+order_num
    
    @property
    def order_date(self)->date:
        return self._order_date
    
    @order_date.setter
    def order_date(self,todays_date:datetime):
        self._order_date=date(todays_date.year,todays_date.month,todays_date.day)
    
    def add_item(self, item:OrderItem):
        self.items.append(item)

    def remove_item(self, item:OrderItem)->type[str]:
        result=""
        if item in self.items:
            self.items.remove(item)
            result="Order item was successfully removed"
        else:
           result=f"{item} is not in the order."
        return result

    def calculate_total(self)->type[float]:
        total_price = sum(item.price for item in self.items)
        return total_price
    
    def __str__(self)->type[str]:
        star_line = "-"*100+"\n"
        order_header_details="Order Header\n"+\
            f"Order ID:{self.order_id:20}" +\
                f"Order date:{self.order_date}\n"
        customer_details=str(self.customer)
        item_details="Order items are:\n"+'\n'.join(map(str, self.items))+'\n'
        return (star_line+order_header_details+customer_details+item_details+star_line)





