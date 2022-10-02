
class StateManager:

    def __init__(self, states):
        self.states = states
        self.current = 0

    def next(self):
        if self.current < len(self.states):
            next_index = self.current
        else:
            next_index = 0
        self.states[next_index].apply()


class State:

    def __init__(self, function):
        self.func = function

    def apply(self):
        self.func()

