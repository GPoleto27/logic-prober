from queue import deque
from turtle import clear

global env
global evaluations

# env will hold variable values associated with their names and work as recursive backtracking
env = {}
evaluations = {}

class Expression:
    """
    Expression is a class that represents a logical expression.
    """

    pass


"""# Operands"""


class Operand(Expression):
    """
    Operand is a class that represents a logical operand.
    """

    def __str__(self):
        global env
        return str(env[self._value])


class Binary(Operand):
    """
    Binary is a class that represents a logical binary operand.
    """

    def __init__(self, value: str):
        global evaluations 
        self._value = value

        env[value] = evaluations[value] = (value == "1")
        

    def evaluate(self) -> bool:
        """
        Evaluate is a method that evaluates a logical binary operand.
        Returns:
            bool: The logical value of the operand
        """
        global evaluations
        return evaluations[self._value]


class Variable(Operand):
    """
    Variable is a class that represents a logical variable.
    """

    def __init__(self, value: str):
        global env
        
        self._value = value
        env[value] = False

    def evaluate(self) -> bool:
        """
        Evaluate is a method that evaluates a logical variable.
        Returns:
            bool: The logical value of the variable
        """
        global env
        return env[self._value]


"""# Operations"""


class Operation(Expression):
    """
    Operation is a class that represents a logical operation.
    """

    pass


class UnaryOperation(Operation):
    """
    UnaryOperation is a class that represents a logical unary operation.
    """

    def __init__(self, l_value: Expression):
        self._l_value = l_value


class BinaryOperation(Operation):
    """
    BinaryOperation is a class that represents a logical binary operation.
    """

    def __init__(self, l_value: Expression, r_value: Expression):
        self._l_value = l_value
        self._r_value = r_value


"""### Unary Operations"""


class Not(UnaryOperation):
    """
    Not is a class that represents a logical not operation.
    """

    def evaluate(self) -> bool:
        """
        Evaluate is a method that evaluates a logical not operation.
        Returns:
            bool: The logical value of the operation
        """
        global evaluations
        if not (str(self) in evaluations.keys()):
            
            evaluations[str(self._l_value)] = self._l_value.evaluate()
            evaluations[str(self)] = not evaluations[str(self._l_value)]
        return evaluations[str(self)]

    def __str__(self):
        return f"~({str(self._l_value)})"


"""### Binary Operations"""


class And(BinaryOperation):
    """
    And is a class that represents a logical and operation.
    """

    def evaluate(self) -> bool:
        """
        Evaluate is a method that evaluates a logical and operation.
        Returns:
            bool: The logical value of the operation
        """
        global evaluations
        if not (str(self) in evaluations.keys()):
            evaluations[str(self._l_value)] = self._l_value.evaluate()
            evaluations[str(self._r_value)] = self._r_value.evaluate()
            evaluations[str(self)] = evaluations[str(self._l_value)] and evaluations[str(self._r_value)]
        return evaluations[str(self)]

    def __str__(self):
        return f"({str(self._l_value)})/\\({str(self._r_value)})"


class Or(BinaryOperation):
    """
    Or is a class that represents a logical or operation.
    """

    def evaluate(self) -> bool:
        """
        Evaluate is a method that evaluates a logical or operation.
        Returns:
            bool: The logical value of the operation
        """
        global evaluations
        if not (str(self) in evaluations.keys()):
            evaluations[str(self._l_value)] = self._l_value.evaluate()
            evaluations[str(self._r_value)] = self._r_value.evaluate()
            evaluations[str(self)] = evaluations[str(self._l_value)] or evaluations[str(self._r_value)]
        return evaluations[str(self)]

    def __str__(self):
        return f"({str(self._l_value)})\\/({str(self._r_value)})"


class Conditional(BinaryOperation):
    """
    Conditional is a class that represents a logical conditional operation.
    """

    def evaluate(self) -> bool:
        """
        Evaluate is a method that evaluates a logical conditional operation.
        Returns:
            bool: The logical value of the operation
        """
        global evaluations
        if not (str(self) in evaluations.keys()):
            evaluations[str(self._l_value)] = self._l_value.evaluate()
            evaluations[str(self._r_value)] = self._r_value.evaluate()
            evaluations[str(self)] = not evaluations[str(self._l_value)] or evaluations[str(self._r_value)]
        return evaluations[str(self)]

    def __str__(self):
        return f"({str(self._l_value)})>({str(self._r_value)})"


