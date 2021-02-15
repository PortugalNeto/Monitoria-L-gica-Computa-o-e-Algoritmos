term = input("Qual o termo ou exoressão deseja verificar se é um palíndromo? ")
inverted_term = term[::-1]

if term == inverted_term:
    print("yes")
else:
    print("no")
