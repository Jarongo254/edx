try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

'''The try command compels the program to run the code while checking
 for errors, in this case a value error incase the input is not an integer.
If there is no error the exception is not triggered therefore the else 
command is executed. The exception is triggered when a value error occurs,
i.e. by entering a value that is not an integer, executing the alternative command.'''

#Alternative with introduction of an infifnite loop. 
#The 'break' command can be used alternatively after the exception to break the infinite loop
#'return' is a better alternative that can be used in a function to break out of a loop
#  within the function while returning a value as well.
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")


#function alternative

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
        
main()

''' 'pass' can be used as well to catch the error without necessarily indicating
  to the user.'''
#code becomes more compact and easy to read
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass        
main()
