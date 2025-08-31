num=int(input("Enter number to generate Fibonacci-"))
def fibonacci(num):
    a=0
    b=1
    for i in range(1,num+1):
        print(a,end=" ")
        next=(a+b)
        a=b
        b=next
fibonacci(num)

