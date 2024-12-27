Card Game Engine: War

- Cards -> class
  - number value
  - suit (spades, clubs, hearts, diamonds)
- Deck -> class
  - holds the cards
- Two Players
  - hold cards -> array/list
  - take turn putting top card in the middle (of the table) to compare -> if statement
    - if player 1 card is higher, player 1 gets card
    - else if player 2 card is higher, player 2 gets card
    - else, in the event of a tie, go to war
    - logic for war (3 cards face down, compare 4th card with if statement)
    - what happens with cards that are won? bottom of array (cards in hand)? or in another array, then when no more cards in hand, shuffle and add to hand?
- Shuffle cards -> well they're in an array, so randomly sort it

- REMEMBER, you don't have to build it perfect at first (or optimally), just make it work since it's your first project and hobby


########################################
Notes for stepping away from the work:

The suits don't matter, you could simplify the lists by removing the requirement of storing and printing the suit value (I does add depth to the descriptions)

Ran into a bug where the players went to war but one player did not have enough cards to play war. I believe that is a loosing scenario for that player and the game would be over as that player ran out of cards.

Need to include logic to determine the winner of the game.