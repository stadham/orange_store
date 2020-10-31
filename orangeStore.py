#Quarter one exam
import random
import time

print("-------------------------------------------------------------------")
print("Welcome to the Orange Store Game")
print("-------------------------------------------------------------------")
print("You will play a game where you are selling oranges on the sidewalk to passing customers.")
print("You can change locations and the amount of people walking past you will vary based on the location.")
print("Sales of oranges depend on the location and amount of people in the area.")
print("The amount of people walking by your box will vary but the more people the more you will sell.")
print("The idea is to sell as many oranges as you can in X amount of time.")
print("You will buy the oranges each week and decide how much to sell each for.")
print("Oranges will vary in price from your supplier each week because your supplier is greaty")
print("Oranges cannot be kept over one week or they will spoil, rot and go bad")
print("You can only sell them on Saturday your day off from school.")
print("You need to manage your store correctly.")
print("So what are you waiting for lets get started")

go_on = 0
orange_amount = 0
oranges_sold = 0
paid_for_oranges = 0
week = 0
price = 0
orange_price = 0
sales_price = 0
people = 0
location = 0
place = 0
daily_sales = 0
amount_sold = 0
cash = 50

print("-------------------------------------------------------------------")
name = input("what is your name? ")
print("OK lets get going "+ name+" ")
print("-------------------------------------------------------------------")

done = False

while not done:
    week = week + 1
    orange_amount = 0

#  Status report here **********************************

    print("-------------------------------------------------------------------")
    print("Oranges Shop REPORT")
    print("-------------------------------------------------------------------")
    print("This is week ",week)
    print("You have this much cash ",cash)
    print("Amount of oranges you have", orange_amount)
    print("-------------------------------------------------------------------")

#     Buying oranges Here **************************************

    print("Now go buy your oranges on Friday night")

    orange_price = random.randrange(1, 10)

    print("The price for each orange is ", orange_price, " yuan")

    orange_amount = int(input("How many oranges do you want? "))

    paid_for_oranges = orange_amount * orange_price

    sales_price = int(input("How much are you going to sell each for orange for? "))

    cash = cash - paid_for_oranges
    print("-------------------------------------------------------------------")
    print("You now have ",orange_amount, "oranges")
    print("You have ",cash," yuan left")
    print("-------------------------------------------------------------------")
    go_on = input("Press the G key to go on ")
    if go_on.lower() == "g":
        print("Keep going your doing great")
    else:
        print("OUCH")
    print("-------------------------------------------------------------------")

# Selling the Oranges here *********************************

    print("Pick a location to sell your oranges")
    print("1. Bus Station")
    print("2. Shopping Center")
    print("3. Train Station")
    print("4. THSI" )

    location = int(input("1, 2, 3, or 4? "))

    if location == 1:
        people = random.randrange(1, 50)
        place = random.randrange(50, 206)
        print("There are ",people, "people here")

    elif location == 2:
        people = random.randrange(1, 30)
        place = random.randrange(30, 117)
        print("There are ", people, "people here")
        
    elif location == 3:
        people = random.randrange(1, 20)
        place = random.randrange(20, 307)
        print("There are ",people, "people here")
        
    elif location == 4:
        people = random.randrange(1, 10)
        place = random.randrange(10, 370)
        print("There are ",people, "people here")
        
    oranges_sold = random.randrange(people, place)

    lost_sales = random.randrange(1, 12)
    
    if lost_sales == 1:
        print("*******You were sick and had to stay home. No oranges sold")
        oranges_sold = 0
    elif lost_sales == 2:
        print("********It rained all day and no one bought oranges")
        oranges_sold = 0
    elif lost_sales == 3:
        print("********You had to run for your life the police came around. You sold no oranges")
        oranges_sold = 0
    elif lost_sales == 4:
        print("********You had to say home and study for the TOFL today and so no oranges sold")
        oranges_sold = 0
    else:
        print("It was a good day")

    if oranges_sold > orange_amount:
        oranges_sold = orange_amount

    daily_sales = oranges_sold *  orange_amount

    cash = cash + daily_sales
#forgot the + 1 to make it real count
    for i in range(oranges_sold + 1):
        print(i, " oranges sold")
        time.sleep(.5)

    print("-------------------------------------------------------------------")
    print("Oranges Shop Weekly REPORT")
    print("-------------------------------------------------------------------")
    print("This is week ",week)
    print("Amount of oranges you have", orange_amount)
# Amount of oranges you have left over if any
    print("Oranges sold ", oranges_sold)

    if orange_amount > oranges_sold:
        print("You lost ", orange_amount - oranges_sold, " oranges")

    daily_sales = sales_price * oranges_sold

    print("You made ", daily_sales, " yuan")

    print("on ", oranges_sold, "oranges sold")

    print("You now have this much cash ",cash)

    print("-------------------------------------------------------------------")

    go_on = input("Press the G key to go or Q to quit")
    if go_on.lower() == "g":
        print("Keep going your doing great")
    elif go_on.lower() =="q":
        done = True
    else:
        print("OUCH")
    print("-------------------------------------------------------------------")

    orange_price = random.randrange(1, 8)

    if cash < 10:
        print("You do not have enough money to buy oranges")
        print("You have gone bankrupt")
        done = True

print("-------------------------------------------------------------------")
print("Game over. Please come back soon and play again")
print("-------------------------------------------------------------------")

