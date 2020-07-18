import sys

class Coffee_machine():
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    state = 'choice'

    espresso_water_volume = 250
    espresso_grain_weigt = 16
    espresso_cost = 4

    latte_water_volume = 350
    latte_milk_volume = 75
    latte_grain_weigt = 20
    latte_cost = 7

    cappuccino_water_volume = 200
    cappuccino_milk_volume = 100
    cappuccino_grain_weigt = 12
    cappuccino_cost = 6

    def machine_work(self, input_string):
        self.state = input_string
        if self.state == 'choice':
            print("Write action (buy, fill, take, remaining, exit): ")
        else:
            if self.state == 'buy':
                coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
                if coffee == 'back':
                    self.state = 'choice'
                else:
                    self.buy(coffee)
            elif self.state == 'fill':
                self.fill()
            elif self.state == 'take':
                self.take()
            elif self.state == 'remaining':
                self.remaining()
            elif self.state == 'exit':
                sys.exit()
            else:
                print('Wrong choice!')

    def buy(self, number_of_coffee):
        if number_of_coffee == '1':
            if self.water < self.espresso_water_volume:
                print('Sorry, not enough water!')
                return False
            elif self.beans < self.espresso_grain_weigt:
                print('Sorry, not enough beans!')
                return False
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                self.water -= self.espresso_water_volume
                self.beans -= self.espresso_grain_weigt
                self.money += self.espresso_cost
                self.cups -= 1
                print('I have enough resources, making you a coffee!')
        elif number_of_coffee == '2':
            if self.water < self.latte_water_volume:
                print('Sorry, not enough water!')
                return False
            elif self.beans < self.latte_grain_weigt:
                print('Sorry, not enough beans!')
                return False
            elif self.milk < self.latte_milk_volume:
                print('Sorry, not enough milk!')
                return False
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                self.water -= self.latte_water_volume
                self.milk -= self.latte_milk_volume
                self.beans -= self.latte_grain_weigt
                self.money += self.latte_cost
                self.cups -= 1
                print('I have enough resources, making you a coffee!')
        elif number_of_coffee == '3':
            if self.water < self.cappuccino_water_volume:
                print('Sorry, not enough water!')
                return False
            elif self.beans < self.cappuccino_grain_weigt:
                print('Sorry, not enough beans!')
                return False
            elif self.milk < self.cappuccino_milk_volume:
                print('Sorry, not enough milk!')
                return False
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                self.water -= self.cappuccino_water_volume
                self.milk -= self.cappuccino_milk_volume
                self.beans -= self.cappuccino_grain_weigt
                self.money += self.cappuccino_cost
                self.cups -= 1
                print('I have enough resources, making you a coffee!')
        self.state = 'choice'
        self.machine_work(self.state)

    def fill(self):
        water_fill = int(input("Write how many ml of water do you want to add: "))
        milk_fill = int(input("Write how many ml of milk do you want to add: "))
        beans_fill = int(input("Write how many grams of coffee beans do you want to add: "))
        cups_fill = int(input("Write how many disposable cups of coffee do you want to add: "))
        self.water += water_fill
        self.milk += milk_fill
        self.beans += beans_fill
        self.cups += cups_fill
        self.state = 'choice'
        self.machine_work(self.state)

    def take(self):
        print(f"I gave you ${Coffee_machine.money}\n")
        self.money = 0
        self.state = 'choice'
        self.machine_work(self.state)

    def remaining(self):
        print(f"The coffee machine has:\n"
              f"{self.water} of water\n"
              f"{self.milk} of milk\n"
              f"{self.beans} of beans\n"
              f"{self.cups} of disposable cups\n"
              f"${self.money} of money\n")
        self.state = 'choice'
        self.machine_work(self.state)


if __name__ == "__main__":
    coffee_machine = Coffee_machine()
    coffee_machine.machine_work('choice')
    while True:
        coffee_machine.machine_work(input())
