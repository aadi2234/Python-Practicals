a,b,c,d,e=map(int,input("Enter marks of 5 subjects=").split())
avg=(a+b+c+d+e)/5
print("Average Marks=",avg)
if(avg>=75):
    print("Grade:First Class with Dist.")
elif(avg>=60 and avg<=74):
    print("Grade:First Class")
elif(avg>=50 and avg<=59):
    print("Grade:Second Class")
elif(avg>=40 and avg<=49):
    print("Grade:Third Class")
else:
    print("Grade:Fail")