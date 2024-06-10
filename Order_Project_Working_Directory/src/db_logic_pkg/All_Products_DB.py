from db_logic_pkg.Product_DB import Product_DB
import os
class All_Products_DB():
    def __init__(self):
        self.all_products=[]
        self.read_all_products()
    
    #append new product to file 
    def save_new_product(self, product:Product_DB)->bool:
        is_valid=True
        for p in self.all_products:
            if p.name == Product_DB.name:
                is_valid=False
                break
        if is_valid:
            self.all_products.append(product)
            product.save()
        return is_valid
    
    def read_all_products(self):
        if not os.path.isfile(Product_DB.file_path+ Product_DB.file_name):       
            f = open(Product_DB.file_path+ Product_DB.file_name, 'x')
            f.close()
        self.all_products.clear() 
        offset=0
        done = False
        #to get the size of the file in bytes
        statinfo = os.stat(Product_DB.file_path+ Product_DB.file_name)
        #print(statinfo.st_size)

        while offset <statinfo.st_size:
            try:
                product = Product_DB.read_product(offset,bytes=Product_DB.rec_length)
                self.all_products.append(product)
                offset=offset+1+Product_DB.rec_length
            except Exception as e: #When end of file is encountered, StopIteration exception is raised.
                print("Error while reading all recs in product.txt")

    #overwrite the file with the data in all_products 
    def save_all_products(self):
        if os.path.exists(Product_DB.file_path+ Product_DB.file_name):
            os.remove(Product_DB.file_path+ Product_DB.file_name)        
        for rec in self.all_products:
            rec.save()


    
    
    def __str__(self)->type[str]:
        star_line = "\n"+"-"*100+"\n"
        product_details="Available products details are:\n"
        for rec in self.all_products:
            product_details += str(rec)
        return (star_line+product_details+star_line)

'''
all_recs = All_Products_DB()
all_recs.read_all_products()
for rec in all_recs.all_products:
    print (rec.name)'''