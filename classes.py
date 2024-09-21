import datetime
#print(datetime.date.today().year)

class User:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = int(age)

    def printHello(self):
        print(f"Dzień dobry {self.firstname} {self.lastname}!")
    
    def printBye(self):
        print(f"Do widzenia {self.firstname}")
    
    def yearOfBirth(self):
        print(f"Rok urodzenia użytkowniaka {self.firstname} to: {datetime.date.today().year-self.age}")
    
    def get_age_to_days(self):
        return self.age*365 

marek = User("Marek", "Kondrat", "60")
marek.printHello()
marek.printBye()
marek.yearOfBirth()
print(marek.get_age_to_days())


class Logger:
    def __init__(self):
        self.log = []
    def add(self, msg):
        self.log.append(msg)
    def show(self):
        print("\n".join(self.log))
    def clear_log(self):
        self.log.clear()

logger = Logger()

logger.add("First message")
logger.add("Secound message")
logger.add("Third message")
logger.show()
logger.clear_log()
print("-----"*20)
logger.add("Fourth message")
logger.show()




