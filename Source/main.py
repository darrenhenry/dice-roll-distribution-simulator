# Dice Roll Distribution Simulator

# Built-in libraries utilized by program
import sys
import random
# External libraries utilized by program
import matplotlib.pyplot

# This function prints a welcome message and explains the program
def welcome_message():
    print()
    print('Welcome to the Dice Roll Distribution Simulator!')
    print()
    print('Two dice are thrown for each roll, resulting in a total from two to twelve. Enter the number of times you\n'
          'wish to roll the dice, and a bar graph will be generated displaying the distribution of results.')

# This function asks the user for the number of dice rolls to simulate
def get_number_of_rolls():
    # Store error message for invalid user input
    error_message = 'Error! Number of dice rolls must be an integer greater than zero! Try again!'
    try:
        print()
        roll_count = int(input('How many times would you like to roll the dice?: '))
    # Error handling and recursion for non integer values
    except ValueError:
        print(error_message)
        roll_count = get_number_of_rolls()
    # Error handling and recursion for invalid integer values
    if roll_count <= 0:
        print(error_message)
        roll_count = get_number_of_rolls()
    # Final value for valid user input
    return roll_count

# This function simulates the dice rolling and tracks the results
def roll_dice(roll_count):
    # Dictionary composition to initialize counts for each possible dice result
    result_dictionary = {str(key): 0 for key in range(2, 13, 1)}
    for roll in range(roll_count):
        # Simulate random individual dice results and combine total
        die_roll_1 = random.randint(1, 6)
        die_roll_2 = random.randint(1, 6)
        total = str(die_roll_1 + die_roll_2)
        # Increment value associated with result key
        result_dictionary[total] = result_dictionary.get(total, 0) + 1
    return result_dictionary

# This function generates a bar graph representing the simulation results
def show_distribution(roll_count, result_dictionary):
    matplotlib.pyplot.bar(result_dictionary.keys(), result_dictionary.values())
    matplotlib.pyplot.xlabel('Roll Result')
    matplotlib.pyplot.ylabel('Frequency')
    matplotlib.pyplot.title(f'Distribution of Frequencies for {roll_count} Dice Rolls')
    matplotlib.pyplot.show()
    print()
    print(f'Plot has been generated for {roll_count} rolls!')

# This function asks the user for to end the program or generate another simulation
def exit_message(roll_count):
    # Store error message for invalid user input
    error_message = "Error! Enter 'y' to roll again or 'n' to exit."
    print()
    roll_again = str(input('Would you like to roll again (y/n)? '))
    # Conditional recursion if the user chooses to generate another simulation
    if roll_again == 'y':
        roll_count = get_number_of_rolls()
        result_dictionary = roll_dice(roll_count)
        show_distribution(roll_count, result_dictionary)
        exit_message(roll_count)
    # Conditional program exit if the user chooses to exit the program
    if roll_again == 'n':
        print()
        print('Thanks for using the Dice Roll Distribution Simulator!')
        sys.exit()
    # Error handling and recursion for invalid user input
    else:
        print(error_message)
        exit_message(roll_count)

# Main function calls user defined functions and controls program flow
def main():
    welcome_message()
    roll_count = get_number_of_rolls()
    result_dictionary = roll_dice(roll_count)
    show_distribution(roll_count, result_dictionary)
    exit_message(roll_count)

# Final call to main
if __name__ == '__main__':
    main()
