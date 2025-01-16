#IT 3883/Section 01
#Kaito Hamm
#Lab 1
#This program will prompt the user to select betweeen numbers 1-4 

#ask user to pick a number 
string =""

#while loop 
choice = 0
while(choice != '4'):
    choice = input("please choose from the following. \n1. Please input a string \n2. displays all previous input concatented \n3. Clears input buffer \n4. Exit program\n")
    if choice == '1' :
        string+= input("Please input a string: ")
        
    elif choice == '2':
        print(string)
        
    elif choice == '3':
        string = ""
    elif choice == '4':
        print("Exit. Goodbye.")
        break
    else:  
        print("invalid selection. PLease select from 1-4")
        choice = input ("Please selection again")

