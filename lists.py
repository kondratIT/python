#[]
#list()

arr=[1,2,-5,36,-45,2]
mixed_arr1= [1,2,3,"string",True, None,7]
arr2 =["a","b","c"]

nestes_list=[[1,2,-5,36,-45,2],["a","b","c"]]

firstnames= ["Adam","Ewa","Magdalena","Jakub","Tomasz","Jan"]

print (firstnames[0])
print (firstnames)
print (firstnames[-1])

print(len(firstnames))

for index in range(len(firstnames)):
    print(f"Index:{index} Name {firstnames[index]}")

for firstname in firstnames:
    print(firstname[-1])

firstnames.append("Aleksander")

for firstname in firstnames:
    print(firstname)

firstnames.sort()
print(firstnames)

firstnames.insert(3,"Czarek")
print(firstnames)

firstnames = firstnames + firstnames
print(firstnames)

del firstnames[1]
print(firstnames)

firstnames.remove("Czarek")
print(firstnames)

while "Jan" in firstnames:
    firstnames.remove("Jan")

print(firstnames)

#remove duplicates 
firstnames = list(set(firstnames))
print(firstnames)
print(firstnames[1:3])

print(firstnames[::-1])#only for printing
firstnames.reverse # permanently change 
print(firstnames)
firstnames = firstnames + firstnames
print (firstnames.index("Ewa"))

empty_list=[]

if empty_list:
    print("list is not empty")
else:
    print("list is empty")







