#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

#print
def print_row(x):
	print('+ - - - - '*x + '+')

def print_col(x):
	print('|         '*x + '|')
	print('|         '*x + '|')
	print('|         '*x + '|')
	print('|         '*x + '|')

def print_grid(x):
	n = x
	while n!=0:
		print_row(x)
		print_col(x)
		n = n-1
	print_row(x)

def two_by_two():
	print_grid(2)

def four_by_four():
	print_grid(4)



# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    two_by_two()
    
    four_by_four()


if __name__ == "__main__":
    main()