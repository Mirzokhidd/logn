#Imports

import filecmp 
import re


#basic idea: If you sing up, it creates a file with your username ( and the password has some rules to follow). When logging in, if the same file exists 
# with the username given, it compares the data inside to the username and password. If it matches it lets you in if not than doesnt 


#the login page
def login():
    print("\nLogin: \n")
    username = input("Your Username: ")
    password = input("Your Password: ")

    if username and password in open(username + ".txt").read(): #compare the inputed username and passowrd to a file with the the same username
        print("It is correct. Welcome\n")
    else: 
        print("Wrong username or password. Try again\n")
        login()


#the sing up page
def signup():
    print("\nSign up \n")
    username = input("Your Username: ")
    password = input("Your Passoword: ")

    try:
        username = open(username + ".txt") #check if a file with the same username exists
        print("\nOhh that account already exists. Try signing in or create a new account\n")
        menu()
    except: #if not than make sure to check the password rules
        if re.search('[0-9]',password) is None:
            print("Have one number atleast and one capital letter")
        elif re.search('[A-Z]',password) is None: 
            print("Have one number atleast and one capital letter")
        else:
            with  open(username + ".txt", "a") as f:
                f.write(username)
                f.write(password)
            print("\n Remember: " + "\n Username: " + username + "\n Password: " + password + " \n") # if everything is right, create the file with that username and password
    

def menu(): # the menu page
    while True:
        ask = int(input("What do you want to do: (Index number only)\n 1. Log in \n 2. Sign Up \n "))
        if ask == 1:
            login()
        elif ask == 2:
            signup()

menu()