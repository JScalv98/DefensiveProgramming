class Ticket:
    def __init__(self, eventName, price):
        self.eventName = eventName
        self.price = price

    def info(self):
        print(self.eventName)
        print(self.price)

#test ticket just to see if it works
ticket = Ticket("Event1", 1)
ticketsList = [ticket]


startingPoints = 0
## We're storing the adminAccount as hardcoded string.
## This will be easy to find even when the python is compiled into an executable.
adminAccount = "admin"
adminPassword = 1649  ## astrongpassword
accountArray = [adminAccount, "guest", "james"]
passwordArray = {adminAccount: adminPassword, "guest": 883, "james": 1236}
## The admin password is going to be a number which is weak aganist a keygen.

ticketPointCost = 5
totalMoney = 100
userAccount = ""




def userChoiceHandler(userChoice):
    if userChoice == "1":
        register()
    elif userChoice == "2":
        login()
    elif userChoice == "3":
        doThis()
    elif userChoice == "4":
        purchaseTickets()
    elif userChoice == "5":
        doThis()
    elif userChoice == "6":
        doThis()
    else:
        print("Please Enter A Valid Answer")


def doThis():
    print("should probably do this")


def purchaseTickets():
    global ticketsList
    global totalMoney

    print("Here are the available events that you can purchase tickets for: ")
    print(ticketsList) #FIXME: need to fix this to print the names of each ticket, this does something weird
    print("Enter the name of the ticket to buy it, or enter quit to quit out.")
    choice = input()
    i = 0
    for i in ticketsList:

        if choice == i.eventName:
            selectedTicket = i
            if selectedTicket.price < totalMoney:
                totalMoney = totalMoney - selectedTicket.price
                print("You bought: " + selectedTicket.eventName)

        else:
            continue




def viewTransactions():
    print("No Transactions Yet")


def register():
    print("Please Enter Your Desired Username")
    newUser = input()
    if newUser in accountArray:
        print("That User Already Exists.")
        register()
    else:
        print("Please Pick A Secure Password")
        securePassword = input()
        print("User " + newUser + " Has Been Created.")
        passwordArray[newUser] = passwordToNumber(securePassword)
        accountArray.append(newUser)
        ##print(passwordArray)


def login():
    print("Enter A User")
    user = input()
    if user in accountArray:
        print("Enter A Password")
        password = input()
        if passwordChecker(password, user):
            print("Welcome " + user)
        else:
            print("Incorrect Password")
    else:
        print("We don't have that user please register.")


def passwordToNumber(password):
    sum = 0
    ## This loop takes the password variable and determines it's ascii value.
    for i in password:
        sum += ord(i)
    ##print(sum)
    return sum


def passwordChecker(password, user):
    sum = passwordToNumber(password)
    if passwordArray[user] == sum:
        ##print("true")
        return True
    else:
        ##print("false")
        return False


def start():
    userChoice = 0
    print("Welcome To Our Store.")
    print("We had it developed by a discount developer so it might be a litle buggy.")
    print("If you have any issues or need any help contact us at nerd@columbusstate.edu\n\n")
    print("Enter a number that matches your choice")
    while userChoice != "7":
        print("Register 1, Login 2, View Transactions 3, Purchase Tickets 4, Make A File 5, Run A File 6, Exit 7\n\n")
        userChoice = input()
        intUserChoice = int(userChoice)
        if userChoice == "7":
            print("bye")
            exit()
        else:
            userChoiceHandler(userChoice)


if __name__ == '__main__':
    start()
