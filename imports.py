class Klasa:
    def __init__(self, account_balance:float):
        self.account_balance = float(account_balance)
        self.list_of_command = []    

    def addCommandToList(self, command:str):
        self.list_of_command.insert(len(self.list_of_command),command)

    def displayListOfCommandRange(self, from_position:int, to_position:int):
        print(f"List of command:\n")
        for inex in range(from_position,to_position):
            print(f"{self.list_of_command[inex]}")
        
    def displayListOfCommand(self):
        print(f"List of command:\n{self.list_of_command}")


balans= 1231

egzemplarz = Klasa(balans)

egzemplarz.addCommandToList("dupa")
egzemplarz.addCommandToList("dupa1")
egzemplarz.addCommandToList("dupa2")
egzemplarz.addCommandToList("dupa3")


egzemplarz.displayListOfCommand()
print("*"*50)
egzemplarz.displayListOfCommandRange(2,3)