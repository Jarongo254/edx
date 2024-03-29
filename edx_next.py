# 'import' is used to call modules with existing code for functions 
#   that soeone can use for their own projects withought having to create
#      new ones from scratch
import statistics
print(statistics.mean([20, 24, 17]))
'''This calls the mean function from the statistics module to calculate the average 
for a select set of numbers.'''

#Alternatively
from statistics import mean
print(mean([4, 12, 32]))
'''This directly imports a specific function fro the module without having to import the entire module'''


#Command line argument
import sys

print("Hello my name is", sys.argv[1]) 
'''will print the string I type after typing the command on the command line or teminal''' 
# sys.exit can be used to exit the program given specified parameters have 
#   been met. can be used with conditionals

#PACKAGES- Modules implemented in folders

# write code to test other code- to make sure the code works properly.

# assert- enforces a boolean to check if a circumstance is true or false
#   -failed assertion raises an assertion error i.e a false is raised


#pytest is a commandline prompt that runs tests on the specified code