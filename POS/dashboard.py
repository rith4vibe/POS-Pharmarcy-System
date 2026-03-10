import pandas as pd
import matplotlib.pyplot as plt

def show_charts():
    df = pd.read_csv("sales.csv")
    # BAR CHART
    sales = df.groupby("MedicineName")["Total"].sum()
    plt.figure()
    sales.plot(kind="bar")
    plt.title("Total Sales by Medicine")
    plt.xlabel("Medicine")
    plt.ylabel("Revenue")
    # PIE CHART
    plt.figure()
    sales.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Sales Distribution")
    plt.show()