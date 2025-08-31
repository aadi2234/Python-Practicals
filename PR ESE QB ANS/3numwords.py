#•	Print the number in words for Example: 1234 => One Two Three Four. Input a tuple from User.
#t=('zero','one','two','three','four','five','six','seven','eight','nine')
t = tuple(input("Enter the elements of the tuple separated by spaces: ").split())
l=[]
num=int(input("Enter a number="))
while num>0:
    r=t[num%10]
    num=int(num/10)
    l.append(r)
l.reverse()
print(l)
