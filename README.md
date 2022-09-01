# Dice Roll Distribution Simulator

Welcome to the Dice Roll Distribution Simulator!

What it Does:
- Two dice are thrown for each roll, resulting in a total from two to twelve
- Enter the number of times you wish to roll the dice, and a bar graph will be generated displaying the distribution of         results for the simulation

How it Works:
- Dice throw results are generated through the buit-in "random" library for each die
- Program stores the result of each throw of the die in a dictionary
- Program utilizes bar plot functionality of "matplotlib.pyplot" library to display the results
- Includes error handling of user input and conditional recursion to allow the user to generate back to back simulations

Curious About the Results?
When you roll a single die, you have an equal probability of landing on each side of the die (1/6). Therefore, if you roll a single die many times, you would expect to see a fairly even distribution of frequencies for the results 1, 2, 3, 4, 5, and 6. However, when you add another die into each throw, you now have possible results of 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, and 12. In addition, there are 36 possible combinations of results from a double dice throw. Below are the probailities of each result when throwing two dice (1/36 means there is only one combination of die that would add to that result).

2:  1/36
3:  2/36 
4:  3/36
5:  4/36
6:  5/36
7:  6/36
8:  5/36
9:  4/36
10: 3/36
11: 2/36
12: 1/36

So, in the context of this program, simulating a low amount of double dice rolls will result in a relatively unpredictable distribution of frequencies. However, you may notice that as you increase the number of simulated rolls, your distribution of frequencies displayed in the graph will more closely resemble the probabailities listed above.
