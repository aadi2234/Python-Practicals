#50.	Implement a program to calculate no. of lines, words and characters in any file.
with open('input.txt','r') as f:
    no_lines=0
    no_words=0
    no_character=0
    for data in f:
        data=data.strip("\n")
        word=data.split()
        no_lines+=1
        no_words+=len(word)
        no_character +=len(data)
    print("Lines",no_lines,"words",no_words,"characters",no_character)
