from argparse import ArgumentParser

from console_logging.console import Console

from lexical_analysis import LexicalAnalysis
from syntactic_analysis import SyntacticAnalysis
from semantic_analysis import SemanticAnalysis


def main():
    parser = ArgumentParser(description="Logic expression evaluator")
    parser.add_argument(
        "-e", "--expression", help="Logic expression to evaluate", type=str, default=""
    )
    parser.add_argument(
        "-i", "--input",
        help="Input file (if set will override 'expression')",
        type=str,
        default="",
    )
    parser.add_argument(
        "-v", "--verbosity",
        help="""Verbosity level:
        [0] No logging
        [1] Errors
        [2] Successes
        [3] Logs
        [4] Info
        [5] Secure (Default=3)""",
        type=int,
        default=3,
    )
    args = parser.parse_args()

    console = Console()
    console.setVerbosity(args.verbosity)

    if args.input != "":
        console.info("Input file given, reading expressions from file")
        with open(args.input, "r") as input_data:
            for i, line in enumerate(input_data):
                accepted, accepted_tokens, errors = LexicalAnalysis().evaluate(line)

                i += 1

                if not accepted:
                    console.error(
                        f"Linha {str(i)}: {line[:-1]} - [LEX] Recusado."
                    )
                    console.logs(*errors)
                    continue
                console.success(f"Linha {str(i)}: {line[:-1]} - [LEX] Aceito.")

                accepted, accepted_tokens, errors = SyntacticAnalysis().evaluate(
                    accepted_tokens
                )
                if not accepted:
                    console.error(
                        "[SYN] Recusado."
                    )
                    console.logs(*errors)
                    continue
                console.success("[SYN] Aceito.")

                console.success(f"[SEM] {SemanticAnalysis(accepted_tokens).evaluate()}")
    else:
        accepted, accepted_tokens, errors = LexicalAnalysis().evaluate(args.expression)
        if not accepted:
            console.error("[LEX] Recusado.")
            console.logs(*errors)
            return
        console.success("[LEX] Aceito.")

        accepted, accepted_tokens, errors = SyntacticAnalysis().evaluate(
            accepted_tokens
        )
        if not accepted:
            console.error("[SYN] Recusado.")
            console.logs(*errors)
            return
        console.success("[SYN] Aceito.")

        console.success(f"[SEM] {SemanticAnalysis(accepted_tokens).evaluate()}")


if __name__ == "__main__":
    main()
