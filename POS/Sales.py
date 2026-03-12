import csv
import os
from datetime import datetime
class Sale:
    FILE = "sales.csv"
    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["SaleID", "MedicineName", "Price", "Quantity", "Total", "Date"])
    def get_sale_ids(self):
        ids = set()
        with open(self.FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                ids.add(row["SaleID"])
        return ids

    def make_sale(self):
        sale_id = input("Enter Sale ID: ").strip()
        if sale_id in self.get_sale_ids():
            print("Sale ID already exists.")
            return
        name = input("Enter Medicine Name: ").strip()
        try:
            price = float(input("Enter Price: "))
            qty = int(input("Enter Quantity: "))
        except ValueError:
            print("Invalid input for price or quantity.")
            return
        if price <= 0 or qty <= 0:
            print("Price and quantity must be positive.")
            return
        total = price * qty
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([sale_id, name, price, qty, total, date])
        print("Sale Saved!")
    def view_sales(self):
        with open(self.FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            print(f"{'SaleID':<10} {'MedicineName':<20} {'Price':<10} {'Qty':<10} {'Total':<10} {'Date'}")
            print("-" * 75)
            for row in reader:
                print(f"{row['SaleID']:<10} {row['MedicineName']:<20} {float(row['Price']):<10.2f} "
                      f"{row['Quantity']:<10} {float(row['Total']):<10.2f} {row['Date']}")

    def search_sale(self):
        keyword = input("Enter SaleID or Medicine Name: ").strip().lower()
        found = False
        with open(self.FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            print(f"{'SaleID':<10} {'MedicineName':<20} {'Price':<10} {'Qty':<10} {'Total':<10} {'Date'}")
            print("-" * 75)
            for row in reader:
                if keyword in row["SaleID"].lower() or keyword in row["MedicineName"].lower():
                    print(f"{row['SaleID']:<10} {row['MedicineName']:<20} {float(row['Price']):<10.2f} "
                          f"{row['Quantity']:<10} {float(row['Total']):<10.2f} {row['Date']}")
                    found = True
        if not found:
            print("No matching sales found.")

    def delete_sale(self):
        sale_id = input("Enter SaleID to delete: ").strip()
        rows = []
        found = False
        with open(self.FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["SaleID"] != sale_id:
                    rows.append(row)
                else:
                    found = True
        if not found:
            print("SaleID not found.")
            return
        with open(self.FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["SaleID", "MedicineName", "Price", "Quantity", "Total", "Date"])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Sale '{sale_id}' deleted successfully.")
