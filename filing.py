#name = input("what's your name ")
#use the open command to open a file
# file = open("names.txt", "a") 
# 'w' writes contents onto the file. rerunning the code overwrites the original content
# 'a' appends contents onto the file meaning they are written and saved on the file.
# 
# file.write(f"{name}\n")
# file.close
#using the 'with' argument ensures the file is open and then closed after code execution (automation)
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
#    file.write(f"{name}\n")

#with open("names.txt", "r") as file:
#    lines = file.readlines()

#for line in lines:
#    print("hello,", line.rstrip())
# csv (comma separated values) - format for capturing related data e.g person-house
# csv.reader parses csv documents, determining where each component of the data in the csv file falls- drawn from the csv module
# ***read documentation on csv module
