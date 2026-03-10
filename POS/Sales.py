import csv
import os
from datetime import datetime
class Sale:
    FILE = "sales.csv"
    
    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "SaleID",
                    "MedicineName",
                    "Price",
                    "Quantity",
                    "Total",
                    "Date"
                ])

    def make_sale(self):
        sale_id = input("Enter Sale ID: ")
        name = input("Enter Medicine Name: ")
        price = float(input("Enter Price: "))
        qty = int(input("Enter Quantity: "))
        total = price * qty
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([sale_id, name, price, qty, total, date])
        print("Sale Saved!")
        
    def view_sales(self):
        with open(self.FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)