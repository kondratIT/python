





my_number= 26
print("Spróbuj zganąć moją liczbę od 0-30. \nGive me number?")
number= int(input())
number=26 # skomneowac tą linie aby działao
while my_number!=number:
    if number>my_number:
        print("Moja liczba jest mniejsza")
    else:
        print("Moja liczba jest wieksza")
    print("podaj kolejną liczbę")
    number= int(input())

print(f"Input number:")
number= int(input())

x= number//2
factor = 0
while x>1:
    if number%x ==0:
        print(f"{number} has factor {x}")
        factor =x
    x-=1
if not factor:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")


#silnia

counter = 0
product = 1
while  counter < 10:
    counter +=1
    product *= counter
    if product >1000:
        print("Braek of loop")
        break
    print(f"{counter}, {product}")


counter = 0

while  counter<10:
    counter += 1 
    if counter >=5 and counter <7:
        continue
    print (counter)
    
