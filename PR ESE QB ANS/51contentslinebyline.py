#51.	Implement a program to create a new file “first.txt”, write some data in it
#and show its contents line by line.
with open('first.txt','w') as file:
    file.write("Hi..!\nThis is Sample\nPython PR-ESE")
    print("Data Written Successfully..")
with open('first.txt','r') as file:
    for line in file:
        print(line.strip())