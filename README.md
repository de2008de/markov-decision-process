# Markov Decision Process

Markov Decision Process (MDP) is a framework to model a scenario which actions will lead to random outcomes. The main components of MDP are:

- states

- actions

- chance nodes

- transition rates

I will use an example to illustrate the MDP concept.

# A Blue/Red Card Game

<img src="docs/imgs/card.svg" width="500" />

Suppose there is a deck of cards in front of you. You can choose to flip a card. The card has either a blue sword or a red heart on it. You can decide to flip a card, or quit the game and get $10. If you choose to flip a card, there are two outcomes:

- If you flip a card that has a blue sword picture, you need to pay $20, and your game is over. 

- If you flip a card that has a red heart picture, you get $5, and you can decide to keep playing the game or quit the game.

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

## Chance Nodes

If you take an action of Play, the outcome is random and depends on the probability. We call the probability from one state to another state transition rate. A characteristic of Markov Decision Process is that we incorporate randomness into the model. Therefore, we introduce chance nodes here to represent the randomness of outcomes.

The probability of flipping a blue sword card depends on the number of blue sword cards and the number of red heart cards in the deck. Let's assume that the numbers of both the blue sword and the read heart cards are the same. Hence, the probability of flipping a blue sword or a red heart card is 50%.

Also, if you take an action of Quit, although we know that taking an action of Quit will result in immediate out state, we can still use a chance node to represent it by giving it 100% chance leading to the out state.

<img src="docs/imgs/in_out_chance_nodes.png" width="500" />

## Rewards

For each outcome, there is an associated reward. For example, if you take an action of Play and flip a red heart card, you earn a reward of $5. On the other hand, if you flip a blue sword card, you get a punishment of $20, so your reward is a negative number -$20.

We represent rewards with its transition rate together using a bracket. For example, for taking an action of Play and flip a red heart card, we use this notation (1/2, 5) to represent the transition rate and the associated reward.

<img src="docs/imgs/in_out_rewards.png" width="500" />

Now, we have a MDP model for this game. We want to find the optimal policy $\pi_{opt}$ that tells us the optimal action for each state. The policy $\pi_{opt}$ is a mapping between states and actions. Given a state to the policy $\pi$, it returns an optimal action for the given state.

We can use value iteration algorithm to find the optimal policy $\pi_{opt}$.

## Utility

The utility is the sum of reward of a policy. For example, if your policy is always playing the game until you flip a blue sword card, one of your game may be like this:

[in; play, 5, in; play, 5, in; play, -20, end]

The utility of the policy for **this game** is: 

5 + 5 - 20 = -10

You kept playing the game, and you flipped a red heart card for the first two rounds. However, you were not so lucky for the third round because you flipped a blue sword card. Therefore, you paid a fine, and the game is ended.

## Discounted Factor

The discounted factor is a ratio to discount the future rewards. For example, it is better to get $100 today than next year because I can spend that money right now. The same concept can be applied to the utility. If we want to get more utility as early as possible, we can apply the discounted factor.

For instance, if the next reward is only worth 80% of the today's reward, the discounted factor is 0.8. By applying the discounted factor to the example above, we will have this utility:

5 + (0.8)*5 + ((0.8)^2)*5 + ((0.8^3))(-20) = 1.96

Now the utility is different because we care more about getting rewards as early as possible.

## Value

Value is the expected utility of a policy. For Markov Decision Process model, we know that each action will lead to some possible outcomes, and those outcomes are determined by chance. Therefore, for each different game of the same policy, you would get different amount of utility.

You can compute an expected utility of the policy if you know the transition rates of each outcome when an action is taken. The expected utility is called value.

# Value Iteration

Value iteration is an algorithm to iteratively compute the value of each state. The basic idea of value iteration is to iteratively update the value of each state. We initialize the value of each state to be a random number, usually zero. Then, we iterate each state. For each state, we iterate its actions. Each action has one or more transition rates and successor states. We calculate the value of the action using the formula mentioned above:

```
transition rate * transition reward + discount factor * value of next state
```

Note that the value of next state comes from our value table for each state. Initially they are all zero. However, they will be updated iteratively through the process.

After we iterate all actions and get their values, we choose the action that will yield the highest value. Then,

- Store the action in the policy table for the current state. 

- Store the value in the value table for this state as the current estimated optimal value. We will use this value when we need the value of next state.

For the value iteration algorithm code, please check this [MDP.py](./MDP.py).
