#55.	Input a set from user and perform all operations on it.
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print("Set=",s1)
print("Is Dis-Joint:",s1.isdisjoint(s2))
print("Is Subset:",s2.issubset(s1))
print("Is Superset:",s1.issuperset(s2))
print("Intersection=",s1&s2) #s1.intersection(s2)
print("Union=",s1|s2)	 #s1.union(s2)
c1=s1.difference(s2)     #c1=s1-s2
c2=s2.difference(s1)     #c2=s2-s1
print("Difference=",c2)
print("Symmetric Difference=",s1^s2)  #s1.symmetric_difference(s2)
s1.clear()
print(s1)