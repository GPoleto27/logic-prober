import lexf

lex = lexf.Lexf()

input_file = input("Enter input file\n")
input_data = open(input_file, 'r')

i = 1

for line in input_data:
    accepted, accepted_tokens, errors = lex.corretude(line)

    print("Linha " + str(i) + ":")
    i += 1

    if accepted:
        print("Aceito.")
        for tokens in accepted_tokens:
            print(tokens)
    else:
        for error in errors:
            print(error)
