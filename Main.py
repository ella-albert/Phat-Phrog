"""Phat Phrog: A story by Ella Albert"""
"""This beautiful tale follows the life of a frog as he gets adopted and"""
"""begins his new life. You, his new owner, get to choose what happens!"""
__author__ = "Ella Albert"

import time

def frog(stretch):
#The * operator here multiplies the string by whichever number is input.
    frogstretch1 = (" " * stretch)
    frogstretch2 = ("-" * stretch)
    frogstretch3 = ("_" * stretch)
    frogstretch4 = ("~" * stretch)
    print("\n    @.",frogstretch1,".@    ",sep="")
    print("   (--", frogstretch2,"--)   ",sep="")
    print(" (  >_",frogstretch3,"_<  ) ",sep="")
    print(" ^^  ~",frogstretch4,"~  ^^ ",sep="")

def ValueCheck(variable):
    moving_on = True
    while moving_on == True:
        try:
            variable = int(variable)
            return variable
            moving_on = False
        except ValueError:
            variable = input("Please enter an integer. ")
        
print("Hello and welcome to FrogCo! You're here to adopt a frog, right?")
#The function time.sleep() delays the output of the next line of code.
time.sleep(2)
print("Splendid! Before you can adopt this frog,",end=" ")
print("you'll need to fill out some paperwork.")
name = input("What is your legal first name? ")
#The + operator here concatenates the two strings.
print(name + "?" , "Alright.")
#I assign a guardian so it will stop asking for payment.
x = 0
payment = str(input("And will you be paying with cash or card? "))
#The == operator here checks if the two are equal.
while x == 0:
#The or statement accounts for capital letters.
    if payment == "Cash" or payment == "cash":
        print("Cash, okay.")
        print("Adopting a frog will only be $5!")
        time.sleep(4)
        cost = 5
#The end argument prints the next two lines together.
        print("\nWhoops! I forgot you'll need some food as well.",end=" ")
        print("It will be $25 extra.",end=" ")
        print("Oh, but you have a discount! The frog food is 45.6% off!")
        time.sleep(7)
#The + operator here adds on the fee for frog food.
        cost = cost + 25
#The * operator multiplies 60% times 25, and the - operator subtracts it.
        cost = cost - (25 * .456)
        print("\nYou have another discount for having a discount!",end=" ")
        print("Half off!! \nPlus we'll make it a pretty number for you.")
        time.sleep(7)
#The / operator divides it by two.
        cost = cost / 2
#The // operator eliminates the decimals by rounding.
        cost = cost // 1
        print("\nAww, man! I forgot about the fee for the premium air",end=" ")
        print("you're breathing right now. \nSo the cost will be",end=" ")
        print("exponentially increased by a factor of two.")
        time.sleep(7)
#The ** operator makes it an exponent.
        cost = cost**2
#The sep argument eliminates extra space in the next print statement.
        print("Your total is now $",format(cost,"0.2f"),".",sep="")
        time.sleep(2)
        x += 1
    elif payment == "Card" or payment == "card":
        print("Card, okay.")
        time.sleep(2)
        print("*beep*")
        time.sleep(2)
        print("*card declined*")
        time.sleep(2)
        print("Uh oh. I'll tell you what.",end=" ")
        print("Enter a number between 1 and 10, and if you guess the",end=" ")
        print("\nnumber I'm thinking of, I'll give you the frog for free!")
        number = input("What number am I thinking of? ")
        number = ValueCheck(number)
#The % operator checks if the number is perfectly divisible by 7.
        if (number % 7) == 0 and (1 <= number <= 10):
                     print("Wow, how did you know? I guess Mr. Frog is yours.")
                     time.sleep(2)
                     x += 1
        elif (number % 7) != 0 and (1 <= number <= 10):
            print("Sorry, but that wasn't what I was thinking of.")
            print("Do you have an alternate form of payment?")
            time.sleep(3)
            payment = "Cash"
        else:
            print("Hey, that's not a number between 1 and 10!",end=" ")
            print("Just pay up. You've got cash, right?")
            payment = "Cash"
            
    else:
        payment = input("Um...? Cash or Card? ")
print("Here is your new pet frog!")
print("\n    U..U    ")
print("   (----)   ")
print(" (  >__<  ) ")
print(" ^^  ~~  ^^ ")
print("\nAww, he's sleeping! Why don't you take him home?")
print("\nYou take him home and put him in his new habitat.")
frog_name = input(name+": 'What should I name this young lad?' ")
print(name+": '"+frog_name,"seems like a good name.'")
print(name+": 'He looks hungry.'")
#The variable x here is used as a guardian for this nested loop.
food = 0
while food in range(0,1):
    while food in range(0,1):
         stretch = input("How much food should I give him? ")
         stretch = ValueCheck(stretch)
         break
    if not stretch >= 5:
        print(name+": 'No, he'll waste away if I give him that!'")
        food = 0
    elif 5 <= stretch and stretch <= 25:
            print(name+": 'That should be enough.'")
            food += 1
    elif 25 < stretch <= 70:
            print(name+": 'I might be overfeeding him...'")
            food += 1
    else:
            print(name+": 'I don't have enough frog food for that!'")
            food = 0
#The number input into stretch is the argument, and becomes the parameter.
frog(stretch)
time.sleep(2)
print(name+": '.",end=" ")
time.sleep(2)
print(".",end=" ")
time.sleep(2)
print(".'")
time.sleep(2)
print(frog_name+": 'RIBBIT'")
time.sleep(1)
print(name+": 'AHHHHHH!'")

    
    


