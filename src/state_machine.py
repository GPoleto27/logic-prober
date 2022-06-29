class Automaton:
    def __init__(self, transitions: dict = {}, final_states: dict = {}):
        """
        Initialize the automaton with the given transitions and final states.
        Args:
            transitions (dict): Transitions are defined by the relation of an state and a dictionary of transitions.
            Ex: __transitions = { "q0": { "a": "q1", "b": "q2" }, "q1" : { "a": "q0"}}
            final_states (dict): Final states are defined by the relation of an state and a boolean.
            # Ex: __final_states = {"q0": False, "q1": True, "q2": True}
        """
        self.__transitions = transitions
        self.__final_states = final_states

    def set_transitions(self, transitions: dict = {}) -> None:
        """
        Set the transitions of the automaton.
        Args:
            transitions (dict): Transitions are defined by the relation of an state and a dictionary of transitions.
            Ex: __transitions = { "q0": { "a": "q1", "b": "q2" }, "q1" : { "a": "q0"}}
        """
        self.__transitions = transitions

    def set_final_states(self, final_states: dict = {}) -> None:
        """
        Set the final states of the automaton.
        Args:
            final_states (dict): Final states are defined by the relation of an state and a boolean.
            # Ex: __final_states = {"q0": False, "q1": True, "q2": True}
        """
        self.__final_states = final_states

    def get_transitions(self) -> dict:
        """
        Get the transitions of the automaton.
        Returns:
            dict: Transitions set on the automaton.
            Transitions are defined by the relation of an state and a dictionary of transitions.
            Ex: __transitions = { "q0": { "a": "q1", "b": "q2" }, "q1" : { "a": "q0"}}
        """
        return self.__transitions.copy()

    def get_final_states(self) -> dict:
        """
        Get the final states of the automaton.
        Returns:
            dict: Final states set on the automaton.
            Final states are defined by the relation of an state and a boolean.
            # Ex: __final_states = {"q0": False, "q1": True, "q2": True}
        """
        return self.__final_states.copy()

    def add_transitions(self, new_transitions: dict = {}) -> None:
        """
        Add the given transitions to the automaton.
        Args:
            new_transitions (dict): Transitions to be added to the automaton.
            Transitions are defined by the relation of an state and a dictionary of transitions.
        """
        for key in new_transitions:
            self.__transitions[key].update(new_transitions[key])

    def is_final(self, state: str = "") -> bool:
        """
        Check if the given state is a final state.
        Args:
            state (str): State to be checked.
        Returns:
            bool: True if the state is a final state, False otherwise.
        """
        return self.get_final_states()[state]
