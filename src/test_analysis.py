#!/usr/bin/env python3
from lexical_analysis import LexicalAnalysis
from syntactic_analysis import SyntacticAnalysis
from semantic_analysis import SemanticAnalysis

from os import listdir
from time import time

import pandas as pd

def tokenize(line):
    # evaluate the line
    _, accepted_tokens, _ = LexicalAnalysis().evaluate(line)
    _, accepted_tokens, _ = SyntacticAnalysis().evaluate(accepted_tokens)
    return accepted_tokens
    

def main():
    samples = 10
    # for each test file in folder tests
    folder = [f for f in listdir('tests') if f.endswith('.txt')]
    folder.sort()

    # file names are test_{n_vars}_{n_lines}.txt
    # n_vars = number of variables
    # n_lines = number of lines
    
    # create a dataframe to store the results
    df = pd.DataFrame(columns=['n_vars', 'n_lines', 'avg_time'])

    for file in folder:
        with open(f"tests/{file}", "r") as f:
            # read the file
            lines = f.readlines()
            tks=[]
            for line in lines:
                # evaluate the line
                tks.append(tokenize(line))

            total_time = 0
            for i in range(samples):
                start_time = time()
                # evaluate each line
                for tk in tks:
                    SemanticAnalysis(tk.copy()).evaluate()
                total_time += time() - start_time
            
            # get the number of variables and lines
            n_vars, n_lines = file.replace(".txt", "").split("_")[1:]
            # calculate the average time
            avg_time = total_time / samples
            # add the result to the dataframe
            df = pd.concat([df, pd.DataFrame([[n_vars, n_lines, avg_time]], columns=['n_vars', 'n_lines', 'avg_time'])])
            print(f"Mean time for {file}: {total_time/samples}")
    
        # save the dataframe to a csv file
        df.to_csv("avg_runtime_report.csv", index=False)    


if __name__ == "__main__":
    main()
