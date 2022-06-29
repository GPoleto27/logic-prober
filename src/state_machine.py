class Automaton():
    def __init__(self, transitions: dict = {}, final_states: dict = {}):
        # As transições são definidas pela relação entre um estado
        # e um dicionário de transições
        # Ex: __transitions = { "q0": { "a": "q1", "b": "q2" }, "q1" : { "a": "q0"}}
        self.__transitions = transitions

        # Os estados finais são definidos por um dicionário
        # Ex: __final_states = {"q0": False, "q1": True, "q2": True}
        self.__final_states = final_states

    def set_transitions(self, transitions: dict = {}) -> None:
        self.__transitions = transitions

    def set_final_states(self, final_states: dict = {}) -> None:
        self.__final_states = final_states

    def get_transitions(self) -> dict:
        return self.__transitions.copy()

    def get_final_states(self) -> dict:
        return self.__final_states.copy()

    def add_transitions(self, new_transitions: dict = {}) -> None:
        for key in new_transitions:
            self.__transitions[key].update(new_transitions[key])
    
    def is_final(self, state: str = "") -> bool:
        return self.get_final_states()[state]
