from queue import deque

global env
env = {}


class Expression():
    pass

"""# Operands"""

class Operand(Expression):
    def __str__(self):
        return str(self._value)

class Binary(Operand):
    def __init__(self, value: str):
        self._value = value

    def evaluate(self) -> bool:
        return self._value == "1"

class Variable(Operand):
    def __init__(self, value: str):
        global env

        self._value = value
        env[value] = False

    def evaluate(self) -> bool:
        return env.get(self._value)

"""# Operations"""

class Operation(Expression):
    pass

class UnaryOperation(Operation):
    def __init__(self, l_value: Expression):
        self._l_value = l_value

class BinaryOperation(Operation):
    def __init__(self, l_value: Expression, r_value: Expression):
        self._l_value = l_value
        self._r_value = r_value

"""### Unary Operations"""

class Not(UnaryOperation):
    def evaluate(self) -> bool:
        return not self._l_value.evaluate()

    def __str__(self):
        return f"~({str(self._l_value)})"

"""### Binary Operations"""

class And(BinaryOperation):
    def evaluate(self) -> bool:
        return self._l_value.evaluate() and self._r_value.evaluate()

    def __str__(self):
        return f"({str(self._l_value)})/\\({str(self._r_value)})"

class Or(BinaryOperation):
    def evaluate(self) -> bool:
        return self._l_value.evaluate() or self._r_value.evaluate()

    def __str__(self):
        return f"({str(self._l_value)})\\/({str(self._r_value)})"

class Conditional(BinaryOperation):
    def evaluate(self) -> bool:
        return not self._l_value.evaluate() or self._r_value.evaluate()

    def __str__(self):
        return f"({str(self._l_value)})>({str(self._r_value)})"

class Biconditional(BinaryOperation):
    def evaluate(self) -> bool:
        return not (self._l_value.evaluate() ^ self._r_value.evaluate())

    def __str__(self):
        return f"({str(self._l_value)})=({str(self._r_value)})"

"""## Evaluate expression"""
class SemanticAnalysis(Expression):
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
            "BICON": Biconditional
        }

        while len(expression) != 0:
            token, value = expression.popleft()

            if issubclass(classes[token], Operand):
                stack.appendleft(classes[token](value))

            elif issubclass(classes[token], UnaryOperation):
                l_value = stack.popleft()
                stack.appendleft(classes[token](l_value))

            elif issubclass(classes[token], BinaryOperation):
                r_value = stack.popleft()
                l_value = stack.popleft()
                stack.appendleft(classes[token](l_value, r_value))
            
            #print("Stack:", list(stack))
            
        self.__expression = stack.popleft()
        print(str(self.__expression))

    def evaluate(self) -> list:
        global env
        n: int = len(env)
        combinations = [num for num in ('{0:b}'.format(p).zfill(n) for p in range(2**n))]

        for combination in combinations:
            for i, var in enumerate(env): env[var] = combination[i] == "1"

            self.__results.append(self.__expression.evaluate())

        return self.__results.copy()

    def is_tautology(self) -> bool:
        return not (False in self.__results)

    def is_contradiction(self) -> bool:
        return not (True in self.__results)
