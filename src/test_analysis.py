from lexical_analysis import LexicalAnalysis
from syntactic_analysis import SyntacticAnalysis
from semantic_analysis import SemanticAnalysis

from os import listdir, cpu_count
from time import time
from concurrent.futures import ProcessPoolExecutor


def worker(la, line):
    # evaluate the line
    _, accepted_tokens, _ = la.evaluate(line)
    _, accepted_tokens, _ = SyntacticAnalysis().evaluate(accepted_tokens)
    SemanticAnalysis(accepted_tokens).evaluate()


def main():
    la = LexicalAnalysis()

    # for each test file in folder tests
    for file in listdir("./tests"):
        with open(f"./tests/{file}", "r") as f:
            # read the file
            lines = f.readlines()
            start_time = time()
            ProcessPoolExecutor(max_workers=cpu_count()).map(worker, [la]*len(lines), lines)
            # wait for all threads to finish
            print(f"Time for file {file}: {time() - start_time}")

if __name__ == "__main__":
    main()