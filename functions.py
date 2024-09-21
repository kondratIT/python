def my_first_function(imie):
    print(f"Dzień dobry {imie}")

my_first_function("Olek")
my_first_function("ziomeczku!")

def average_of_list(item: list, rounding: int):
    print(type(item))
    return round(sum(item) / len (item),rounding)

print(average_of_list([32,43,41,652,1,1,1,2,34],2))



def greet_people(greeting, *args):
    for name in args:
        print(f"{greeting} {name}")

greet_people("Hello", "Allice", "Bob", "Jackob", "Marcin")


def print_user_info(**kwargs):
    for key , value in kwargs.items():
        print(f"Key: {key}, Value: {value}")

print_user_info(name="Alice", age=35, isFemale=True, city="Warsaw")

print("-----"*20)
def custom_greet(message,*args,**kwargs):
    if args:
        message += " "+" ".join(args)
    if kwargs:
        message += " | "+"".join(f" {k}={v} "for k,v in kwargs.items())
    print(message)

custom_greet("Welcome", "Alice", "Bob", title="Dr", location="Hospital")
