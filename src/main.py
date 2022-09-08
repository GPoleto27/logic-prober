from argparse import ArgumentParser
from time import time

from console_logging.console import Console

from lexical_analysis import LexicalAnalysis
from syntactic_analysis import SyntacticAnalysis
from semantic_analysis import SemanticAnalysis
from semantic_analysis_DP import SemanticAnalysis as SemanticAnalysisDP

# Retirado de https://github.com/luanaccampos/kuine sob licença GPLv3
from quine import Quine


def main():
    parser = ArgumentParser(description="Logic expression evaluator")
    parser.add_argument(
        "-e", "--expression", help="Logic expression to evaluate", type=str, default=""
    )
    parser.add_argument(
        "-i",
        "--input",
        help="Input file (if set will override 'expression')",
        type=str,
        default="",
    )
    parser.add_argument(
        "-v",
        "--verbosity",
        help="Verbosity level: [0] No logging [1] Errors [2] Successes [3] Log [4] Info [5] Secure (Default=3)",
        type=int,
        default=3,
    )
    args = parser.parse_args()

    console = Console()
    console.setVerbosity(args.verbosity)

    pd = False

    if args.input != "":
        console.info("Input file given, reading expressions from file")
        with open(args.input, "r") as input_data:
            start_time = time()
            for i, line in enumerate(input_data):
                line = line.replace("\n", "")
                accepted, accepted_tokens, errors = LexicalAnalysis().evaluate(line)

                i += 1
                print("-" * 100)
                print(f"Linha {str(i)}: {line}")
                if not accepted:
                    console.error("[LEX] Recusado.")
                    console.log([error for error in errors])
                    continue
                console.success("[LEX] Aceito.")

                accepted, accepted_tokens, errors = SyntacticAnalysis().evaluate(
                    accepted_tokens
                )
                if not accepted:
                    console.error("[SYN] Recusado.")
                    console.log([error for error in errors])
                    continue
                console.success("[SYN] Aceito.")

                if pd:
                    semantic = SemanticAnalysisDP(accepted_tokens.copy())
                else:
                    semantic = SemanticAnalysis(accepted_tokens.copy())
                
                semantic_results = semantic.evaluate()
                
                vars = semantic.get_variables()
                console.success(f"[SEM] {semantic_results}")

                termos = []
                for i in range(len(semantic_results)):
                    if semantic_results[i] == True:
                        termos.append(i)

                #quine_results = Quine(termos, len(vars)).getResposta()
                #prod_sum = []
                #for r in quine_results:
                #    prod = r[0]
                #    exp = []
                #    for val in prod:
                #        if val == '0':
                #            exp.append(f"~{vars[prod.index(val)]}")
                #        elif val == '1':
                #            exp.append(vars[prod.index(val)])
                #    # insert "/\" between each expression
                #    exp = " /\\ ".join(exp)
                #    prod_sum.append(f"({exp})")
                ## insert "\/" between each expression
                #prod_sum = " \\/ ".join(prod_sum)
                #console.success(f"[OPT] {prod_sum}")
            
            end_time = time()
            console.log(f"Tempo de execução: {end_time - start_time}s")

    else:
        console.info("Expression given, reading expression from arguments")
        accepted, accepted_tokens, errors = LexicalAnalysis().evaluate(args.expression)
        if not accepted:
            console.error("[LEX] Recusado.")
            console.log([error for error in errors])
            return
        console.success("[LEX] Aceito.")

        accepted, accepted_tokens, errors = SyntacticAnalysis().evaluate(
            accepted_tokens
        )
        if not accepted:
            console.error("[SYN] Recusado.")
            console.log([error for error in errors])
            return
        console.success("[SYN] Aceito.")

        semantic = SemanticAnalysis(accepted_tokens)
        semantic_results = semantic.evaluate()
        vars = semantic.get_variables()

        console.success(f"[SEM] {semantic_results}")

        termos = []
        for i in range(len(semantic_results)):
            if semantic_results[i] == True:
                termos.append(i)

        quine_results = Quine(termos, len(vars)).getResposta()
        prod_sum = []
        for r in quine_results:
            prod = r[0]
            exp = []
            for val in prod:
                if val == '0':
                    exp.append(f"~{vars[prod.index(val)]}")
                elif val == '1':
                    exp.append(vars[prod.index(val)])
            # insert "/\" between each expression
            exp = " /\\ ".join(exp)
            prod_sum.append(exp)
        # insert "\/" between each expression
        prod_sum = " \\/ ".join(prod_sum)
        console.success(f"[OPT] {prod_sum}")


if __name__ == "__main__":
    main()
