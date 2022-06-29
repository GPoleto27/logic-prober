import argparse

from console_logging import Console

from lexical_analysis import LexicalAnalysis
from syntactic_analysis import SyntacticAnalysis
from semantic_analysis import SemanticAnalysis


input_file = input("Enter input file\n")

with open(input_file, 'r') as input_data:
    for i, line in enumerate(input_data):
        accepted, accepted_tokens, errors = LexicalAnalysis().evaluate(line)
        print()
        print("Linha", str(i) + ":", line[:-1])
        i += 1

        if not accepted:
            print('[LEX] Recusado.')
            print(*errors)
            continue
        print("[LEX] Aceito.")

        accepted, accepted_tokens, errors = SyntacticAnalysis().evaluate(accepted_tokens)
        if not accepted:
            print('[SYN] Recusado.')
            print(*errors)
            continue
        print("[SYN] Aceito.")

        print("[SEM]", SemanticAnalysis(accepted_tokens).evaluate())
