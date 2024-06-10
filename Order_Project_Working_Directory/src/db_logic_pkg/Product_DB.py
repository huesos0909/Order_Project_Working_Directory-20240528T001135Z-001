import os
import sys


class Product_DB():
    file_path ='.'+os.sep+'assets'+os.sep+'data_files'+os.sep
    file_name= 'products.txt'
    rec_template='{:50}, {:10.2f}, {:5d}\n'
    rec_length  = 70
    def __init__(self, name, unit_price, stock_quantity):
        self.name = name
        self.unit_price = float(unit_price)
        self.stock_quantity = int(stock_quantity)



        
    @property
    def name(self)->str:
        return self._name
    
    @name.setter
    def name(self, name):
        self._name=name

    #appends a record to the file
    def save(self):
        try:
            #create file if not created already
            print(Product_DB.file_path+ Product_DB.file_name)
            if not os.path.isfile(Product_DB.file_path+ Product_DB.file_name):       
                f = open(Product_DB.file_path+ Product_DB.file_name, 'x')
                f.close()
            #open the file in append mode
            f=open(Product_DB.file_path+ Product_DB.file_name, "a")
            f.write(Product_DB.rec_template.format(self.name,self.unit_price,self.stock_quantity)) 
            f.close()
        except Exception:
            e = sys.exc_info()[0]
            print("File handling error while appending a product rec: "+ str(e) )
    
    
    #reads a record of size equal to 'bytes' from 'offset' location from
    #the beginning of the file
    @staticmethod
    def read_product(offset:int, bytes:int):
        try:
            f=open(Product_DB.file_path+ Product_DB.file_name, "r+")
            print(Product_DB.file_path+ Product_DB.file_name)
            #position file pointer to read from offset bytes from the begining of the file
            f.seek(offset,0)
            s= f.read(bytes)
            tokens = s.split(',')
            print(f'tokens read: {tokens}')
            tokens[0]=tokens[0].strip() #name
            tokens[1]=tokens[1].strip() #unit price
            tokens[2]=tokens[2].strip() #quantity
            product=Product_DB(tokens[0],float(tokens[1]), int(tokens[2]))
            return product
        except ValueError:
            print ("Products file read error")
    
    def update_this_product_in_file(self)->bool:
        offset=0
        is_updated = False
        #to get the size of the file in bytes
        statinfo = os.stat(Product_DB.file_path+ Product_DB.file_name)
        try:
            f=open(Product_DB.file_path+ Product_DB.file_name, "r+")
            #print(statinfo.st_size)
            while offset <statinfo.st_size and not is_updated:
                    s= f.read(Product_DB.rec_length)
                    tokens = s.split(',')
                    tokens[0]=tokens[0].strip() #name
                    tokens[1]=tokens[1].strip() #unit price
                    tokens[2]=tokens[2].strip() #quantity
                    rec_in_file=Product_DB(tokens[0],float(tokens[1]), int(tokens[2]))
                    if rec_in_file.name == self.name:                    
                        f.seek(offset,0)
                        f.write(Product_DB.rec_template.format(self.name,self.unit_price,self.stock_quantity)) 
                        f.close()                    
                        is_updated = True
                    offset=offset+1+Product_DB.rec_length
        except StopIteration: #When end of file is encountered, StopIteration exception is raised.
            print("File handling error while updating a record in product.txt")
        return is_updated


    def __str__(self):
        return f'{self.name:20}, {self.unit_price:5.2f}, {self.stock_quantity:5d}\n'

'''
products=[Product_DB("Pen", 10, 100), Product_DB("Eraser", 5.6787, 10)]
for a_product in products:
    a_product.save()
'''
'''
a_product =Product_DB.read_product(offset=71,bytes=Product_DB.rec_length)
print(a_product.name)
print(a_product.unit_price)
print(a_product.stock_quantity)'''