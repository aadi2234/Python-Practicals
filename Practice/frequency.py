import collections
import pprint
file_input=input("Enter File Name:")
with open(file_input,'r') as fp:
    count=collections.Counter(fp.read().upper())
    value=pprint.pformat(count)
    print(value)