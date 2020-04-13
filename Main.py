
from Res import CustomersProductMenu as cpm
import sys
from Res import admin

class WrongChoiceError(Exception):
    """docstring for WrongChoiceError"""
    pass

def adminMenu():
    var = admin()
    
    pass

def exit():
    print("Exiting...")
    sys.exit()


def main():
    """ Title
            Main Menu
                    Products Info Generator
                    administrator
                    exit
                    """

    print("********************Canteen-Management**********************\n"
          "====================================================\n"
          "***********************S=Y=S=T=E=M**************************\n\n\n")

    print("\t\t============Main Menu==============\n")

    print("\t\t01. Products Report Generator\n")
    print("\t\t02. administrator\n")
    print("\t\t03. exit\n")

    print("\t\t===================================\n")

    print("\t\tPlease Select Your Option (1-3)")

    while True:
        try:
            choice = int(input("\t\t"))

            if choice == 1:
                cpm.customersMenu()
            elif choice == 2:
                adminMenu()
            elif choice == 3:
                exit()
            else:
                raise WrongChoiceError

        except WrongChoiceError:
            print("Wrong Choice has been entered,\n"
                  "please Choose number from 1-3")


main()
