from lexical_analysis import LexicalAnalysis
from syntactic_analysis import SyntacticAnalysis
from semantic_analysis import SemanticAnalysis

from os import listdir, cpu_count
from time import time
from concurrent.futures import ProcessPoolExecutor

def tokenize(la, line):
    # evaluate the line
    _, accepted_tokens, _ = la.evaluate(line)
    _, accepted_tokens, _ = SyntacticAnalysis().evaluate(accepted_tokens)
    return accepted_tokens

def worker(accepted_tokens):
    SemanticAnalysis(accepted_tokens).evaluate()
    

def main():
    la = LexicalAnalysis()

    # for each test file in folder tests
    #folder = reversed([file for file in listdir('tests') if file.endswith('.txt')])
    #for file in folder:
    file = "test_10000.txt"
    with open(f"/home/gpoleto/logic-prober/tests/{file}", "r") as f:
        # read the file
        lines = f.readlines()
        tks=[]
        for line in lines:
            # evaluate the line
            tks.append(tokenize(la, line))

        start_time = time()
        # evaluate each line
        pool = ProcessPoolExecutor(max_workers=cpu_count())
        pool.map(worker, tks)
        # wait for all threads to finish
        pool.shutdown(wait=True)
        print(f"Parallel time for file {file}: {time() - start_time}")

        start_time = time()
        # evaluate each line
        for t in tks:
            worker(t)
        # wait for all threads to finish
        print(f"Sequential time for file {file}: {time() - start_time}")


if __name__ == "__main__":
    main()
