#DAY1
class Product: #class 
    def __init__(self,mid,name,price,qty,): #constructor
        self.mid = mid
        self.name = name
        self.price = price
        self.qty = qty

    def display(self): #display  // I have to fix at this display
        print(f"ID: {self.mid}")
        print(f"Name: {self.name}")
        print(f"Price:${self.price}")
        print(f"Quatity: {self.qty}")


class Manage_Medicine: #class
    # Read data and store
    def __init__(self):
        self.medicines = []
    
        # Add Medicine
    def add_medicine(self):
        print("\n=====ADD MEDICINE======")
        mid = input("Enter Medicine ID: ")
        name = input("Enter Medicine Name: ")
        price = float (input("Enter Medicine Price: "))
        qty = int(input("Enter Medicine Quantity: "))

        medicines = Product(mid,name,price,qty)
        self.medicines.append(medicines)
        #color
        print("\033[92mMedicine Added Seccessfully!\033[0m")
      
#DAY2
        # View Medicine
    def view_medicine(self):
        print("\n=====MEDICINES LIST=====")
        if len(self.medicines) == 0:
            print("\033[91mNo Medicines Available.\033[0m")
        else:
            for m in self.medicines:
                m.display()

        # Search Medicine
    def search_medicine(self):
        print("\n=====SEARCH MEDICINES=====")
        mid = input("Enter Medicine ID: ")
        for m in self.medicines:
            if m.mid == mid:
                m.display()
                return
        
        print("\033[91mMedicine not found!\033[0m")

        # Delete Medicine
    def delete_medicine(self):
        print("\n=====DELETE MEDICINES=====")
        mid =input("Enter ID Medicine To Delete: ")
        for m in self.medicines:
            if m.mid == mid:
                self.medicines.remove(m)
                print("\033[92Medicine Deleted!\033[m0")
                return
            print("\033[91Medicine Not found!\033[0m")

        # Update Medicine Stock
    def update_medicine_stock(self):
        print("\n=====UPDATE MEDICINE STOCK=====")

        print("Enter Medicine ID: ")
        print("Enter Medicine Name:")
        print("Enter Medicine Price: ")
        print("Enter Medicine Quatity: ")
        for m in self.medicines:
            self.medicines.append(m)
            print("\033[92Update Medicine Stock!\033[0m")            






       
       
       
       
    
        # Create object 
manage = Manage_Medicine()
        
        #main menu
while True:
    print("\n=====MANAGE PRODUCTS=====")
    print("1. Add Medicine.")
    print("2. View Medicine.")
    print("3. Search Medicine.")
    print("4. Delete Medicine.")
    print("5. Update Medicine Stock.")

    choice = input("Chose Option:")
    if choice == "1":
        manage.add_medicine()
    elif choice == "2":
        manage.view_medicine()
    elif choice == "3":
        manage.search_medicine()
    elif choice == "4":
        manage.delete_medicine()
    elif choice == "5":
        manage.update_medicine_stock()
    else:
        print("\033[91mInvalid Choice!\033[0m")    