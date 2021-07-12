from MDP import *


def main():
    state_in = State("in")
    state_end = State("end", is_end=True)
    states = [state_in, state_end]

    in_stay_chance = state_in.add_action("stay").create_chance_node()
    in_stay_chance.add_transition(rate=2/3, reward=4, next_state=state_in)
    in_stay_chance.add_transition(rate=1/3, reward=4, next_state=state_end)

    in_quit_chance = state_in.add_action("quit").create_chance_node()
    in_quit_chance.add_transition(rate=1, reward=10, next_state=state_end)

    [values, policy] = value_iteration(states, states[0])
    print(values)
    print(policy)


if __name__ == "__main__":
    main()
