from lexical_analysis import LexicalAnalysis

operations = ["/\\", "\\/", ">", "="]

def main():
    n = 1
    while n <= 1000000:
        import random
        with(open(f"../tests/test_{n}.txt", "a")) as f:
            #write 10 operations
            lines = []
            for i in range(n):
                line = ""
                for i in range(10):
                    # select a random operation a 2 random chars from a to z
                    op = random.choice(operations)
                    l = random.choice([chr(i) for i in range(ord("a"), ord("z"))])
                    is_not = random.choice([True, False])
                    if i == 9:
                        r = random.choice([chr(i) for i in range(ord("a"), ord("z"))])
                        line += f"{'~' if is_not else ''}{l}{op}{r}\n"
                    else:
                        line += f"{'~' if is_not else ''}{l}{op}"
                lines.append(line)
            f.writelines(lines)

        n *= 10

if __name__ == "__main__":
    main()