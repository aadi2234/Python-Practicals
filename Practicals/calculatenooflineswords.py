ipFileObj=open('input.txt','r')
words=1
lines=1
characters=1
while True:
    char=ipFileObj.read(1)
    print(char,end="")
    characters+=1
    if char.isspace():
        words+=1
    if char=='\n':
        lines+=1
    if not char:
        break
ipFileObj.close()
print("\ncharacters =",characters)
print("words =",words)
print("lines =",lines)