#myvar = "something"
#_myvar = "something"
#_my_var = "something"
#myVar = "something"
#myvar2 = "something"
# 2var = "something"


"""
Variable types
"""
age = 15      #Intiger or int
Name = "Olek" #Srting or str
heihgt = 1.80    #Floating point number or float
isFamale = False    #Boolean or bool
#c =1j               #complex numbers
var = None


a = 15
b = 7

print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (a**b)
print (a%b)
print (b%a)
print (a//b) #Floor division zaokrąglene w dół
print (b/a)
print (b//a)

#Variable assingnment operation 
print (b)
b -= 5
print (b)

#bolean operaytions

a=5
b=5
c=10
print (a==b)
print (a==c)
print (a!=c)
print (a>=c)
print (a<c)
print ("*"*50)

#Logical operations

var1 =True
var2 =True
var3 =False
var4 =False

print(var1 and var2)
print(var1 and var3)
print(var3 and var4)
print ("*"*50)

print(var1 or var2)
print(var1 or var3)
print(var3 or var4)
print ("*"*50)

print(var3 or (var1 and var2))
print ("*"*50)

print(not False)
print(not True)
print ("*"*50)

#Differnt boolean values
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(1.3))
print(bool(0.0))

print ("*"*50)
#Differnt boolean values with string
print(bool("hello"))
print(bool("False"))
print(bool(""))
print(bool(" "))
print ("*"*50)
print(bool())
print(bool(None))

#Checking type
print ("*"*50)

print (1)
print ("1")


age = 15      #Intiger or int
Name = "Olek" #Srting or str
heihgt = 1.80    #Floating point number or float
isFamale = False    #Boolean or bool
#c =1j               #complex numbers
var = None

print(type(age))
print(type(Name))
print(type(heihgt))
print(type(isFamale))
print(type(var))

print ("*"*50)
print("Casting a Variables")
print (type(str(age)))
print(type(age))
print(age)
age = float(age)
print(type(age))
print(age)

print("Value: {}, Type: {}".format(age,type(age))) 

f=44.99
f= int(f)
print("Value: {}, Type: {}".format(f,type(f))) 
a=1
b=2
c=3

print(f"{a} {b} {c}")
a ,b ,c = 9 , 7, 5

print(f"{a} {b} {c}")























