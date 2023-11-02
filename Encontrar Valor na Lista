#Faça um programa que receba uma quantidade de valores e pergunte ao usuário se quer continuar
#informando valores. Após isso, mostre os números listados, a quantidade e se o valor 5 está entre eles.

valores = []

while True:
 valores.append(int(input("Digite um valor:")))
 pergunta = str (input("Quer continuar? [S/N]"))
 if pergunta in 'Nn':
  break
print ("A quantidade de números inserida foi: ", len(valores))
valores.sort(reverse = True)
print ("Os números inseridos foram: ", valores)
if 5 in valores:
  print ("O número 5 foi inserido na lista.")
else:
  print ("O número 5 não foi inserido na lista.")
