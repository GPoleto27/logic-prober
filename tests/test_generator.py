from random import choice

operations = ["/\\", "\\/", ">", "="]

def main():
    for n_vars in range(5, 33):
        n = 1
        vars = ["0", "1"]
        # append a to z
        for i in range(ord("a"), ord("a")+n_vars-1):
            vars.append(chr(i))

        while n <= 10000:
            with(open(f"test_{n_vars}_{n}.txt", "w+")) as f:
                # write 5 operations
                lines = []
                for i in range(n):
                    line = ""
                    for i in range(n_vars):
                        # select a random operation a 2 random chars from a to z
                        op = choice(operations)
                        l = choice(vars)
                        is_not = choice([True, False])
                        if i == n_vars-1:
                            r = choice(vars)
                            line += f"{'~' if is_not else ''}{l}{op}{r}\n"
                        else:
                            line += f"{'~' if is_not else ''}{l}{op}"
                    lines.append(line)
                f.writelines(lines)

            n *= 10

if __name__ == "__main__":
    main()