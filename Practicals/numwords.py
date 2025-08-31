t=('zero','one','two','three','four','five','six','seven','eight','nine')
l=[]
num=int(input("Enter a number="))
while num>0:
    r=t[num%10]
    num=int(num/10)
    l.append(r)
l.reverse()
print(l)