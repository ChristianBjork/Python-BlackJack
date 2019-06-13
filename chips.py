class Chips:

    def __init__ (self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet    

    def lose_bet(self):
        self.total -= self.bet   

            
    def take_bet(self):

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