class Biconditional(BinaryOperation):
    """
    Biconditional is a class that represents a logical biconditional operation.
    """

    def evaluate(self) -> bool:
        """
        Evaluate is a method that evaluates a logical biconditional operation.
        Returns:
            bool: The logical value of the operation
        """
        global evaluations
        if not (str(self) in evaluations.keys()):
            evaluations[str(self._l_value)] = self._l_value.evaluate()
            evaluations[str(self._r_value)] = self._r_value.evaluate()
            evaluations[str(self)] = evaluations[str(self._l_value)] == evaluations[str(self._r_value)]
        return evaluations[str(self)]

    def __str__(self):
        return f"({str(self._l_value)})=({str(self._r_value)})"


"""## Evaluate expression"""


class SemanticAnalysis(Expression):
    """
    SemanticAnalysis is a class that represents a logical semantic analysis.
    """

    def __init__(self, expression: deque = None):
        global env
        env = {}

        self.__results = []
        self.__expression = None

        stack = deque()

        classes = {
            "NEG": Not,
            "BIN": Binary,
            "VAR": Variable,
            "DISJ": Or,
            "CONJ": And,
            "COND": Conditional,
            "BICON": Biconditional,
        }

        # Executa o parsing da expressão
        while len(expression) != 0:
            # Pega o elemento da expressão a ser analisado
            token, value = expression.popleft()

            # Verifica se o token é um operando
            if issubclass(classes[token], Operand):
                # Se for, adiciona o operando na pilha
                stack.appendleft(classes[token](value))

            # Verifica se o token é uma operação unária
            elif issubclass(classes[token], UnaryOperation):
                # Se for, pega a expressão no topo da pilha
                l_value = stack.popleft()
                # Adiciona a operação com a expressão no topo da pilha
                stack.appendleft(classes[token](l_value))

            # Verifica se o token é uma operação binária
            elif issubclass(classes[token], BinaryOperation):
                # Se for, pega as duas expressões no topo da pilha
                r_value = stack.popleft()
                l_value = stack.popleft()
                # Adiciona a operação com as expressões no topo da pilha
                stack.appendleft(classes[token](l_value, r_value))

            # Token desconhecido
            else:
                raise Exception("Token inválido, você executou a análise semântica sem antes executar as análises léxica e sintática?")

        self._vars = list(env.keys())
        # Pega a expressão no topo da pilha
        self.__expression = stack.popleft()

    def evaluate(self) -> list:
        """
        Evaluate is a method that evaluates every combination of variable values of logical expression.
        Returns:
            list: The truth table of the expression
        """
        global env
        global evaluations
        # Pega o número de variáveis da expressão
        n: int = len(env)

        # Gera as combinações de variáveis da expressão
        combinations = [
            num for num in ("{0:b}".format(p).zfill(n) for p in range(2**n))
        ]

        # Itera sobre as combinações
        for combination in combinations:
            # Atribui os valores das variáveis da combinação
            for i, var in enumerate(self._vars):
                env[var] = combination[i] == "1"

            # Adiciona o resultado da combinação na lista de resultados
            self.__results.append(self.__expression.evaluate())
        #print(evaluations)

        # Retorna a lista de resultados da expressão
        return self.__results.copy()

    def is_tautology(self) -> bool:
        """
        is_tautology is a method that checks if the expression is a tautology.
        Returns:
            bool: True if the expression is a tautology, False otherwise
        """
        # Verifica se todos os resultados da expressão são verdadeiros
        return all(self.__results)

    def is_contradiction(self) -> bool:
        """
        is_contradiction is a method that checks if the expression is a contradiction.
        Returns:
            bool: True if the expression is a contradiction, False otherwise
        """
        # Verifica se todos os resultados da expressão são falsos
        return all(not self.__results)

    def is_satisfiable(self) -> bool:
        """
        is_satisfiable is a method that checks if the expression is satisfiable.
        Returns:
            bool: True if the expression is satisfiable, False otherwise
        """
        # Verifica se a expressão não é uma tautologia nem uma contradição
        return not (self.is_tautology() or self.is_contradiction())

    def is_contingency(self) -> bool:
        """
        is_contingency is a method that checks if the expression is a contingency.
        Returns:
            bool: True if the expression is a contingency, False otherwise
        """
        # Verifica se a expressão é satisfiável e não é uma tautologia
        return self.is_satisfiable() and not self.is_tautology()

    def get_variables(self) -> list:
        """
        variables is a method that returns the variables of the expression.
        Returns:
            list: The variables of the expression
        """
        return self._vars.copy()
    
    def get_expression(self) -> Expression:
        """
        get_expression is a method that returns the expression.
        Returns:
            Expression: The expression
        """
        return self.__expression
