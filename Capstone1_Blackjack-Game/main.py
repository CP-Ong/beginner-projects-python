# import libraries
import art
import random

# start the while loop (ask user if they want to play a game of Blackjack)
continue_playing = True

while continue_playing:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    print("\n" * 20)

# print the Blackjack logo from art.py
    if play == 'y':
        print(art.logo)

        # Setup cards (equal probability)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        # print out first two cards drawn by user and their sum
        drawn_user = [random.choice(cards), random.choice(cards)]
        current_score_user = sum(drawn_user)

        print(f"    Your cards: {drawn_user}, current score: {current_score_user}")

        # print out computer's first card
        current_drawn_computer = [random.choice(cards)]
        print(f"    Computer's first card: {current_drawn_computer[0]}")

        less_than_seventeen = True

        # dealer draws a card until the sum is more than or equal to 17
        while less_than_seventeen:
            if sum(current_drawn_computer) < 17:
                current_drawn_computer.append(random.choice(cards))
            elif sum(current_drawn_computer) > 21 and cards[0] in current_drawn_computer:
                index_ace_computer = current_drawn_computer.index(cards[0])
                current_drawn_computer[index_ace_computer] = 1
            else:
                final_drawn_computer = current_drawn_computer
                final_score_computer = sum(final_drawn_computer)
                less_than_seventeen = False

        # outcome of the game depending on choice of user to get another card
        less_than_twenty_one = True

        # start the while loop (different situations depending on score, i.e. > or < 21)
        while less_than_twenty_one:

            # asks user if they want to get another card
            another_card_or_not = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            # if user wants another card
            if another_card_or_not == 'y':
                drawn_user.append(random.choice(cards))
                new_score = sum(drawn_user)

                # user continues to decide if they want another card iff sum does not exceed 21
                if new_score <= 21:
                    print(f"    Your cards: {drawn_user}, current score = {new_score}")
                    print(f"    Computer's first card: {current_drawn_computer[0]}")

                # convert the value of the ace card from 11 into 1 if sum exceeds 21
                elif new_score > 21 and cards[0] in drawn_user:
                    index_ace_user = drawn_user.index(cards[0])
                    drawn_user[index_ace_user] = 1
                    updated_score_user = new_score - 10
                    print(f"    Your cards: {drawn_user}, current score = {updated_score_user}")
                    print(f"    Computer's first card: {current_drawn_computer[0]}")

                # user loses if sum exceeds 21
                elif new_score > 21:
                    final_drawn_computer = current_drawn_computer
                    final_score_computer = sum(final_drawn_computer)
                    print(f"    Your final hand: {drawn_user}, final score = {new_score}")
                    print(f"    Computer's final hand: {final_drawn_computer}, "
                          f"final score: {final_score_computer}")
                    print("You went over. You lose! :(")
                    less_than_twenty_one = False

            # user does not want another card
            elif another_card_or_not == "n":
                final_drawn_user = drawn_user
                final_score_user = sum(drawn_user)
                final_drawn_computer = current_drawn_computer
                final_score_computer = sum(final_drawn_computer)
                print(f"    Your final hand: {final_drawn_user}, final score: {final_score_user}")
                print(f"    Computer's final hand: {final_drawn_computer}, final score: {final_score_computer}")

                # different outcomes depending on final scores
                if final_score_computer == final_score_user:
                    print("It's a draw!")
                elif final_score_computer == 21 and len(final_drawn_computer) == 2:
                    print("You lose! Computer wins with a Blackjack! :(")
                elif final_score_user == 21 and len(final_drawn_user) == 2:
                    print("You win with a Blackjack! :)")
                elif final_score_user < final_score_computer <= 21:
                    print("You lose! :(")
                elif final_score_computer > final_score_user and final_score_computer > 21:
                    print("You win! :)")
                elif final_score_computer < final_score_user:
                    print("You win! :)")

                # stop the while loop
                less_than_twenty_one = False

    # user does not want to play the game
    elif play == 'n':
        print("No Blackjack game for you! :(")
        continue_playing = False

    # user typed something other than 'y' and 'n' when asked if they want to play the game
    else:
        print("Invalid input!")
        continue_playing = False
