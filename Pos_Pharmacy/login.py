from main_router import main_router
#==============login==================
user_name = "admin"
password = 112233 
while True:
    print("\n============Please Login============") 
    u = input("Enter Username: ") 
    try:
        p = int(input("Enter Password: "))
    except ValueError:
        print("Password must be a number!")
        continue
    if u == user_name and p == password:
        print("Login Successfully!")
        main_router()
        break
    else:
        print("Incorrect, Try again!......")
