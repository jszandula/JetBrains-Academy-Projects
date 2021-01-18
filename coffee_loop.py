class CoffeMachine():
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
    def user_interaction(self, action = str(input("Write action (buy, fill, take, remaining, exit) : "))
 ):
        while action != 'exit':
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            else:
                self.remaining()
            action = str(input("Write action (buy, fill, take, remaining, exit) : "))

        exit()

    def buy(self):
        which_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back to main menu: ")
        if which_coffee == 'back':
            self.user_interaction(action = str(input("Write action (buy, fill, take, remaining, exit) : ")))
        elif int(which_coffee) == 1:
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.beans < 16:
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
        elif int(which_coffee) == 2:
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.beans < 20:
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
        else:
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.beans < 12:
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
    
    def fill(self):
        self. add_water = int(input("Write how many ml of water do you want to add: "))
        self.add_milk = int(input("Write how many ml of milk do you want to add: "))
        self.add_beans = int(input("Write how many grams of coffee beans do you want to add: "))
        self.add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
        self.water += self.add_water
        self.milk += self.add_milk
        self.beans += self.add_beans
        self.cups += self.add_cups

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0

    def remaining(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print("$" + str(self.money) + " of money")
        print()
 
coffee = CoffeMachine()
coffee.user_interaction()