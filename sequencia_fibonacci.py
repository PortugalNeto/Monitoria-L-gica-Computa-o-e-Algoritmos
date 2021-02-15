import matplotlib
import matplotlib.pyplot as plt

index = []
first = 0
second = 1
soma_arr = []
termos = int(input("Quantos termos você deseja visualizar na sequência de Fibonacci? (insira um número inteiro) "))
for i in range(0, termos + 1):
    soma = first + second
    print(soma)
    first = second
    second = soma
    index.append(i)
    soma_arr.append(soma)

plt.bar(index, soma_arr, color="blue")
matplotlib.pyplot.show()
