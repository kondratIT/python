#tuple is not modifiable after creation

tup1 = (1,2,3,4,5)
tup2 = 1,2,3,4,5,6,7,8,9
tup3 = tuple(["a","b","c","d"])

print(f"{tup1},{tup2},{tup3}")
print(tup1[2])
print(tup1[2:4])
print(tup1[-1])


#tup1[2]=7
#del tup1[2]
print(tup1)
del tup1 #delete tup1

tup4 = tup2 + tup3[2:4]
print(tup4)

print(len(tup4))
print(min(tup2))
print(max(tup2))


