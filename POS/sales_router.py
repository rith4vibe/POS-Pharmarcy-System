from make_sale import make_sale
from sale_history import sale_history
from dashboard import dashboard
import sys
import os
class SalesRouter:

    def __init__(self):
        self.routes = {}
        self.register_routes()

    def register(self, key, name, func):
        self.routes[key] = (name, func)

    def register_routes(self):
        self.register('1', "Make Sale", make_sale)
        self.register('2', "Sales History", sale_history)
        self.register('3', "Dashboard", dashboard)
        self.register('0', "Exit", self.exit_program)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self):
        self.clear()
        print("======[ POS SYSTEM ]======")
        for key in sorted(self.routes):
            print(f"{key}. {self.routes[key][0]}")

    def route(self, choice):
        action = self.routes.get(choice)
        if not action:
            print("Invalid choice.")
            return

        try:
            action[1]()
        except Exception as e:
            print("Error:", e)

        input("\nPress Enter to continue...")
    def exit_program(self):
        print("Exiting system...")
        sys.exit()

    def start(self):
        while True:
            self.display_menu()
            choice = input("Select option: ").strip()
            self.route(choice)

if __name__ == "__main__":
    SalesRouter().start()