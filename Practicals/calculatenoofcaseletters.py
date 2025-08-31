def letters(string):
    ul=0;
    ll=0;
    for i in string:
        if(i.isalpha()):            
            if(i.islower()):
                ll=ll+1
            else:
                ul=ul+1
    print("Number of Upper Case Letters:",ul)
    print("Number of Lower Case Letters:",ll)
string=input("Enter a String:")
letters(string)