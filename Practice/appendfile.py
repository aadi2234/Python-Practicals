with open('input.txt','r') as src,open('output.txt','w') as dest:
    line=src.read()
    dest.write(line)
    print("Data appended Successfully")