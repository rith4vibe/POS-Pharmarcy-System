from management_medicine import Manage_Medicine
from sales import Sale

def main_router():
    sale = Sale()
    username = "admin"
    password = 112233
    
    while True:
        print("============== PLEASE LOGIN ===============")

        u = input("Enter Username: ")
        p = int(input("Enter Password: "))
        if u == username and p == password:
            print("\033[92mLogin Successfully\033[0m")
            break
        else:
            print("\033[91mIncorrect, Try again...\033[0m") 
   
    while True:
        print("\n======================= PHARMACY POS SYSTEM =========================")
        print("1. Manage Products.")
        print("2. Sales.")
        print("3. Exit.")
        choice = input("Choose Option: ")
        if choice == "1":
            manage = Manage_Medicine()
            manage.menu()
        elif choice == "2":
            sale.menu(manage)

        elif choice == "3":
            print("\033[91mExit Programming, Thanks....\033[0m")
            break
        else:
            print("\033[93mInvalid option. Try again.\033[0m")


if __name__ == "__main__":
    main_router()
