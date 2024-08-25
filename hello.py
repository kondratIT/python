print ("Hello world")

#Text manipulation 
print ("Hello "+"world")

age = 23
Name= "Olek"
#print ("Hello "+age+"world") #incorrect
print ("Hello "+str(age)+" world")

print ("I'm %s years old, and again my %s" %(age,age)) #Old method

print ("I'm {} years old, and my name is {}".format(age,Name)) #NEW method


print ("I'm {myage} years old, and my name is {myname}".format(myname=Name,myage=age)) #NEW method

#Shorthand method

print(f"I'm {age} years old, and my name is {Name}")

var2=8.9877889787798
print(f"{round(var2,2)}")
print("%.2f" %var2)

#Escaping
print("My name is \"Olek\"")

#Newline
print("Line1 \nLine2")
print(f"Name: {Name}\nAge: {age}")

#Multiply string
print("*#+"*10)



