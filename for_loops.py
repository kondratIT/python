#For loop
 
for i in range(0,6):
    print(f"Loop, i = {i}")

print("*"*25)

for i in range(2,14,2):
    print(f"Loop, i = {i}")

print("*"*25)

for i in range(22,12,-2):
    print(f"Loop, i = {i}")

print("*"*25)

for i in range(5):
    print(f"Loop, i = {i}")    

lista = ["a","b","c","d","e","f"]
print("*"*25)
for i in range(6,2):
    print(f"Loop, i = {lista[i]}")    

moj_input = input()
print(type(moj_input))
print(f"{moj_input}")
#print(f"{lista}")
print("*"*25)

if moj_input=="":
    print("enter")
int(moj_input)
print(type(moj_input))
print(f"{moj_input}")