import csv
import os
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
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
    def show_charts(self):
    """
    Daily chart analysis
    """
    df = pd.read_csv("sales.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df["Period"] = df["Date"].dt.date.astype(str)
    revenue = df.groupby("Period")["Total"].sum().reset_index()
    top_medicine = df.groupby("MedicineName")["Quantity"].sum().reset_index()
    sales_dist = df.groupby("MedicineName")["Total"].sum().reset_index()
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "xy"}, {"type": "domain"}],
               [{"colspan": 2, "type": "xy"}, None]],
        subplot_titles=("Daily Revenue", "Sales Distribution", "Top Selling Medicines")
    )
    fig.add_trace(go.Scatter(x=revenue["Period"], y=revenue["Total"], mode="lines+markers", name="Revenue"), row=1, col=1)
    fig.add_trace(go.Pie(labels=sales_dist["MedicineName"], values=sales_dist["Total"], name="Sales Distribution"), row=1, col=2)
    fig.add_trace(go.Bar(x=top_medicine["MedicineName"], y=top_medicine["Quantity"], name="Top Selling"), row=2, col=1)
    fig.update_layout(height=700, width=900, title_text="Pharmacy POS Daily Analytics Dashboard")
    fig.show()
        with open(self.FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["SaleID", "MedicineName", "Price", "Quantity", "Total", "Date"])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Sale '{sale_id}' deleted successfully.")
