
import pprint
import os
os.chdir("Res")
import sqlite3
from Products import Products 
import pprint
from prettytable import from_db_cursor


try:
    os.chdir("data")
except:
    os.mkdir("data")
    os.chdir("data")

class admin(object):
    """docstring for admin
                -Create Products
                -Display all available
                Search Products
                Modify Products
                Delete Products
                Back to Menu
        """

    def __init__(self):
        self.product_data = sqlite3.connect(database="dt.db")
        self.cursor = self.product_data.cursor()
        
        cmd = """create table if not exists ProductDt (No int NOT NULL, Name varchar2(100) NOT NULL,
                                                Company varchar2(100), price float,
                                                Quantity int, discount float, PRIMARY KEY(No))"""
        self.cursor.execute(cmd)
        cmd = """select No from ProductDt"""
        self.cursor.execute(cmd)
        self.No_list = self.cursor.fetchall()
        self.prev_no = self._productNoinitializer(self.No_list)
        


    def createProducts(self):
        temp_product = Products(self.prev_no)

        def writeToDb():
            ls = temp_product.getInfo()
            
            cmd = "insert into ProductDt values(?, ?, ?, ?, ?, ?)"
            self.cursor.execute(cmd, ls)
            self.product_data.commit()
            print("\t\tProduct added\n")
        writeToDb()

    def displayProducts(self):
        con = sqlite3.connect(database="dt.db")
        with con:
            cur = con.cursor()
            cur.execute("select * from ProductDt")

            x = from_db_cursor(cur)
        
        print(x)


    def searchProducts(self):
        self._fetchData()
        print(self.data_list)
        item_to_search = input("\t\tEnter the name of the product: ")
        is_item_found = False
        for _,e in enumerate(self.data_list):
            for i in e:
                if i == item_to_search:
                    print("Product is present in the Database")
                    is_item_found = True
                    break
                else:
                    continue
        
        if not is_item_found:
            print("Product not present in the Database")
                    
    def modifyProducts(self):
        self._fetchData()
        self.displayProducts()
        no = int(input("\t\tEnter the No of the Product to be modified"))
        def _modifyRow():
            name = input("\t\tEnter the Product name: ")
            company = input("\t\tEnter the Company name:")
            price = int(input("\t\tEnter the Price: "))
            quantity = int(input("\t\tEnter the Quantity: "))
            discount = int(input("\t\tEnter the discount: "))

            cmd = """update ProductDt
                    set
                        Name = ?,
                        Company = ?,
                        Price = ?,
                        Quantity = ?,
                        Discount = ?
                    where
                        No = ?"""
            
            tup = (name, company, price, quantity, discount, no)
            self.cursor.execute(cmd, tup)
            self.product_data.commit()
            print("\t\tProduct has been modified")

        _modifyRow()

    def deleteProducts(self):
        self.displayProducts()
        no = int(input("\t\tEnter the No of product to be deleted::"))
        def _deleteRow():
            cmd = """delete from ProductDt where No = ?"""
            self.cursor.execute(cmd, str(no))
            self.product_data.commit()
            
        if no not in self.No_list:
            print("\t\tProduct No is not in database")
        else:
            if input("\t\tPress Enter to delete: "):
                _deleteRow()
                print("Product deleted from the database")

    def backToMenu(self):
        pass
    
    def _productNoinitializer(self, No_list):
        try:
            res = int(''.join(map(str, No_list[-1])))
            return res + 1
        except IndexError:
            return 0


    def _fetchData(self):
        cmd = "select * from ProductDt"
        self.cursor.execute(cmd)
        self.data_list = self.cursor.fetchall()
        

if __name__ == "__main__":
    dmin = admin()
    dmin.displayProducts()