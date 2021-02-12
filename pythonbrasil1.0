#(Python Brasil) Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas 
#existentes na máquina.

saca = 0

# notas de 100, 50, 10, 5 e 1;
# valor entre 10 e 600;

while not(saca >= 10 and saca <= 600):
    saca = int(input("Neste terminal está disponível o valor de 10 a 600 reais. Quanto você deseja sacar? "))

notacem = int((saca / 100))
notacinquenta = int((saca % 100 / 50))
notadez = int((saca % 50 / 10))
notacinco = int((saca % 10 / 5))
notaum = saca % 5

if (saca > 100 and notacem > 0):
    print(f"Recebe {notacem} nota(s) de cem reais.")

if (saca > 50 and notacinquenta > 0):
    print(f"Recebe {notacinquenta} nota(s) de cinquenta reais.")

if (saca > 10 and notadez > 0):
    print(f"Recebe {notadez} nota(s) de dez reais.")

if (saca > 5 and notacinco > 0):
    print(f"Recebe {notacinco} nota(s) de cinco reais.")

if (notaum > 0):
    print(f"Recebe {notaum} nota(s) de um real.")

