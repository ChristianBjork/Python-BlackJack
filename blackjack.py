# BlackJack game
import random
import time
from chips import Chips
from player import Player
from dealer import Dealer


print('''
WELCOME TO THE BLACKJACK TABLE
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

''')

#Start the game    
while True:
        #Dealer cards
        dealer_cards = []

        #Player cards
        player_cards = []

        #Choose to be a player or dealer
        dealer_or_player = str(input('Press "deal" to deal or press "play" to play!' + "\n" + "-" * 40))

        #This will be executed if dealer_or_player == "play"
        Player.player_game(dealer_or_player)
        
        #This will be executed if dealer_or_player == "deal"
        Dealer.dealer_game(dealer_or_player)

        #The will be executed if the users answer is different from "play" and "deal"
        if ("play" != dealer_or_player != "deal") :
            print("I'm sorry, that is not possible, you can only deal or play.\n")
            continue    


        #Player chooses if he/she wants to play another game of blackjack
        #If the Player runs out of chips, the game will end automaticly  
        if dealer_or_player == "play":
            if Player.chips.total == 0:
                time.sleep(2)
                print("You are out of Chips! Thank you for playing!")
                break
            else:
                time.sleep(2)
                print("Your winnings stand at: ", Player.chips.total, "Chips! $$$")
                new_game = str(input('Would you like to play another game? Press "y" or "n"'))

                if new_game != "y":
                    print("Thank you for playing!")
                    break
        
        #Dealer chooses if he/she wants to play another game of blackjack
        elif dealer_or_player == "deal":
            time.sleep(2)
            new_game = str(input('Would you like to play another game? Press "y" or "n"'))

            if new_game != "y":
                print("Thank you for playing!")
                break


   