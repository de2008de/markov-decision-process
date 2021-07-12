class State:
    def __init__(self, name, is_end=False):
        self.name = name
        self.actions = []
        self.is_end = is_end

    def add_action(self, name):
        action = Action(name)
        self.actions.append(action)
        return action


class Action:
    def __init__(self, name):
        self.name = name
        self.chance_node = None

    def create_chance_node(self):
        chance_node = ChanceNode()
        self.chance_node = chance_node
        return chance_node


class ChanceNode:
    def __init__(self):
        self.transitions = []

    def add_transition(self, rate, reward, next_state):
        transition = Transition(rate, reward, next_state)
        self.transitions.append(transition)


class Transition:
    def __init__(self, rate, reward, next_state):
        self.rate = rate
        self.reward = reward
        self.next_state = next_state


def value_iteration(states, start_state, discount_factor=1):
    values = {}
    policy = {}
    for state in states:
        values[state.name] = 0
    count = 0
    while True:
        for state in states:
            if state.is_end:
                continue
            max_value = None
            for action in state.actions:
                chance_node = action.chance_node
                action_value = 0
                for transition in chance_node.transitions:
                    action_value = action_value + transition.rate * \
                        (transition.reward + discount_factor *
                         values[transition.next_state.name])
                if max_value is None:
                    max_value = action_value
                    policy[state.name] = action.name
                elif action_value > max_value:
                    max_value = action_value
                    policy[state.name] = action.name
            values[state.name] = max_value
        # TODO: Change this to epsilon
        count = count + 1
        if count == 100:
            break
    return [values, policy]
