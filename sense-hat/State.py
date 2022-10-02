
class StateManager:

    def __init__(self, states):
        self.states = states
        self.current = 0

    def next(self):
        if self.current >= len(self.states):
            self.current = 0
        self.states[self.current].apply()
        self.current = self.current + 1


class State:

    def __init__(self, function):
        self.func = function

    def apply(self):
        self.func()

