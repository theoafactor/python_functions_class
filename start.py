## define a function that collects usernames
def getUsername(username): #<--- parameter
  
    if len(username) == 0:
        print("No name was provided")
    else: 
        print('Welcome ' + username)



## COllect name from user
username = input("Enter your username: ")
## call the function
getUsername(username) ## <-- argument
