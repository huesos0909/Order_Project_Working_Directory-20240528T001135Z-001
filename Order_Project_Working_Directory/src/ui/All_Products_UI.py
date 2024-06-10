from db_logic_pkg.All_Products_DB import All_Products_DB
from db_logic_pkg.Product_DB import Product_DB

class All_Products_UI:
    def __init__(self):
        self.all_products_db= All_Products_DB()

    #appends a new product to the products.txt file
    def input_a_product(self):
        name = input("Enter name of a product: ")
        while True:
            try:
                unit_price=float(input("Enter the unit price: "))
                break
            except Exception as e:
                print('Invalid input: unit price must be decimal')
        while True:
            try:
                stock_count = int(input("Enter the stock count: "))
                break
            except Exception as e:
                print('Invalid input: stock count must be integer')
        p = Product_DB(name,unit_price,stock_count)
        self.all_products_db.save_new_product(p)
            
    def display_products(self):
        for product in self.all_products_db.all_products:
            print(f'Name: {product.name}, unit price: {product.unit_price}')

        #print(self.all_products_db.all_products) #TODO: add a method here
    '''
    def update_a_product(self)->bool:
        is_updated=False
        if len(self.all_products_db.all_products)>0:
            print("The following products exist: ")
            self.display_products()
            name = input("Enter the name of the product to update: ")
            for p in self.all_products_db.all_products:
                if name == p.name:
                    print("The current details are: ")
                    print (str(p))                    
                    is_change=input("Do you want to change the unit_price(Y/N)? ")
                    is_change=is_change.lower()
                    if is_change =='y':
                        p.unit_price = float(input("Enter new unitprice: "))
                    is_change=input("Do you want to change the stock count(Y/N)? ")
                    is_change=is_change.lower()
                    if is_change =='y':
                        p.stock_quantity = int(input("Enter new stock count: "))
                    p.update_this_product_in_file()
                    is_updated=True
                    break              

        else:
            print("No existing product")
        return is_updated
'''

    def update_a_product(self) -> bool:
        is_updated = False
        if len(self.all_products_db.all_products) > 0:
            print("The following products exist: ")
            self.display_products()
            name = input("Enter the name of the product to update: ")
        for p in self.all_products_db.all_products:
            if name == p.name:
                print("The current details are: ")
                print(str(p))
                try:
                    change_price = input("Do you want to change the unit price (Y/N)? ").strip().lower()
                    if change_price not in ['y', 'n']:
                        raise ValueError("Please type 'Y' for yes or 'N' for no.")
                    if change_price == 'y':
                        while True:
                            try:
                                p.unit_price = float(input("Enter new unit price: "))
                                break
                            except Exception as e:
                                print("Please use only numbers for the unit price.")

                    change_stock = input("Do you want to change the stock count (Y/N)? ").strip().lower()
                    if change_stock not in ['y', 'n']:
                        raise ValueError("Please type 'Y' for yes or 'N' for no.")
                    if change_stock == 'y':
                        while True:
                            try:
                                p.stock_quantity = int(input("Enter new stock count: "))
                                break
                            except Exception as e:
                                print("Please use only numbers for the stock count.")

                    p.update_this_product_in_file()
                    is_updated = True
                    break
                except ValueError as e:
                    print(e)
                    continue
        else:
            print("No existing product")
        return is_updated