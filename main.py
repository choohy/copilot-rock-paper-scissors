# write a rock paper sissor game
# import a random module
import random

# define the main function that handles all the logic
def main():
    # define the variables
    # the user choice
    user_choice = ''
    # the computer choice
    computer_choice = ''
    # the winner
    winner = ''
    # the user's score
    user_score = 0
    # the computer's score
    computer_score = 0
    # the number of ties
    ties = 0
    # the number of rounds
    rounds = 0

    # display the welcome message
    print("Welcome to the Rock, Paper, Scissors, Lizard and Spock game!")

    # ask the user how many rounds they want to play
    rounds = int(input("How many rounds would you like to play? "))

    # validate the rounds
    while rounds < 1 or rounds > 10:
        print("Please enter a number between 1 and 10.")
        rounds = int(input("How many rounds would you like to play? "))

    # start the game
    for i in range(rounds):
        # ask the user for their choice
        user_choice = input("Please enter your choice (R)ock, (P)aper, (Sc)issors, (L)izard, or (Sp)ock: ")
        #validate the user's choice if they entered the full word and single letter
        while user_choice != 'Rock' and user_choice != 'rock' and user_choice != 'Paper' and user_choice != 'paper' and user_choice != 'Scissors' and user_choice != 'scissors' and user_choice != 'Lizard' and user_choice != 'lizard' and user_choice != 'Spock' and user_choice != 'spock' and user_choice != 'R' and user_choice != 'r' and user_choice != 'P' and user_choice != 'p' and user_choice != 'Sc' and user_choice != 'sc' and user_choice != 'L' and user_choice != 'l' and user_choice != 'Sp' and user_choice != 'sp':
            print("Please enter a valid choice.")
            user_choice = input("Please enter your choice (R)ock, (P)aper, (Sc)issors, (L)izard, or (Sp)ock: ")
        # get the computer's choice
        computer_choice = get_computer_choice()
        # print computer_choice
        print("The computer chose", computer_choice)
        # determine the winner
        winner = determine_winner(user_choice, computer_choice)
        # display the winner
        if winner == 'user':
            print("You won!")
            user_score += 1
        elif winner == 'computer':
            print("The computer won!")
            computer_score += 1
        else:
            print("It's a tie!")
            ties += 1

    # display the final results
    print("You won", user_score, "times.")
    print("The computer won", computer_score, "times.")
    print("You tied", ties, "times.")

#defnie the get_computer_choice function with new options
def get_computer_choice():
    # generate a random number
    rand_num = random.randint(1, 5)
    # determine the computer's choice
    if rand_num == 1:
        return 'R'
    elif rand_num == 2:
        return 'P'
    elif rand_num == 3:
        return 'S'
    elif rand_num == 4:
        return 'L'
    else:
        return 'Sp'
    
#define the determine_winner function with new options
def determine_winner(user_choice, computer_choice):
    # determine the winner
    if user_choice == 'R' or user_choice == 'r' or user_choice == 'Rock' or user_choice == 'rock':
        if computer_choice == 'R':
            return 'tie'
        elif computer_choice == 'P':
            return 'computer'
        elif computer_choice == 'S':
            return 'user'
        elif computer_choice == 'L':
            return 'user'
        else:
            return 'computer'
    elif user_choice == 'P' or user_choice == 'p' or user_choice == 'Paper' or user_choice == 'paper':
        if computer_choice == 'R':
            return 'user'
        elif computer_choice == 'P':
            return 'tie'
        elif computer_choice == 'S':
            return 'computer'
        elif computer_choice == 'L':
            return 'computer'
        else:
            return 'user'
    elif user_choice == 'Sc' or user_choice == 'sc' or user_choice == 'Scissors' or user_choice == 'scissors':
        if computer_choice == 'R':
            return 'computer'
        elif computer_choice == 'P':
            return 'user'
        elif computer_choice == 'S':
            return 'tie'
        elif computer_choice == 'L':
            return 'user'
        else:
            return 'computer'
    elif user_choice == 'L' or user_choice == 'l' or user_choice == 'Lizard' or user_choice == 'lizard':
        if computer_choice == 'R':
            return 'computer'
        elif computer_choice == 'P':
            return 'user'
        elif computer_choice == 'S':
            return 'computer'
        elif computer_choice == 'L':
            return 'tie'
        else:
            return 'user'
    else:
        if computer_choice == 'R':
            return 'user'
        elif computer_choice == 'P':
            return 'computer'
        elif computer_choice == 'S':
            return 'user'
        elif computer_choice == 'L':
            return 'computer'
        else:
            return 'tie'


# Call main
main()
