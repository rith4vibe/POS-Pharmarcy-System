from sales import Sale
from chart_analysis import show_charts
sale = Sale()
while True:
    print("\n===== PHARMACY POS SYSTEM =====")
    print("1. Make Sale")
    print("2. View Sales")
    print("3. Search Sale")
    print("4. Delete Sale")
    print("5. Chart Analysis")
    print("6. Exit")
    choice = input("Choose option: ")
    if choice == "1":
        sale.make_sale()
    elif choice == "2":
        sale.view_sales()
    elif choice == "3":
        sale.search_sale()
    elif choice == "4":
        sale.delete_sale()
    elif choice == "5":
        show_charts()
    elif choice == "6":
        break
    else:
        print("Invalid option. Try again.")
