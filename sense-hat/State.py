from time import sleep


class StateManager:

    def __init__(self, states):
        self.states = states
        self.current = 0

    def next(self):
        self.current = self.current + 1
        if self.current >= len(self.states) - 1:
            self.current = 0
        self.states[self.current].apply()
    
    def refresh(self):
        self.states[self.current].apply()
        sleep(2)


class State:

    def __init__(self, function):
        self.func = function

    def apply(self):
        self.func()

