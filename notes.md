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

The code doesn't know the value of Jack, Queen, King or Ace
We need to define their numerical value with a list? dictionary? what is the difference? What is a dictionary?

We need to make it loop through the player's hands. Currently it runs for one round and then the code ends
Ways to loop
Have another level of ifs that compare the number of cards in each player's hands at the end of this logic that exits the program if either player's hands drop to zero
There is probably a way to use a while loop to make the comparision, that way you aren't reading a really long list of if statements (makes it more obvious it is the game loop)

