empty_set= set()
sample_set = {"a","b","c",1,2,3,True} #every item in set are unique

print(sample_set)
print(empty_set)
set0 = {"a","b","c",1,2,3,True,1,2,3}#every item in set are unique
print(set0)


#set operations

s1= {"foo","bar","baz"}
s2= {"baz","qux","quux"}

print(s1.union(s2))
print(s1)
print(s2)
print("Diff")
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

s3 = {"a","b","c","d","e"}
s4 = {"a","b","d"}
print(s4.issubset(s3))
