def sumofdigit(no):
    sum=0
    while(no>0):
        digit=no%10
        sum=sum+digit
        no=no//10
    print("Sum of digits=",sum)
no=int(input("Enter a Number:"))
sumofdigit(no)