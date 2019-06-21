class Chips:

    # If an instance of Chips is created the chips.total = 100 and chips.bet = 0
    def __init__ (self):
        self.total = 100
        self.bet = 0

    # When the game is won add the bet to the total
    def win_bet(self):
        self.total += self.bet    

    # When the game is lost subtract the bet from the total
    def lose_bet(self):
        self.total -= self.bet   

    # Ask the player, how much the player wants to bet
    def take_bet(self):

        #Unittests

        # if self.bet <= 0:
        #     raise ValueError("The bet is negative")

        # if type(self.bet) not in [int, float]:
        #     raise TypeError("You have to bet an int")    

        # self.bet = input("How many chips would you like to bet?: ")

        while True:
            try:
                #Place the bet
                print("Your chips total is: ", self.total)
                self.bet = int(input("How many chips would you like to bet?: "))  
            except ValueError:
                print("You have to bet a number!")
            else:
                if self.bet > self.total:
                    print("You bet can't be higher than your total amount of chips: ", self.total)
                elif self.bet < 0:
                    print("You can't bet a negative value!")
                else:
                    break     