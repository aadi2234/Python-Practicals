def letters(string):
    ul = 0
    ll = 0
    for char in string:
        if 'A' <= char <= 'Z':
            ul += 1
        elif 'a' <= char <= 'z':
            ll += 1
    print("Number of Upper Case Letters:", ul)
    print("Number of Lower Case Letters:", ll)

string = input("Enter a String: ")
letters(string)
