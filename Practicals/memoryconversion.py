print("Conversion of bits to MB,GB,TB")
bits = int(input("Enter no of bits="))
byte=bits/8
kb=byte/1024
mb=kb/1024
gb=mb/1024
tb=gb/1024
print("Megabites",mb)
print("Gigabites",gb)
print("Terabites",tb)