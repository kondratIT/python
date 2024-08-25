"""
if conditional:
    code line1
    code line2
else:
    code line 3
    code line 4

"""

#if condition:

if True:
    print(1)
    print("inside if")
print("outside if")


if 1==1 and 2==2:
    print("Condition is saisfied")


c="Simpletext"

if c:
    print(f"c excists, and value of c is: {c}")


c=""

if c:
    print(f"c excists, and value of c is: {c}")


num =2
if num%2:
    print(f"Number {num} is odd")
else:
    print(f"Number {num} is even")      


if num%2:
    print(f"Number {num} is odd")
    if num>10:
        print("Number is greater than 10")
    else:
        print("Number is smaller than 10")

else:
    print(f"Number {num} is even")      



#FizzBuzz task
#number is devidble by 5 print Frizz, and if devidble by 3 print  Buzz, if both print FizzBuzz

print("Please enter number")
number = int(input()) 

if number%5==0 or number%3==0:
    response =""
    if not number%5:
        response += "Fizz"
    if not number%3:
        response += "Buzz"
    print(response)
else:
    print(f"Number {number} is not FizzBuzz")



#sesound option

if number%15==0:
    print("FizzBuzz")
elif number%5==0:
    print("Fizz")
elif number%3==0:
    print("Buzz")
else:
    print(f"Number {number} is not FizzBuzz")



