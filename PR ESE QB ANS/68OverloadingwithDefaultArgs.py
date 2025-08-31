#68.	Write a Python program to create a class to print an integer and a character with two
#methods having the same name but different sequence of the integer and the character parameters.
#For example, if the parameters of the first method are of the form (int n, char c), then that of
#the second method will be of the form (char c, int n).
class Overloading:
    def show(self, n=None, c=None):
        if n and c:
            print("Number=", n, " Character=", c)
        if n is None or c is None:
            print("Insufficient Data")

o = Overloading()
o.show(n=2, c='A')
o.show(c='Z', n=92)
