from queue import deque


class SyntacticAnalysis:
    """
    Syntactic Analysis is a class that implements the syntactic analysis of a given input.
    """

    def __init__(self):
        self.__stack: deque = deque()
        self.__queue: deque = deque()

    def __shunting_yard(self, input_data: list = []) -> deque:
        """
        Shunting Yard is a method that implements the shunting yard algorithm to convert a given input into a postfix notation.
        Args:
            input_data (list): list of tuples containing:
                - bool: True if the input data is accepted, False otherwise
                - list: List of tuples containing:
                    - str: Token name
                    - str: Token value
                - list: List of error messages
        Returns:
            tuple: A tuple containing:
                - bool: True if the input data is accepted, False otherwise
                - list: List of errors messages
        """
        accepted: bool = True
        errors: list = []

        precedence: dict = {"NEG": 3, "DISJ": 2, "CONJ": 2, "COND": 1, "BICON": 1}

        # Enquanto existirem tokens a serem lidos
        for i, (token, value) in enumerate(input_data):
            # Se for um literal
            if token == "BIN" or token == "VAR":
                # Insere na fila de saída
                self.__queue.append((token, value))

            # Se for um parêntese
            elif token == "PAR":
                # Se for esquerdo
                if value == "(":
                    # Insere na pilha
                    self.__stack.appendleft((token, value))
                # Se for direito
                else:
                    opened_bracket: bool = False
                    # Enquanto a pilha não estiver vazia
                    while len(self.__stack) != 0:
                        # Saca o topo da pilha
                        top = self.__stack.popleft()
                        # Se for um parêntese esquerdo, descarte
                        if top[1] == "(":
                            opened_bracket = True
                            break
                        # Caso contrário, insira na fila de saída
                        self.__queue.append(top)
                    if not opened_bracket:
                        errors.append(f"Faltando '(' para  token {i+1}")
                        accepted = False

            # Se for um operador
            else:
                # Inicializa um Enum
                current_operator: int = precedence.get(token)

                # Enquanto a pilha não estiver vazia
                while len(self.__stack) != 0:
                    # Saca o topo da pilha
                    top_token, top_value = self.__stack.popleft()
                    if top_token == "PAR":
                        self.__stack.appendleft((top_token, top_value))
                        break
                    # Inicializa um Enum com o operador do topo
                    top_operator = precedence.get(top_token)
                    # Se o operador do topo for de maior precedência que o lido
                    if top_operator > current_operator:
                        # Insere na fila de saída
                        self.__queue.append((top_token, top_value))
                    # Caso contrário
                    else:
                        # Insere de volta ao topo dap pilha
                        self.__stack.appendleft((top_token, top_value))
                        # Sai do loop
                        break
                # Insere o token atual no topo da pilha
                self.__stack.appendleft((token, value))

        # Enquanto a pilha não estiver vazia
        while len(self.__stack) != 0:
            # Saca o topo da pilha
            top = self.__stack.popleft()
            # Insere na fila de saída
            self.__queue.append(top)

        return (accepted, errors.copy())

    def evaluate(self, input_data: list = []) -> tuple:
        """
        Evaluate is a method that evaluates a given input in postfix notation.
        Args:
            input_data (list): list of tuples representing the input data as:
                - str: Token name
                - str: Token value
        Returns:
            tuple: A tuple containing:
                - bool: True if the input data is accepted, False otherwise
                - list: List of tuples containing:
                    - str: Token name
                    - str: Token value
                - list: List of errors messages
        """
        # Executa Shunting Yard
        accepted, errors = self.__shunting_yard(input_data)
        aux_queue = self.__queue.copy()

        # Enquanto houverem tokens a serem lidos
        while len(aux_queue) != 0:
            # Lê o token
            token, value = aux_queue.popleft()
            # Se for um literal
            if token == "BIN" or token == "VAR":
                # Insere na pilha
                self.__stack.appendleft((token, value))

            # Se for uma negação
            elif token == "NEG":
                # Se houver ao menos um token na pilha
                if len(self.__stack) > 0:
                    # Lê o topo da pilha
                    first_token, first_value = self.__stack.popleft()
                    # Se não for binário ou varivável
                    if first_token != "BIN" and first_token != "VAR":
                        # Não é possível operar, joga um erro
                        errors.append(
                            f"Impossível operar {(token, value)} com {(first_token, first_value)}"
                        )
                        accepted = False
                        continue
                    # Cria um token equivalente a valoração da operação
                    res = ("VAR", f"({value} {first_value})")
                    # Insere o token na pilha
                    self.__stack.appendleft(res)
                # Se a pilha estiver vazia
                else:
                    # Não é possível operar, joga um erro
                    errors.append(f"Impossível operar {(token, value)}.")
                    accepted = False
                    continue
            # Se for um operador
            else:
                # Se houverem pelo menos 2 tokens na pilha
                if len(self.__stack) > 1:
                    # Lê o topo da pilha
                    second_token, second_value = self.__stack.popleft()
                    # Se não for binário ou varivável
                    if second_token != "BIN" and second_token != "VAR":
                        # Não é possível operar, joga um erro
                        errors.append(
                            f"Impossível operar {(token, value)} com {(second_token, second_value)}"
                        )
                        accepted = False
                        continue

                    # Lê o topo da pilha
                    first_token, first_value = self.__stack.popleft()
                    # Se não for binário ou varivável
                    if first_token != "BIN" and first_token != "VAR":
                        # Não é possível operar, joga um erro
                        errors.append(
                            f"Impossível operar {(token, value)} com {(first_token, first_value)}"
                        )
                        accepted = False
                        continue

                    # Cria um token equivalente a valoração da operação
                    res = ("VAR", f"({first_value} {value} {second_value})")
                    # Insere o token na pilha
                    self.__stack.appendleft(res)

                # Se houverem menos que 2 tokens na pilha
                else:
                    # Não é possível operar, joga um erro
                    errors.append(f"Impossível operar {(token, value)}.")
                    accepted = False
                    continue

        if accepted:
            return (True, self.__queue, None)
        return (False, None, errors)
