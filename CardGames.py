##################################################################
# COSC 1336 Lab 6                                                #
# Lab 6 Solution                                                 #
#                                                                #
# This program gives the user a menu of card games               #
# to play.  It will continue to offer the games                  #
# unitl the user chooses to quit.                                #
#                                                                #
# Currently available games:                                     #
#    1. Make Change                                              #
#    2. High Card                                                #
#    3. Deal Hand                                                #
#    4. Save Dream Hand                                          #
#    5. Display Dream Hand                                       #
#                                                                #
# Make Change: will read a purchase amount and a payment amount  #
# and display the change due and the breakdown of the change     #
# into number of dollars, quarters, dimes, nickels and pennies   #
#                                                                #
# High Card: will deal one card to each of two players, display  #
# who got which card and who wins                                #
#                                                                #
# Deal Hand: deals and displays a 5-card hand                    #
#                                                                #
# Save Dream Hand: lets the user save their 5-card dream hand in #
# in a file name specified by them                               #
#                                                                #
# Display Dream Hand: reads and displays the contents of a file  #
# specified by the user that contains a 5-card dream hand        #
##################################################################

import random

# Define global constants for the menu options
MAKE_CHANGE = 1
HIGH_CARD = 2
DEAL_HAND = 3
SAVE_DREAM_HAND = 4
DISPLAY_DREAM_HAND = 5
QUIT = 6

def main():

    # Welcome the user
    welcome()
    
    # Get the first menu choice
    choice = menu()

    # Once the user chooses to quit, do not contiue
    # to display the menu
    while choice != QUIT:

        # Check the choice and play the game chosen
        if choice == MAKE_CHANGE:
            make_change()
        elif choice == HIGH_CARD:
            high_card()
        elif choice == DEAL_HAND:
            deal_hand()
        elif choice == SAVE_DREAM_HAND:
            save_dream_hand()
        elif choice == DISPLAY_DREAM_HAND:
            display_dream_hand()

        # Get the next menu choice
        choice = menu()

#############################################################
# Function:	welcome                                     #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function welcomes the user and         #
#               displays a program description              #
#############################################################
def welcome():
    # Display program description
    print('\n******************************************************')
    print('*   Welcome to the Lame Game computer gaming room    *')
    print('*                                                    *')
    print('* This program display a game menu:                  *')
    print('* 1. Make Change                                     *')
    print('* 2. High Card                                       *')
    print('* 3. Deal Hand                                       *')
    print('* 4. Save Dream Hand                                 *')
    print('* 5. Display Dream Hand                              *')
    print('* 6. Quit                                            *')
    print('*                                                    *')
    print('* Prompts for option and plays the game chosen.      *')
    print('******************************************************\n')

#############################################################
# Function:	menu                                        #
# Inputs:	none                                        #
# Outputs:	a valid menu choice                         #
# Description:	This function will display the game menu,   #
#               reads the choice, validates the choice      #
#               and returns it                              #
#############################################################
def menu():
    
    try:
        # Display the menu and read the choice
        print("\n\nLame Game Main Menu")
        print("-------------------")
        print("1. Make Change")
        print("2. High Card")
        print("3. Deal Hand")
        print("4. Save Dream Hand")
        print("5. Display Dream Hand")
        print("6. Quit")
        choice = int(input("\nEnter choice: "))
        
       # Check for invalid input
        while choice < MAKE_CHANGE or choice > QUIT:
            print("Invalid option...")
            # Display the menu and read the choice again
            print("\n\nLame Game Main Menu")
            print("-------------------")
            print("1. Make Change")
            print("2. High Card")
            print("3. Deal Hand")
            print("4. Quit")
            choice = int(input("\nEnter choice again: "))
        
    except ValueError:
        print("Error: Invalid data entered")
        # Set choice to 0 because an error has occurred
        # Function must always return a value, even
        # if there were an error
        choice = 0

    # Pass back the user's choice
    return choice

