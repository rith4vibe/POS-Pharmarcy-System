#==============login==================
print("\n============Please Login============")
user_name = "admin"
password = 112233 

u = input("Enter Username: ")
p = int (input("Enter Password: "))

if u == user_name and p == password:
    print("Login Success!")
else:
    print("Incorect, Try again!......")