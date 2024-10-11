## Our Blackjack Game House Rules

- The deck is unlimited in size. 
- There are no jokers. 
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- Use the following list as the deck of cards:

`cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.

 ### How the game works:

- If the computer and user both have the same score, then it's a draw.
- If the computer has a blackjack (0), then the user loses. 
- If the user has a blackjack (0), then the user wins. 
- If the <code>user_score</code> is over 21, then the user loses. 
- If the <code>computer_score</code> is over 21, then the computer loses. 
- If none of the above, then the player with the highest score wins.

### How the game ends:
Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack.





