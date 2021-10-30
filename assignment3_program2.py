print("The price for apple is 20 pesos and for orange is 25 pesos.")
    # displaying the price of the fruits - apple and orange

def fruits(a, o):
    return (a*20) + (o*25)
        # creating a function with the computation

def displayOutput(totalF):
    print(f"The total amount is {totalF}.")
        # creating a function that will print the total amount

apple = int(input("Enter the number of apple: "))
    # creating a variable that will ask for the number of apple
orange = int(input("Enter the number of orange: "))
    # creating a variable that will ask for the number of orange

total = fruits(apple, orange)
    # creating a varible that will call the function fruits along with the information to process the computation

displayOutput(total)
    # calling the function - displayOutput along with the total variable to send back the information and print using the format

'''
Steps:
1. Display the prices of the fruits.
2. Ask for the number of apple.
3. Ask for the number of orange.
4. Compute the total amount.
5. Display the total amount.

'''