#############################################################
# Function:	make_change                                 #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function will read a purchase amount   #
#               and a payment amount and display the change #
#               due and the breakdown of the change into    #
#               number of dollars, quarters, dimes, nickels #
#               and pennies                                 #
#############################################################
def make_change():

    # Read the amount of the purchase
    price = float(input('\nEnter the amount of the purchase '))

    # Read the amount of the payment
    paid = float(input('Enter the amount of payment '))

    # Check to see if the payment is enough to cover the purchase
    if paid < price:
        print('You did not pay enough')
        
    else:

        # Calculate the change due
        change = paid - price

        # Display the change due
        print('\nChange due: ',format(change,'.2f'))
        #print('   unformatted: ',change)
        print('This breaks down into:')

        # Calculate the number of dollars due
        dollars = int(change//1)
        print('\tDollars:\t',dollars)

        # Isolate the change amount and convert it to an integer.
        # To account for precesion lost converting to an integer,
        # force rounding of the 100ths digit by adding .005
        # to the change portion
        change = int(((change - dollars) + .005)* 100)
        #print('change is now ',change)

        # Calculate the number of quaters due
        quarters = change // 25
        print('\tQuarters:\t',quarters)
        change = change - (quarters * 25)

        # Calculate the number of dimes due
        dimes = change // 10
        print('\tDimes:\t\t',dimes)
        change = change - (dimes * 10)

        # Calculate the number of nickels due
        nickels = change // 5
        print('\tNickels:\t',nickels)
        change = change - (nickels * 5)

        # The number of pennies due will be all that is left
        pennies = change
        print('\tPennies:\t',pennies)
        print()

#############################################################
# Function:	high_card                                   #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function will read the name of each of #
#               2 players deal 2 cards to each player and   #
#               determine who wins:                         #
#               the player with the highest card            #
#############################################################
def high_card():
    print("High Card")
    print("----------")

    # Prompt for user's names
    player1 = input("What is your first name player one? ")
    player2 = input("What is your first name player two? ")

    # Deal two cards: Generate random card between 1 and 13
    player1_card = random.randint(1,13)
    player2_card = random.randint(1,13)

    # Display the cards
    print("Card for ", player1, ": ", end=' ')
    display_face_value(player1_card)
    print("Card for ", player2, ": ", end=' ')
    display_face_value(player2_card)

    # Check to see which card was higher,
    # or if the game is a draw
    if player1_card > player2_card:
        print("Contratulations ", player1, ", You Won!")
    elif player2_card > player1_card:
        print("Contratulations ", player2, ", You Won!")
    else:
        print("The game is a draw; both cards are the same")

#############################################################
# Function:	deal_hand                                   #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function will deal a five card hand    #
#               using a random number function then         #
#               displays the face value of each card        #
#############################################################
def deal_hand():
    print("Deal Hand")
    print("------------")

    # Deal a five card hand: Generate 5 random cards between 1 and 13
    card1 = random.randint(1,13)
    card2 = random.randint(1,13)
    card3 = random.randint(1,13)
    card4 = random.randint(1,13)
    card5 = random.randint(1,13)
    
    # Display the cards
    print("The 5-card hand is:")
    display_face_value(card1)
    display_face_value(card2)
    display_face_value(card3)
    display_face_value(card4)
    display_face_value(card5)

##############################################################
# Function:	save_dream_hand                              #
# Inputs:	none                                         #
# Outputs:	none                                         #
# Description:	This function get a file name from the user  #
#               and their favorite 5-card hand, and saves    #
#               the cards in the file.  The cards are given  #
#               by numeric value:                            #
#               Ace = 1                                      #
#               Two = 2 ... Ten = 10                         #
#               Jack = 11                                    #
#               Queen = 12                                   #
#               King = 13                                    #
##############################################################
def save_dream_hand():

    print("Save Dream Hand")
    print("------------------")
    
    # Get file name from user
    file_name = input("Enter the file name: ")
    outfile = open(file_name, 'w')

    try:
        # Prompt user for 5 cards (numeric value)
        card1 =  int(input("Enter a card (1-13): "))
        # Error check card, must be between 1 and 13
        while card1 < 1 or card1 > 13:
            print("Error: card must be between 1 and 13")
            card1 =  int(input("Enter a card (1-13): "))
            
        card2 =  int(input("Enter a card (1-13): "))
        # Error check card, must be between 1 and 13
        while card2 < 1 or card2 > 13:
            print("Error: card must be between 1 and 13")
            card2 =  int(input("Enter a card (1-13): "))
            
        card3 =  int(input("Enter a card (1-13): "))
        # Error check card, must be between 1 and 13
        while card3 < 1 or card3 > 13:
            print("Error: card must be between 1 and 13")
            card3 =  int(input("Enter a card (1-13): "))
            
        card4 =  int(input("Enter a card (1-13): "))
        # Error check card, must be between 1 and 13
        while card4 < 1 or card4 > 13:
            print("Error: card must be between 1 and 13")
            card4 =  int(input("Enter a card (1-13): "))
            
        card5 =  int(input("Enter a card (1-13): "))
        # Error check card, must be between 1 and 13
        while card5 < 1 or card5 > 13:
            print("Error: card must be between 1 and 13")
            card5 =  int(input("Enter a card (1-13): "))

        # Write cards to file   
        outfile.write(str(card1) + '\n')
        outfile.write(str(card2) + '\n')
        outfile.write(str(card3) + '\n')
        outfile.write(str(card4) + '\n')
        outfile.write(str(card5) + '\n')

        # Close file
        outfile.close()

    # Error trap for invalid value for card
    except ValueError:
        print("Error: Invalid input")

##############################################################
# Function:	display_dream_hand                           #
# Inputs:	none                                         #
# Outputs:	none                                         #
# Description:	This function reads and displays the 5-card  #
#               hand stored in the file given by the user    #
#               and displays the face value of the card.     #                                                        #
##############################################################    
def display_dream_hand():

    print("Display Dream Hand")
    print("---------------------")
    try:
        # Get file name from user
        file_name = input("Enter the file name: ")
        infile = open(file_name, 'r')

        # Read each card from the file
        card1 =  int(infile.readline())
        card2 =  int(infile.readline())
        card3 =  int(infile.readline())
        card4 =  int(infile.readline())
        card5 =  int(infile.readline())

        # Display the face value of each card
        print("The 5-card dream hand is:")
        display_face_value(card1)
        display_face_value(card2)
        display_face_value(card3)
        display_face_value(card4)
        display_face_value(card5)
           
        # Close file
        infile.close()

    # Check for invalid file name
    except FileNotFoundError:
        print("Error: Invalid file name")
        
        
#############################################################
# Function:	display_face_value                          #
# Inputs:	integer card value                          #
# Outputs:	none                                        #
# Description:	This function will display the face value   #
#               of a numeric card                           #
#############################################################
def display_face_value(value):
    # Display the face value of the card passed in
    if value == 1:
        print("Ace")
    elif value == 2:
        print("Two")
    elif value == 3:
        print("Three")
    elif value == 4:
        print("Four")
    elif value == 5:
        print("Five")
    elif value == 6:
        print("Six")
    elif value == 7:
        print("Seven")
    elif value == 8:
        print("Eight")
    elif value == 9:
        print("Nine")
    elif value == 10:
        print("Ten")
    elif value == 11:
        print("Jack")
    elif value == 12:
        print("Queen")
    elif value == 13:
        print("King")
    else:
        # This will catch an invalid value passed in
        print("Invalid card")

main()
    
