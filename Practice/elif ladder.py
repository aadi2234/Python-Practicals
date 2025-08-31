per=int(input("Enter Percentage:"))
if(per>=75 and per<=100):
    print("Distinction")
elif(per>=60 and per<75):
    print("First Class")
elif(per>=40 and per<60):
    print("Pass")
elif(per<40):
    print("Fail")
else:
    print("Invalid Percentage")