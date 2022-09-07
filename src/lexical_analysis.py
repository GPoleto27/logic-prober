from state_machine import Automaton
from string import ascii_letters


class LexicalAnalysis(Automaton):
    """
    Lexical analysis is a finite state machine that accepts or rejects a sequence of tokens
    """

    def __init__(self):
        # Define as transições descritas na imagem automato_base.png
        transitions: dict = {
            "q0": {
                "(": "q1",
                ")": "q1",
                "~": "q2",
                "0": "q3",
                "1": "q3",
                "\\": "q5",
                "/": "q7",
                ">": "q9",
                "=": "q10",
            },
            "q1": {},
            "q2": {},
            "q3": {},
            "q4": {},
            "q5": {
                "/": "q6",
            },
            "q6": {},
            "q7": {
                "\\": "q8",
            },
            "q8": {},
            "q9": {},
            "q10": {},
        }

        transitions.get("q0").update({letter: "q4" for letter in ascii_letters})
        transitions.get("q4").update({letter: "q4" for letter in ascii_letters})
        transitions.get("q4").update({num: "q4" for num in "0123456789"})

        # Define os estados finais
        final_states: dict = {
            "q0": False,
            "q1": True,
            "q2": True,
            "q3": True,
            "q4": True,
            "q5": False,
            "q6": True,
            "q7": False,
            "q8": True,
            "q9": True,
            "q10": True,
        }

        # Instancia o autômato com as transições e estados finais
        super(LexicalAnalysis, self).__init__(transitions, final_states)

        self.__error_messages: dict = {
            "q0": "Token inválido",
            "q5": "Esperado '/'.",
            "q7": "Esperado '\\'.",
        }

        self.__tokens: dict = {
            "q1": "PAR",
            "q2": "NEG",
            "q3": "BIN",
            "q4": "VAR",
            "q6": "DISJ",
            "q8": "CONJ",
            "q9": "COND",
            "q10": "BICON",
        }

    # Função para aceitar ou rejeitar uma sequência de tokens
    def evaluate(self, input_data: str) -> tuple:
        """
        Evaluate the input data
        Args:
            input_data (str): Input data to be evaluated
        Returns:
            tuple: A tuple containing:
                - bool: True if the input data is accepted, False otherwise
                - list: List of tuples containing:
                    - str: Token name
                    - str: Token value
                - list: List of error messages
        """

        # Define que a palavra será aceita
        accepted: bool = True
        # Array de tuplas de tokens aceitos e seus respectivos valores
        accepted_tokens: list = []
        # Array de mensagens de erro
        errors: list = []
        # Valor associado ao token
        value: str = ""

        # Trata a string, removendo espaços em branco e nova linha
        input_data: str = input_data.replace(" ", "").replace("\n", "")

        # Define o estado atual como o estado inicial
        current_state: str = "q0"
        # Define as transições como as transições do autômato
        transitions: dict = self.get_transitions()

        # Para cada caracter na sequência
        for char in input_data:
            try:
                # Define as transições atuais como as transições do estado atual
                current_transitions: dict = transitions[current_state]
                # Se não houver transição do estado atual que consuma o carater
                if not (char in current_transitions):
                    # Se o estado atual for final
                    if self.is_final(current_state):
                        # Adiciona o token e seu valor aos tokens aceitos
                        token: str = self.__tokens[current_state]
                        accepted_tokens.append((token, value))

                    # Se o estado atual não for final
                    else:
                        # O token não é aceito, pois não há transição naquele estado que consuma o caracter lido
                        accepted = False
                        # Adiciona mensagens de erros a serem retornadas
                        errors.append(
                            "Antes de '"
                            + char
                            + "': "
                            + self.__error_messages[current_state]
                        )

                    # Redefine o estado atual como o estado inical
                    current_state = "q0"
                    # Redefine o valor associado ao token como vazio
                    value = ""
                    # Tenta acessar as transições do estado atual
                    current_transitions = transitions[current_state]

                # Tenta acessar a transição que consome o caracter lido e transicionar o estado
                current_state = current_transitions[char]
                # Concatena o char ao valor associado ao token
                value += char

            # Se houver algum erro na transição entre os estados
            except:
                # O token não é aceito, pois não há transição naquele estado que consuma o caracter lido
                accepted = False
                # Adiciona mensagens de erros a serem retornadas
                errors.append(
                    "Em '" + char + "': " + self.__error_messages[current_state]
                )
                # Redefine o estado atual como o estado inical
                current_state = "q0"

        # Se o estado atual for final
        if self.is_final(current_state):
            # Adiciona o último token e seu valor aos tokens aceitos
            token = self.__tokens[current_state]
            accepted_tokens.append((token, value))

        # Após ler toda a entrada
        # a palavra é aceita se o estado atual for final e rejeitada caso contrário
        if self.is_final(current_state):
            if accepted:
                return (True, accepted_tokens, None)
        return (False, None, errors)
