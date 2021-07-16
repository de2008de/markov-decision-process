# Markov Decision Process

Markov Decision Process (MDP) is a framework to model a scenario which actions will lead to random outcomes. The main components of MDP are:

- states

- actions

- chance nodes

- transition rates

I will use an example to illustrate the MDP concept.

# A Blue/Red Card Game

Suppose you have $10 on hand, and there is a deck of cards in front of you. You can choose to flip a card. The card has either a blue sword or a red heart picture on it. You can decide to flip a card, or quit the game with the $10 you have. If you choose to flip a card, there are two outcomes:

- If you flip a card that has a blue sword picture, you need to pay $20, and your game is over. 

- If you flip a card that as a red heart picture, you get $5, and you can decide to keep playing the game or quit the game.

Now, let's model this game using MDP.

There are two states in this game, which are in and out. The in state means that you are still in the game, and this happens when you flip a red heart card, or when you just started the game. The out state means that you flipped a blue sword card and can no longer play this game.



