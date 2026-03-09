#DAY1
class Product:
    def __init__(self,mid,name,price,qty,): #constructor
        self.mid = mid
        self.name = name
        self.price = price
        self.qty = qty

    def display(self): #display
        print(f"ID: {self.mid}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quatity: {self.qty}")

class Manage_Medicine:
    # Read data and store
    def __init__(self):
        self.medicines = []
    
        # Add product
    def add_medicine(self):
        print("\n=====ADD MEDICINES======")
        mid = input("Enter Medicine ID: ")
        name = input("Enter Medicine Name: ")
        price = float (input("Enter Medicine Price: "))
        qty = int(input("Enter Medicine Quantity: "))

        medicines = Product(mid,name,price,qty)
        self.medicines.append(medicines)
        print("Medicine Added Seccessfully!")
      
#DAY2
        # View Product
    def view_medicine(self):
        print("\n=====MEDICINES LIST=====")
        if len(self.medicines) == 0:
            print("No Medicines Available.")
        else:
            for m in self.medicines:
                m.display()



        # Create object 
manage = Manage_Medicine()
        
        #main menu
while True:
    print("\n=====MANAGE PRODUCTS=====")
    print("1. Add Medicines.")
    print("2. View Medicines.")

    choice = input("Chose Option:")
    if choice == "1":
        manage.add_medicine()
    elif choice == "2":
        manage.view_medicine()
        