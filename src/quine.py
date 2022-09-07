# Retirado de https://github.com/luanaccampos/kuine sob licença GPLv3

from setCoverGreedy import setCoverGreedy
from setCoverPD import setCoverPd


class Quine:
    def __init__(self, termos, N, minimal=True):
        self.quadros = []
        self.implicantes = []
        self.quadro = {}
        self.n = N
        self.var = []
        self.grafo = {}
        self.termos = set(termos)

        if N >= 6:
            minimal = False

        for i in range(0, N + 1):
            self.quadro[i] = []

        for i in range(0, N):
            self.var.append("{:c}".format(i + 65))

        for i in termos:
            aux = "{:010b}".format(i)
            aux = aux[10 - N :]
            self.quadro[self.bitsLigados(aux)].append((aux, frozenset([i])))

        self.quadros.append(self.quadro)

        n = N + 1

        while n > 1:
            novo = {}
            J = 0

            marked = {}

            for i in range(0, n):
                for j in self.quadro[i]:
                    marked[j] = False

            for i in range(0, n - 1):
                aux = set()
                for t in self.quadro[i]:
                    for t2 in self.quadro[i + 1]:
                        k = self.match(t[0], t2[0])
                        if k:
                            aux.add((k[1], t[1].union(t2[1])))
                            marked[t] = marked[t2] = True
                            self.grafo[k[1]] = (t[0], t2[0])

                if len(aux) != 0:
                    novo[J] = aux
                    J += 1

            for i in marked:
                if not marked[i]:
                    self.implicantes.append(i)

            self.quadro = novo
            n = len(novo)
            self.quadros.append(novo)

        if len(self.quadro) > 0:
            for i in self.quadro[0]:
                self.implicantes.append(i)

        S = []

        for i in self.implicantes:
            S.append(set(i[1]))

        if minimal:
            self.ans = setCoverPd(termos, S).getResposta()
        else:
            self.ans = setCoverGreedy(termos, S).getResposta()

        resposta = []

        for imp in self.ans:
            for i in self.implicantes:
                if i[1] == imp:
                    resposta.append((i[0], i[1]))
                    break

        if len(self.termos) == 0:
            resposta.append(("", {}))

        self.ans = resposta

    def bitsLigados(self, s):
        k = 0
        for i in s:
            if i == "1":
                k += 1
        return k

    def match(self, s1, s2):
        k = 0
        s = ""

        for i in range(0, self.n):
            if s1[i] != s2[i]:
                s += "X"
                k += 1
            else:
                s += s1[i]

        if k == 1:
            return True, s
        else:
            return False

    def toLiteral(self, s1):
        s = ""

        if s1 == "":
            return "Contradição"

        if len(self.termos) == 2**self.n:
            return "Tautologia"

        for i in range(0, len(s1)):
            if s1[i] != "X":
                if s1[i] == "0":
                    s += self.var[i] + "\u0305"
                else:
                    s += self.var[i]

        return s

    def getResposta(self):
        return self.ans

    def getQuadros(self):
        return self.quadros

    def getImplicantes(self):
        return self.implicantes

    def getTermos(self):
        return self.termos

    def getGrafo(self):
        return self.grafo
