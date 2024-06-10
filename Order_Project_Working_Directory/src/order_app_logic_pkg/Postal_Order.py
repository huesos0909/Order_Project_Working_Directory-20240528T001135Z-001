
from .Order import Order
from .Customer import Customer

# from datetime import datetime,timedelta


# class Postal_Order(Order):
#     VALID_STATES = ["Initiated", "Packed", "Shipped", "Delivered"]
#     def __init__(self, customer:Customer):
#         super().__init__(customer)
#         one_month_from_now=(datetime.now()+timedelta(days=30))#one month from now
#         #i was testing it for an error, so I used the try/except. Can delete.
#         try:
#             self.o_delivery_date=one_month_from_now
#         except AttributeError:
#             print("Postal Order: Delivery date not set")   

#         self.past_states=[] #not a property
#         self.current_state=0#current state is, "initiated", among past states
    
#     @property
#     def o_delivery_date(self)->datetime:
#         return self._o_delivery_date

#     @o_delivery_date.setter
#     def o_delivery_date(self, d_date: datetime):
#         current_date = datetime.now()
#         new_date = current_date + timedelta(days=30)
#         # delivery date should be within 1 month from now
#         if new_date >= d_date >= current_date:
#             self._o_delivery_date = d_date

#     @property
#     def current_state(self)->type[int]:
#         return self._current_state

#     @current_state.setter
#     def current_state(self, new_state:type[int]):
#         if Postal_Order.VALID_STATES[new_state] in Postal_Order.VALID_STATES:
#             self.past_states.append(new_state)#add new_state, assuming it is valid
#             if self.has_partial_valid_state_sequence(self.past_states,Postal_Order.VALID_STATES):
#                 self._current_state=new_state
#             else:
#                 self.lower_the_status_by_a_level()#not valid, so  undo new_state


#     #Returns true if the 'states' parameter has a set of valid states. Returns False otherwise
#     #Parameter valid_sequence has values ["Initiated", "Packed", "Shipped", "Delivered"]
#     #A postal oders's valid partial state sequence can only have the following form:
#     #[]
#     #["initiated"],
#     #["Initiated", "Packed"]
#     #["Initiated", "Packed", "Shipped"],
#     #["Initiated", "Packed", "Shipped", "Delivered"]
#     def has_partial_valid_state_sequence(self,states:type[list[int]], valid_sequence:list[type[str]])->type[bool]:
#         result=False
#         if len(states)<=len(valid_sequence):
#             in_valid_seq=True
#             for i, state in enumerate(states):
#                 if state>=len(Postal_Order.VALID_STATES):
#                     in_valid_seq= False
#                     break
#                 if valid_sequence[state-i] != valid_sequence[0]:
#                     in_valid_seq= False
#                     break
#                 else:
#                     valid_sequence = valid_sequence[1:]  # Remove the matched state
#             if in_valid_seq:
#                 result=True
#         return result
#     #useful if the order status was wrongly raised
#     def lower_the_status_by_a_level(self):
#         self.past_states=self.past_states.pop()#remove last
    
#     #useful if the order status was wrongly lowered 
#     def raise_the_status_by_a_level(self):
#         if len(self.past_states)<len(Postal_Order.VALID_STATES):
#             self.past_states=len(self.past_states)

#     '''
#     @property
#     def past_states(self):
#         return self.past_states
        
#     '''
#     def __str__(self)->type[str]:
        
#         states =Postal_Order.VALID_STATES[:len(self.past_states)]
#         star_line = "-"*100+"\n"
#         postal_order_header_details="Additional details for Postal Order\n"+ \
#             f"Delivery date:{self.o_delivery_date}\n" +"Postal Order states:"  + \
#                 " ".join(map(str,states))+"\n"
#         base_order_details=super().__str__()    
#         return (base_order_details+star_line+postal_order_header_details+star_line)
        
import os
from datetime import datetime

class Postal_Order(Order):
    VALID_STATES = ["Initiated", "Packed", "Shipped", "Delivered"]

    def __init__(self, customer: Customer):
        super().__init__(customer)
        self.states = []

    @classmethod
    def create_from_input(cls):
        customer_name = input("Enter customer name: ")
        customer_email = input("Enter customer email: ")
        customer = Customer(customer_name, customer_email)
        postal_order = cls(customer)

        order_id = input("Enter order ID: ")
        postal_order.order_id = order_id

        delivery_date = input("Enter delivery date (yyyy-mm-dd): ")
        postal_order.delivery_date = datetime.strptime(delivery_date, "%Y-%m-%d")

        postal_order.states = ["Initiated", "Packed", "Shipped", "Delivered"]  # Default flow
        return postal_order

    def save(self):
        base_path = "path_to_orders"
        if not os.path.exists(base_path):
            os.makedirs(base_path)  # Create the directory if it does not exist
        file_path = os.path.join(base_path, "postal_orders.txt")
        
        with open(file_path, "a") as f:
            delivery_date_str = self.delivery_date.strftime("%Y%m%d")
            states_sequence = "-".join(self.states)
            record = f"{self.order_id:<15}{delivery_date_str:<8}{states_sequence}\n"
            f.write(record)
        print("Postal order saved successfully.")
