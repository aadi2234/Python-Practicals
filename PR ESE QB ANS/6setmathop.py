#•	Write a Python program to perform following operations on set: intersection of sets,
#union of sets, set difference, symmetric difference, clear a set.
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print("Set=",s1)
print("Intersection=",s1&s2) #s1.intersection(s2)
print("Union=",s1|s2)	 #s1.union(s2)
c1=s1.difference(s2)     #c1=s1-s2
c2=s2.difference(s1)     #c2=s2-s1
print("Difference=",c2)
print("Symmetric Difference=",s1^s2)  #s1.symmetric_difference(s2)
print(s1)