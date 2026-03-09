class Product:
    def __init__(self, pid, name, price, qty):
        self.pid = pid
        self.name = name
        self.price = price
        self.qty = qty

    def display(self):
        print(f"ID: {self.pid}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.qty}")
        print("----------------------")


class manage_product:
    def __init__(self):
        self.products = []

    # Add Product
    def add_product(self):
        print("\n=== Add Product ===")
        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        qty = int(input("Enter Quantity: "))

        product = Product(pid, name, price, qty)
        self.products.append(product)

        print("Product added successfully!")

    # View Product
    def view_product(self):
        print("\n=== Product List ===")

        if len(self.products) == 0:
            print("No product available.")
        else:
            for p in self.products:
                p.display()

    # Delete Product
    def delete_product(self):
        print("\n=== Delete Product ===")
        pid = input("Enter Product ID to delete: ")

        for p in self.products:
            if p.pid == pid:
                self.products.remove(p)
                print("Product deleted.")
                return

        print("Product not found.")

    # Search Product
    def search_product(self):
        print("\n=== Search Product ===")
        pid = input("Enter Product ID: ")

        for p in self.products:
            if p.pid == pid:
                print("Product Found:")
                p.display()
                return

        print("Product not found.")


# Program
manager = manage_product()

while True:
    print("\n====== MANAGE PRODUCT ======")
    print("1 → Add Product")
    print("2 → View Product")
    print("3 → Delete Product")
    print("4 → Search Product")
    print("5 → Back")

    choice = input("Choose option: ")

    if choice == "1":
        manager.add_product()

    elif choice == "2":
        manager.view_product()

    elif choice == "3":
        manager.delete_product()

    elif choice == "4":
        manager.search_product()

    elif choice == "5":
        print("Back to main menu...")
        break

    else:
        print("Invalid choice!")