from Sales import Sale
from dashboard import show_charts
sale = Sale()

while True:

    print("\n===== PHARMACY POS =====")
    print("1. Make Sale")
    print("2. View Sales")
    print("3. Chart Analysis")
    print("4. Exit")
    choice = input("Choose option: ")
    if choice == "1":
        sale.make_sale()
    elif choice == "2":
        sale.view_sales()
    elif choice == "3":
        show_charts()
    elif choice == "4":
        break
    else:
        print("Invalid option!")
        