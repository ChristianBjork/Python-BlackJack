# random is used to deal the player or dealer a random number between 1, 11
import random

# time is used to make the game more player freindly
import time


class Dealer:

    # Lifecycle for a game as a dealer
    def dealer_game(dealer):
        
        # Empty cards for every new game

        #Dealer cards
        dealer_cards = []

        #Player cards
        player_cards = []


        if dealer == "deal":

            # Deal the cards
            # Display the cards
            # Dealer cards
            while len(dealer_cards) != 2:
                dealer_cards.append(random.randint(1, 11))
                if len(dealer_cards) == 2:
                    print("You have:   [ X &", dealer_cards[1],"]")

            # Deal the cards
            # Display the cards
            # Player cards
            while len(player_cards) != 2:
                player_cards.append(random.randint(1, 11))
                if len(player_cards) == 2:
                    print("Player has: [", player_cards[0], "&", player_cards[1], "]")

            # if sum player_cards are under 21
            if sum(player_cards) < 21:

                # run while sum player_Cards are under 21
                while sum(player_cards) < 21:
                    time.sleep(2)

                    # give the dealer a new card until the player_cards sum is over 14
                    if sum(player_cards) <= 14:
                        player_cards.append(random.randint(1,11))
                        print('Player: "Hit me!"')
                        print("Player now has a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
                    
                        # if sum player_cards is 21 --> Player wins
                        if sum(player_cards) == 21:
                            print("Player has BLACKJACK! Player Wins!")
                            print("-" * 40)

                        # if sum player_cards is higher than 21 --> Dealer wins    
                        elif sum(player_cards) > 21:
                            print("Player busted! YOU WIN")
                            print("-" * 40)

                    # if sum player_cards is over 14 and equal to dealer_Cards --> Dealer wins
                    elif (sum(player_cards) > 14 and sum(player_cards) == sum(dealer_cards)):
                        print('Player: "I stay!"')
                        time.sleep(2)
                        print("You have a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                        print("Player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                        print("YOU WIN!")
                        print("-" * 40)
                        break 

                    # if player_cards are higher than 14 
                    else:  
                        print('Player: "I stay!"')
                        time.sleep(2)

                        # if sum dealer_cards is 21 --> Dealer win 
                        if sum(dealer_cards) == 21:
                            print("You have BLACKJACK! " + str(sum(dealer_cards)) + " with ", dealer_cards)
                            print("Player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                            print("YOU WIN!")
                            print("-" * 40)
                            break

                        # if sum dealer_cards is higher than player_cards --> Dealer wins  
                        elif sum(dealer_cards) > sum(player_cards):
                            print("You have a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                            print("The player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                            print("YOU WIN!")
                            print("-" * 40)
                            break    

                        # if sum dealer_cards is not higher than player_cards    
                        else:
                            
                            # run while sum dealer_cards is under 21
                            while sum(dealer_cards) < 21:
                                print("You have: ", dealer_cards, " with a total of " + str(sum(dealer_cards)))
                                deal_a_card = str(input('The players cards are higher than yours, with a total of {}. Press "ENTER" to turn the next card '.format(sum(player_cards)) + "\n" + "-" * 40))
                                dealer_cards.append(random.randint(1, 11))

                                # if dealer_cards is higher than player_cards and under 21 --> Dealer wins
                                if(sum(dealer_cards) > sum(player_cards) and sum(dealer_cards) < 21):
                                    print("You have a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                                    print("Player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                                    print("YOU WIN!")
                                    print("-" * 40)
                                    break

                                # if sum of dealer_cards and player_cards are equal --> Dealer wins    
                                elif sum(dealer_cards) == sum(player_cards):
                                    print("You have a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                                    print("Player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                                    print("YOU WIN!")
                                    print("-" * 40)
                                    break

                                # if sum dealer_cards is 21 --> Dealer wins    
                                elif sum(dealer_cards) == 21:
                                    print("You have BLACKJACK! " + str(sum(dealer_cards)) + " with ", dealer_cards)
                                    print("Player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                                    print("YOU WIN!")
                                    print("-" * 40)

                                # if sum dealer_cards is over 21 --> Player wins    
                                elif sum(dealer_cards) > 21:
                                    print("You have Busted with " + str(sum(dealer_cards)), dealer_cards)
                                    print("Player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                                    print("PLAYER WINS!") 
                                    print("-" * 40)  

                            # if sum player_cards is higher than dealer_cards --> Player_wins         
                            if sum(player_cards) > sum(dealer_cards):
                                print("You have a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                                print("Player has a total of " + str(sum(player_cards)) + " with ", player_cards)
                                print("PLAYER WINS!")
                                print("-" * 40)

                            break
                            
             # if player receives 11, 11 in the first hand
            elif sum(player_cards) > 21:
                time.sleep(2)
                print("Player busted! YOU WIN")
                print("-" * 40)
            
            # if Player gets BLACKJACK in first hand
            elif sum(player_cards) == 21:
                time.sleep(2)
                print("You have BLACKJACK! You Win! 21")  
                print("-" * 40)
                Chips.win_bet(Player.chips)     