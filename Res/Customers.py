
"""
    Customers Menu
        Create Customers Details
        Display all Customers Details
        Search Record
        Modify Customers Records
        Delete Customers Records
        Back to MainMenu"""

import os
import sqlite3
from prettytable import from_db_cursor

class Customer(object):
    """No Name address Phone no"""

    def __init__(self):
        
        try:
            os.chdir("Data")
        except:
            os.mkdir("Data")
            os.chdir("Data")
        
        self.db = sqlite3.connect(database="dt.db")
        self.cur = self.db.cursor()

        cmd = """create table if not exists CustomersDt (CustNo int NOT NULL, Name varchar(100),
                                                        address varchar(100), PhoneNo int,
                                                        primary key(CustNo))"""
        self.cur.execute(cmd)
        self.db.commit()
        cmd = """select No from CustomersDt"""
        self.cursor.execute(cmd)
        self.No_list = self.cursor.fetchall()
        self.prev_no = self._productNoinitializer(self.No_list)


        def createCustomersDetails(self):
            name = input("\t\tEnter the name of the Customer: ")
            address = input("\t\tEnter the address of the Customer: ")
            phoneno = int(input("\t\tEnter Phone no:"))
            if len(phoneno) <= 10:
                pass
            else:
                print("Invalid PhoneNo")


            ls = (self.prev_no, name, address, phoneno)
            cmd = """insert into CustomersDt values (?, ?, ?, ?)"""
            self.cur.execute(cmd, ls)


        def displayCustomerDetails(self):
            con = sqlite3.connect(database="dt.db")
            with con:
                cur = con.cursor()
                cur.execute("select * from CustomersDt")

                x = from_db_cursor(cur)
        
            print(x)

        def searchRecords(self):
            self._fetchData()
            
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

        
        def modifyCustomerDetails(self):
            self._fetchData()
            self.displayCustomerDetails()
            no = int(input("\t\tEnter the CustNo to be modified: "))
            def _modifyRow():
                name = input("\t\tEnter the Customer's name: ")
                address = input("\t\tEnter the address: ")
                phoneno = int(input("\t\tEnter Phone no: "))
                if len(phoneno) <= 10:
                    pass
                else:
                    print("Invalid PhoneNo")                

                cmd = """update CustomersDt
                        set
                            Name = ?,
                            address = ?,
                            PhoneNo = ?
                        where
                            No = ?"""
            
                tup = (name, address, phoneno)
                self.cur.execute(cmd, tup)
                self.dt.commit()
                print("\t\Customer data has been modified")

            _modifyRow()

        
        def deleteCustomerRecords(self):
            self.displayCustomerDetails()
            no = int(input("\t\tEnter the CustNo to be deleted::"))
            def _deleteRow():
                cmd = """delete from CustomersDt where No = ?"""
                self.cur.execute(cmd, str(no))
                self.dt.commit()
            
            if no not in self.No_list:
                print("\t\tCustomer is not in database")
            else:
                if input("\t\tPress Enter to delete: "):
                    _deleteRow()
                print("\t\tCustomer deleted from the database")

        
        def _productNoinitializer(self, No_list):
            try:
                res = int(''.join(map(str, No_list[-1])))
                return res + 1
            except IndexError:
                return 0


        def _fetchData(self):
            cmd = "select * from CustomersDt"
            self.cursor.execute(cmd)
            self.data_list = self.cursor.fetchall()
     