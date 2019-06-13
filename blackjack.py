# BlackJack game
# Github test this is a change hey what is this is change
import os
import random
import time
from chips import Chips
#The Planning Phase

player_chips = Chips()
  
    #Player Bet
def take_bet(chips):

    while True:
        try:
            print("Your chips total is: ", chips.total)
            chips.bet = int(input("How many chips would you like to bet?: "))  
        except ValueError:
            print("You have to bet an integer!")
        else:
            if chips.bet > chips.total:
                print("You bet can't be higher than your chips total: ", chips.total)
            elif chips.bet < 0:
                print("You can't bet a negative value!")
            else:
                break     

playing = True


while playing == True:
    #Dealer cards
    dealer_cards = []

    #Player cards
    player_cards = []

    dealer_or_player = str(input("Do you want do deal or play? "))


    if dealer_or_player == "play":
        take_bet(player_chips)
    
        #Deal the cards
        #Display the cards
        #Dealer cards    
        while len(dealer_cards) != 2:
            dealer_cards.append(random.randint(1, 11))
            if len(dealer_cards) == 2:
                print("Dealer has: [ X &", dealer_cards[1],"]")

        #Player cards
        while len(player_cards) != 2:
            player_cards.append(random.randint(1, 11))
            if len(player_cards) == 2:
                print("You have:   [", player_cards[0], "&", player_cards[1], "]")

            #Sum of the Player cards

        while sum(player_cards) < 21:
            action_taken = str(input("Do you want to stay or hit? "))
            if action_taken == "hit":
                player_cards.append(random.randint(1, 11))
                print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
            elif sum(dealer_cards) == 21:
                print("The dealer has BLACKJACK! " + str(sum(dealer_cards)) + " with ", dealer_cards)
                print("You have a total of " + str(sum(player_cards)) + " with ", player_cards) 
                print("Dealer Wins")   
                Chips.lose_bet(player_chips)
            else:   
                if sum(dealer_cards) > sum(player_cards):
                    print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                    print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
                    print("Dealer wins!")
                    Chips.lose_bet(player_chips)
                    break
                else:
                    while sum(dealer_cards) < 21:
                        dealer_cards.append(random.randint(1, 11))
                        if (sum(dealer_cards) > sum(player_cards) and sum(dealer_cards) < 21):  
                            print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                            print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
                            print("Dealer wins!")
                            Chips.lose_bet(player_chips)
                            break
                        elif sum(dealer_cards) == sum(player_cards):   
                            print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                            print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
                            print("Dealer wins!")
                            Chips.lose_bet(player_chips)
                            break
                        elif sum(dealer_cards) == 21:
                            print("The dealer has BLACKJACK! " + str(sum(dealer_cards)) + " with ", dealer_cards)
                            print("You have a total of " + str(sum(player_cards)) + " with ", player_cards) 
                            print("Dealer Wins")   
                            Chips.lose_bet(player_chips)
                            dealer_cards.append(1)
                        elif sum(dealer_cards) > 21:
                            print("The dealer has busted! " + str(sum(dealer_cards)) + " with ", dealer_cards)
                            print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
                            print("You Win!")
                            Chips.win_bet(player_chips)
                                
                    break

                    


        if sum(player_cards) > 21:
            print("You Busted! Dealer wins.")
            Chips.lose_bet(player_chips)
        elif sum(player_cards) == 21:
            print("You have BLACKJACK! You Win! 21")  
            Chips.win_bet(player_chips)  


        


    if dealer_or_player == "deal":
        while len(dealer_cards) != 2:
            dealer_cards.append(random.randint(1, 11))
            if len(dealer_cards) == 2:
                print("You have X & ", dealer_cards[1])

        # player cards
        while len(player_cards) != 2:
            player_cards.append(random.randint(1, 11))
            if len(player_cards) == 2:
                print("Player has ", player_cards)

        # sum of player cards
        while sum(player_cards) < 21:
            if sum(player_cards) < 14:
                player_cards.append(random.randint(1,11))
                print('Player: "Hit me!"')
                print("Player now has a total of " + str(sum(player_cards)) + " from these cards ", player_cards)

                if sum(player_cards) == 21:
                    print("Player has BLACKJACK! Player Wins!")
                elif sum(player_cards) > 21:
                    print("Player busted! You win")
            else:  
            
                if sum(dealer_cards) > sum(player_cards):
                    print("You have a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                    print("The player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                    print("You win!")
                    break    
                else:
                    while sum(dealer_cards) < 17:
                        deal_a_card = str(input('The players cards are higher than yours. Press "ENTER" to turn the next card '))
                        dealer_cards.append(random.randint(1, 11))

                        if(sum(dealer_cards) > sum(player_cards) and sum(dealer_cards) < 21):
                            print("You have a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                            print("Player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                            print("You win!")
                            break
                        elif sum(dealer_cards) == sum(player_cards):
                            print("You have a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                            print("Player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                            print("You win!")
                            break
                        elif sum(dealer_cards) == 21:
                            print("You have BLACKJACK! " + str(sum(dealer_cards)) + " with ", dealer_cards)
                            print("Player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                            print("You win!")
                        elif sum(dealer_cards) > 21:
                            print("You have Busted! " + str(sum(dealer_cards)) + " with ", dealer_cards)
                            print("Player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                            print("Player wins!")
                        print(str(sum(dealer_cards)))    
                    if sum(player_cards) > sum(dealer_cards):
                        print("You have a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                        print("Player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                        print("Player wins!")

                    break

    if player_chips.total == 0:
        playing = False
        print("You are out of Chips! Thank you for playing!")
    else:
        print("Thanks for playing! Your winnings stand at: ", player_chips.total, "Chips!")
        new_game = str(input('Would you like to play another game? Press "y" or "n"'))

        if new_game[0] == "y":
            playing = True
        else:    
            playing = False
            print("Thank you for playing!")
    
    
   