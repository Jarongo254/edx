name = input("what's your name ")
#use the open command to open a file
# file = open("names.txt", "a") 
# 'w' writes contents onto the file. rerunning the code overwrites the original content
# 'a' appends contents onto the file meaning they are written and saved on the file.
# 
# file.write(f"{name}\n")
# file.close
#using the 'with' argument ensures the file is open and then closed after code execution (automation)
with open("names.txt", "a") as file:
    file.write(f"{name}\n")