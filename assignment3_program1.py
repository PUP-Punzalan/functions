def getName():
    theName = input("Enter name: ")
    return theName
        # creating a function to get the name

def getAge():
    theAge = input("Enter age: ")
    return theAge
        # creating a function to get the age

def getAddress():
    theAddress = input("Enter address: ")
    return theAddress
        # creating a function to get the address

def displayOutput(nameOuput, ageOutput, addressOutput):
    print(f"Hi, my name is {nameOuput}. I am {ageOutput} years old and I live in {addressOutput}.")
        # creating a function to print / display the name, age, and address

name = getName()
    # calling the function getName and move the input into the name variable
age = getAge()
    # calling the function getAge and move the input into the age variable
address = getAddress()
    # calling the function getAddress and move the input into the address variable

displayOutput(name, age, address)
    # calling the displayOutput with the variables - name, age, and address to print it

'''
Steps:
1. Ask for the name at the same time save it to a variable.
2. Ask for the age at the same time save it to a variable.
3. Ask for the address at the same time save it to a variable.
4. Display the information - name, age, address.

'''
