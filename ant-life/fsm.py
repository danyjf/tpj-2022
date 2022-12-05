import random

class State:
    def __init__(self, name) -> None:
        self.name = name

    def enter(self):
        print(f"Entering {self.name}")

    def update(self, entity):
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

    def update(self, entity):
        entity.search()

class GoHome(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, entity):
        print("Return Home")
        return super().update(entity)

class Dead(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, entity):
        print("Died")
        return super().update(entity)

class FSM:
    def __init__(self, states, transitions) -> None:
        self._states = states
        self._transitions = transitions

        self.current: State = self._states[0]
        self.end: State = self._states[-1]

    def update(self, event, entity):
        if event:
            trans = self._transitions.get(event)
            if trans and trans._from == self.current:
                self.current.exit()
                self.current = trans._to
                self.current.enter()
        self.current.update(entity)

        if self.current == self.end:
            self.current.exit()
            return False
        return True
