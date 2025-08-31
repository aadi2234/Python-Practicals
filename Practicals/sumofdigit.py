num=int(input("Enter a number-"))
a=num
sum=0
while(num>0):
    digit=num%10
    sum=(sum+digit)
    num=num//10
print("Sum of",a,"=",sum)
