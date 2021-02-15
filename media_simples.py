#Calculando a média entre três avaliações**
notas = []

for i in range(1, 4):
    i = float(input(f"Insira a nota da {i}° avaliação: "))
    notas.append(i)

media = round((notas[0] + notas[1] + notas[2])/3, 2)
print(f"A média do aluno é {media}")
