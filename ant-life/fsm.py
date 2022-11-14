import random

class State:
    def __init__(self, name) -> None:
        self.name = name

    def enter(self):
        print(f"Entering {self.name}")

    def update(self, object):
        pass

    def exit(self):
        pass

class Transition:
    def __init__(self, _from, _to) -> None:
        self._from = _from
        self._to = _to

class Search(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, object):
        object.search()

class GoHome(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, object):
        print("Return Home")
        return super().update(object)

class Dead(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, object):
        print("Died")
        return super().update(object)

class FSM:
    def __init__(self, states, transitions) -> None:
        self._states = states
        self._transitions = transitions

        self.current: State = self._states[0]
        self.end: State = self._states[-1]

    def update(self, event, object):
        if event:
            trans = self._transitions.get(event)
            if trans and trans._from == self.current:
                self.current.exit()
                self.current = trans._to
                self.current.enter()
        self.current.update(object)

        if self.current == self.end:
            self.current.exit()
            return False
        return True
