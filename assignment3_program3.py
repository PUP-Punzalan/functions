def total_price(totalMoney, applePrice):
    totalApple = totalMoney // applePrice
    totalPrice = totalApple * applePrice
    return totalPrice
        # funtion that will solve how much is the total price of the apple

def total_change(totalMoney, totalPrice):
    totalChange = totalMoney - totalPrice
    return totalChange
        # function that will solve how much is the total change

def total_apple(totalMoney, applePrice):
    totalApple = totalMoney // applePrice
    return totalApple
        # function that will solve how much apple they can buy with the specified money and price

def displayOutput(totalApple, totalChange):
    print(f"You can buy {totalApple:.0f} apples and your change is {totalChange:.2f} pesos.")
        # function that will print the total apple they can buy and the total change

money = float(input("Enter the total money: "))
    # variable to get the total money they have
price = float(input("Enter the price per apple: "))
    # variable to get the price per apple

priceF = total_price(money, price)
    # variable that calls the function to solve for the total price
changeF = total_change(money, priceF)
    # variable that calls the function to solve for the total change
appleF = total_apple(money, price)
    # variable that calls the function to solve for the total apple they can buy

displayOutput(appleF, changeF)
    # calling the function to print the total apple and change

'''
Steps:
1. Ask how much the total money.
2. Ask for the price of one apple.
3. Compute the total amount of apple they can buy with their total money.
4. Compute for the change.
5. Display the total amount of apply then can buy and their change.

'''