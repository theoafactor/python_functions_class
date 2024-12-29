def checkUser():
    username = input('Enter the username of the user you want to check: ')
    fobject = open("users.csv", "r")
    data = fobject.readlines()
    
    counter = 0
    does_user_exist = False
    while counter < len(data):
        if counter != 0:
            data_box = data[counter].split(",")
            if username == data_box[2]:
                ## we  have found the user 
                # print("User retrieved: ")
                # print("Firstname: " , data_box[0])
                # print("Lastname: ", data_box[1])
                # print("Username: ", data_box[2])
                # print("Email: ", data_box[3])
                does_user_exist = True
                return [data_box[0], data_box[1], data_box[2], data_box[3]]
                
            else:
                does_user_exist = False

        counter = counter + 1

    if does_user_exist == False:
        return []

    

print("""
   ---- Welcome to the Users Database ----
                By Olu Adeyemo
                -------------- 

                    Menu
                --------------
                1. Check a user
                2. Add User to database
                3. Print all Users from database
                4. Exit
 """)
 
option = input("Pick an option from the menu items: ")

if option == "1": 
    print("1: Check a user")
    result = checkUser()
    if len(result) == 0: 
        print("No user with that username exists in our records")
    else: 
        print("Result: -------")
        print("Firstname: ", result[0])
        print("Lastname: ", result[1])
        print("Username: ", result[2])
        print("Email: ", result[3])


elif option == "2": 
    print("2: Add User to database")

elif option == "3": 
    print("3: Print all users from database")

elif option == "4": 
    print("4: Exiting ...")

else: 
    print("invalid option.. try again")