# random is used to deal the player or dealer a random number between 1, 11
import random
# time is used to make the game more player freindly
import time
from chips import Chips

class Player:

    # Create instans of Chips class
    # chips is now an Attribute of the class Player
    chips = Chips()

    # Lifecycle for a game as a player
    def player_game(player):
        
        # Empty cards for every new game
        
        # Player cards 
        player_cards = []
        # Dealer cards
        dealer_cards = []

        if player == "play":

            # Player makes the bet
            Chips.take_bet(Player.chips)

            # Deal the cards
            # Display the cards
            # Dealer cards    
            while len(dealer_cards) != 2:
                dealer_cards.append(random.randint(1, 11))
                if len(dealer_cards) == 2:
                    print("Dealer has: [ X &", dealer_cards[1],"]")

            # Deal the cards
            # Display the cards
            # Player cards
            while len(player_cards) != 2:
                player_cards.append(random.randint(1, 11))
                if len(player_cards) == 2:
                    print("You have:   [", player_cards[0], "&", player_cards[1], "]")
                    

            # Ask if the player wants to stay or hit while the player_card sum is under 21
            while sum(player_cards) < 21:
                
                # Ask player: stay or hit
                action_taken = str(input("Do you want to stay or hit? " + "\n" + "-" * 40))
                
                # Answer: hit --> give new card to the player    
                if action_taken == "hit":
                    player_cards.append(random.randint(1, 11))
                    print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
                
                # Answer: not hit and sum of dealer_cards == 21 --> dealer wins    
                elif sum(dealer_cards) == 21:
                    time.sleep(2)
                    print("The dealer has BLACKJACK! " + str(sum(dealer_cards)) + " with ", dealer_cards)
                    print("You have a total of " + str(sum(player_cards)) + " with ", player_cards) 
                    print("DEALER WINS!")   
                    print("-" * 40)
                    Chips.lose_bet(Player.chips)
                    break
                
                # Answer: stay 
                elif action_taken == "stay":   

                    # if sum of dealer_cards is higher than player_cards --> Dealer wins
                    if sum(dealer_cards) > sum(player_cards):
                        time.sleep(2)
                        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
                        print("DEALER WINS!")
                        print("-" * 40)
                        Chips.lose_bet(Player.chips)
                        break
                    else:

                        # If sum of dealer_cards is under 21 --> give dealer new card    
                        while sum(dealer_cards) < 21:
                            print("The dealer turns a card!")
                            time.sleep(2)
                            dealer_cards.append(random.randint(1, 11))
                            print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                            print("-" * 40)
                            time.sleep(2)

                            # If sum of dealer_cards is higher than player_cards and under 21 --> Dealer wins
                            if (sum(dealer_cards) > sum(player_cards) and sum(dealer_cards) < 21):  
                                print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                                print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
                                print("DEALER WINS!")
                                print("-" * 40)
                                Chips.lose_bet(Player.chips)
                                break

                            # If the sum of the cards are equal --> Dealer wins   
                            elif sum(dealer_cards) == sum(player_cards):   
                                print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                                print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
                                print("DEALER WINS!")
                                print("-" * 40)
                                Chips.lose_bet(Player.chips)
                                break

                            # If the sum of dealer_cards is 21 --> Dealer wins 
                            elif sum(dealer_cards) == 21:
                                print("The dealer has BLACKJACK! " + str(sum(dealer_cards)) + " with ", dealer_cards)
                                print("You have a total of " + str(sum(player_cards)) + " with ", player_cards) 
                                print("DEALER WINS!") 
                                print("-" * 40)  
                                Chips.lose_bet(Player.chips)
                            # If the sum of dealer_cards is higher than 21 --> You win
                            elif sum(dealer_cards) > 21:
                                print("The dealer has busted! with " + str(sum(dealer_cards)), dealer_cards)
                                print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
                                print("YOU WIN!")
                                print("-" * 40)
                                Chips.win_bet(Player.chips)
                                    
                        break

                # If player answer is not equal to stay or hit        
                else:
                    print('That is not possible, you have to enter "stay" or "hit"!')

            # If the sum of player_cards is higher than 21 --> Dealer wins
            if sum(player_cards) > 21:
                time.sleep(2)
                print("YOU BUSTED! DEALER WINS!")
                print("-" * 40)
                Chips.lose_bet(Player.chips)

            # You have BLACKJACK    
            elif sum(player_cards) == 21:
                time.sleep(2)
                print("You have BLACKJACK! You Win! 21")  
                print("-" * 40)
                Chips.win_bet(Player.chips)  