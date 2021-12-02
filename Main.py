"""Phat Phrog: a dramatic adoption story that will change your life."""
__author__ = "Ella Albert"

# I import time because I will use it later to delay print statements.
import time


def frog(stretch):
    """This function prints the cartoon frog, expanding it according to which
    number (stored in variable stretch) is input."""
    # The * operator here multiplies the string by whichever number is input.
    frog_stretch1 = (" " * stretch)
    frog_stretch2 = ("-" * stretch)
    frog_stretch3 = ("_" * stretch)
    frog_stretch4 = ("~" * stretch)
    print("\n    @.", frog_stretch1, ".@    ", sep="")
    print("   (--", frog_stretch2, "--)   ", sep="")
    print(" (  >_", frog_stretch3, "_<  ) ", sep="")
    print(" ^^  ~", frog_stretch4, "~  ^^ ", sep="")


def value_check(variable):
    """This function checks if the variable is an integer.
    If it is not, this function prints an error message.
    This function will not continue until an integer is input.
    The parameter "variable" is then converted to integer
    format and returned."""
    moving_on = True
    while moving_on:
        try:
            variable = int(variable)
            return variable
        except ValueError:
            variable = input("Please enter a whole number. ")


def enter_home(name):
    """This function continues the story once the user
    enters the home. It includes a frog cartoon, allows
    you to input the frog's name, and calls the frog_stretch
    function. The parameter "name" is used in this function."""
    print("Here is your new pet frog!")
    print("\n    U..U    ")
    print("   (----)   ")
    print(" (  >__<  ) ")
    print(" ^^  ~~  ^^ ")
    print("\nAww, he's sleeping! Why don't you take him home?")
    print("\nYou take him home and put him in his new habitat.")
    frog_name = input(name + ": 'What should I name this young lad?' ")
    print(name + ": '" + frog_name, "seems like a good name.'")
    print(name + ": 'He looks hungry.'")
    # The variable x here is used as a guardian for this nested loop.
    food = 0
    stretch = 0
    while food in range(0, 1):
        while food in range(0, 1):
            stretch = input("How many flies should I feed him? ")
            stretch = value_check(stretch)
            break
        if not stretch >= 5:
            print(name + ": 'No, he'll waste away if I give him that!'")
            food = 0
        elif (5 <= stretch) and (stretch <= 25):
            print(name + ": 'That should be enough.'")
            food += 1
        elif 25 < stretch <= 70:
            print(name + ": 'I might be overfeeding him...'")
            food += 1
        else:
            print(name + ": 'I don't have enough flies for that!'")
            food = 0
    # The number input is the argument, and it becomes the parameter.
    frog(stretch)
    time.sleep(2)
    print("\n" + name + ": '.", end=" ")
    time.sleep(2)
    print(".", end=" ")
    time.sleep(2)
    print(".'")
    time.sleep(2)
    print(frog_name + ": 'RIBBIT'")
    time.sleep(1)
    print(name + ": 'AHHHHHH!'")
    time.sleep(2)
    adoption = True
    while adoption:
        print("\nWould you like to adopt another frog?")
        adoption_choice = input("\nEnter 1 for yes, and 2 for no! ")
        adoption_choice = value_check(adoption_choice)
        if adoption_choice == 1:
            adoption = False
            enter_store()
        elif adoption_choice == 2:
            print("Goodbye! Come back to FrogCo soon :)")
            adoption = False
        else:
            print("\nPlease enter in 1 or 2.")


def cash(name):
    """This function continues the story if the user selects
    "cash" as their form of payment. The parameter "name"
    is used in this function."""
    print("Cash, okay.")
    print("Adopting a frog will only be $5!")
    time.sleep(4)
    cost = 5
    # The end argument prints the next two lines together.
    print("\nWhoops! I forgot you'll need a habitat as well.", end=" ")
    print("It will be $25 extra.", end=" ")
    print("Oh, but you have a discount! The habitat is 45.6% off!")
    time.sleep(7)
    # The + operator here adds on the fee for frog food.
    cost = cost + 25
    # The * operator multiplies 60% times 25, and the - operator subtracts it.
    cost = cost - (25 * .456)
    print("\nYou have another discount for having a discount!", end=" ")
    print("Half off!! \nPlus we'll make it a pretty number for you.")
    time.sleep(7)
    # The / operator divides it by two.
    cost = cost / 2
    # The // operator eliminates the decimals by rounding.
    cost = cost // 1
    print("\nAww, man! I forgot about the fee for the premium air", end=" ")
    print("you're breathing right now. \nSo the cost will be", end=" ")
    print("exponentially increased by a factor of two.")
    time.sleep(7)
    # The ** operator makes it an exponent.
    cost = cost ** 2
    # The sep argument eliminates extra space in the next print statement.
    print(name + ", your total is now $", format(cost, "0.2f"), ".", sep="")
    time.sleep(2)
    enter_home(name)


def card(name):
    """This function continues the story if the user selects
    "card" as their form of payment. The parameter "name" is
    used in this function."""
    print("Card, okay.")
    time.sleep(2)
    print("*beep*")
    time.sleep(2)
    print("*card declined*")
    time.sleep(2)
    print("Uh oh. I'll tell you what.", end=" ")
    print("Enter a number between 1 and 10, and if you guess the", end=" ")
    print("\nnumber I'm thinking of, I'll give you the frog for free!")
    number = input("What number am I thinking of? ")
    number = value_check(number)
    # The % operator checks if the number is perfectly divisible by 7.
    if (number % 7) == 0 and (1 <= number <= 10):
        print("Wow,", name + ", how did you know? I guess Mr. Frog is yours.")
        time.sleep(2)
        enter_home(name)
    elif (number % 7) != 0 and (1 <= number <= 10):
        print("Sorry, but that wasn't what I was thinking of.")
        print("Do you have an alternate form of payment?")
        time.sleep(3)
        cash(name)


def enter_store():
    """This function serves as a sort of main function, and
    you return to it if you repeat the project. It includes
    the adoption scene and calls either the cash or card function."""
    print("Hello and welcome to FrogCo! You're here to adopt a frog, right?")
    # The function time.sleep() delays the output of the next line of code.
    time.sleep(2)
    print("Splendid! Before you can adopt this frog,", end=" ")
    print("you'll need to fill out some paperwork.")
    name = input("What is your legal first name? ")
    # The + operator here concatenates the two strings.
    print(name + "?", "Alright.")
    payment = str(input("And will you be paying with cash or card? "))
    # The or statement accounts for capital letters.
    payment_choice = True
    while payment_choice:
        if payment == "Cash" or payment == "cash":
            cash(name)
            payment_choice = False
        elif payment == "Card" or payment == "card":
            card(name)
            payment_choice = False
        else:
            payment = input("Um...? Cash or card? ")


# Starting off the story
enter_store()



