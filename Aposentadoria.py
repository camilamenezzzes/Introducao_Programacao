#Faça um programa que receba a idade e o tempo de serviço de uma
#pessoa, calcule e mostre se ela pode ou nao se aposentar. Para se aposentar,
#deve ter idade igual ou superior a 65 anos ou 25 anos de tempo de serviço

idade = int (input("Digite a idade:"))
tempo_servico = (input("Digite o tempo de serviço:"))

if (idade >= 65):
  print("Pode aposentar")
elif (tempo_servico==30):
  print("Pode aposentar")
elif (idade==60 and tempo_servico==25):
  print("Pode aposentar")
else:
 print("Não pode aposentar")