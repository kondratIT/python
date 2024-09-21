a= ["a","b"]

try:
    print(a[3])
except IndexError:
    print("IndexError happened -> nie ma takego elementu w liście")
except:
    print("Error but no IndexError")


#print(a[3])
