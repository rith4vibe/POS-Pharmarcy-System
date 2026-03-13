from management_medicine import Manage_Medicine
from sales import Sale

def main_router():
    sale = Sale()
    while True:
        print("\n=======================PHARMACY POS SYSTEM=========================")
        print("1. Manage Products.")
        print("2. Sales.")
        print("3. Exit.")
        choice = input("Choose Option: ")
        if choice == "1":
            manage = Manage_Medicine()
            manage.menu()
        elif choice == "2":
            sale.menu()

        elif choice == "3":
            print("\033[91mExit Programming....\033[0m")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main_router()
