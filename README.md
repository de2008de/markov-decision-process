# Markov Decision Process

Markov Decision Process (MDP) is a framework to model a scenario which actions will lead to random outcomes. The main components of MDP are:

- states

- actions

- chance nodes

- transition rates

I will use an example to illustrate the MDP concept.

# A Blue/Red Card Game

<img src="docs/imgs/card.svg" width="500" />

Suppose you have $10 on hand, and there is a deck of cards in front of you. You can choose to flip a card. The card has either a blue sword or a red heart picture on it. You can decide to flip a card, or quit the game with the $10 you have. If you choose to flip a card, there are two outcomes:

- If you flip a card that has a blue sword picture, you need to pay $20, and your game is over. 

- If you flip a card that as a red heart picture, you get $5, and you can decide to keep playing the game or quit the game.

Now, let's model this game using MDP.

## States

There are two states in this game, which are in and out. The in state means that you are still in the game, and this happens when you flip a red heart card, or when you just started the game. The out state means that you flipped a blue sword card and can no longer play this game, or you have decided to quit the game.

Let's use circles to represent states.

<img src="docs/imgs/in_out_states.png" width="500" />

## Actions

When you are at a state, you may have some available actions to perform. In MDP, you need to perform an action in a state to transit to another state. If a state has no available actions, you cannot transit to other states because you cannot do anything. As a result, a state with no actions is called **absorbing state** because it absorbs you and will not let you go.

When you are in the in state, you have two available:

- play

- quit

However, when you are in the out state, you do not have any available action. Therefore, we can say out state is an absorbing state or end state.

<img src="docs/imgs/in_out_actions.png" width="500" />
