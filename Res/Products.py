
import pprint
import sqlite3

class Products(object):

    def __init__(self, No=0):
        self.No = No 
        self.Name = input("\t\tEnter Product Name\n")
        self.Company = input("\t\tEnter Company Name\n")
        self.Price = int(input("\t\tEnter Product Price\n"))
        self.Quantity = int(input("\t\tEnter Quantity of Product\n"))
        self.Discount = int(input("\t\tEnter Product Discount (if any)\n"))


    def getInfo(self):
        self.product_info =(self.No, self.Name, 
                        self.Company, self.Price, 
                        self.Quantity, self.Discount)
        return self.product_info    

if __name__ == "__main__":
    data = ['spam', 'eggs', 'hello', 'shubham']

    pp = pprint.PrettyPrinter(width=100, compact=True, depth=10, indent=5)
    pp.pprint(data)