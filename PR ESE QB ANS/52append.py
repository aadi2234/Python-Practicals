#52.	Implement a program to create a new file “first.txt”, write some data in it and show its contents line by line. In this file, append some another data in file and show whether data is updated or not.
with open('first.txt','w') as file:
    file.write("Hi..!\nThis is Sample\nPython PR-ESE")
    print("Data Written Successfully..")
with open('first.txt','r') as file:
    for line in file:
        print(line.strip())
with open('first.txt','a') as file:
    file.write("\nHello..!\nThis is Appended Data\nPython PR-ESE")
    print("Data Appended Successfully..")
with open('first.txt','r') as file:
    for line in file:
        print(line.strip())  