from random import choice

operations = ["/\\", "\\/", ">", "="]

def main():
    for n_vars in range(5, 17):
        n = 1
        vars = [chr(i) for i in range(ord("a"), ord("a")+n_vars)]

        while n <= 1000:
            with(open(f"test_{n_vars}_{n}.txt", "w+")) as f:
                # write 5 operations
                lines = []
                for i in range(n):
                    line = ""
                    for i in range(n_vars-1):
                        # select a random operation a 2 random chars from a to z
                        op = choice(operations)
                        is_not = choice([True, False])
                        if i == n_vars-2:
                            line += f"{'~' if is_not else ''}{vars[i]}{op}{vars[i+1]}\n"
                        else:
                            line += f"{'~' if is_not else ''}{vars[i]}{op}"
                    lines.append(line)
                f.writelines(lines)

            n *= 10

if __name__ == "__main__":
    main()