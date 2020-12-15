class Automaton():
    def __init__(self):
        # As transições são definidas pela relação entre um estado
        # e um dicionário de transições
        # Ex: __transitions = { "q0": { "a": "q1", "b": "q2" }, "q1" : { "a": "q0"}}
        self.__transitions = {}

        # Os estados finais são definidos por um dicionário
        # Ex: __final_states = {"q0": False, "q1": True, "q2": True}
        self.__final_states = {}

    def __init__(self, transitions, final_states):
        self.__transitions = transitions
        self.__final_states = final_states

    def set_transitions(self, transitions):
        self.__transitions = transitions

    def set_final_states(self, final_states):
        self.__final_states = final_states

    def get_transitions(self):
        return self.__transitions.copy()

    def get_final_states(self):
        return self.__final_states.copy()

    def add_transitions(self, new_transitions):
        for key in new_transitions:
            self.__transitions[key].update(new_transitions[key])
    
    def is_final(self, state):
        return self.get_final_states()[state]
