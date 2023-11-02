#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
#Use a função len(string) para saber o tamanho de um texto (número de caracteres)

nome = str (input("Digite um nome: "))
while (len(nome) <=3):
  nome = str (input("É necessário que o nome tenha mais de 3 caracteres. Digite um nome: "))

idade = int (input("Digite a sua idade: "))
while (idade<0) or (idade>150):
  idade = int (input("Idade Inválida. É necessário que esteja entre entre 0 e 150. Digite a sua idade: "))

salario = float (input("Digite o valor do seu salário: "))
while (salario<=0):
  salario = float (input("Salário inválido. É necessário que seja maior que 0. Digite o valor do seu salário: "))

sexo = str (input("Digite o gênero correspondente. Para masculino, digite 'm', e para feminino, digite 'f': "))
while (sexo != "m") and (sexo != "f"):
  sexo = str (input("Gênero não cadastrado. Digite 'm' ou 'f'. Digite o gênero correspondente. Para masculino, digite 'm', e para feminino, digite 'f': "))

estado_civil = str (input("Digite o estado civil correspondente. Para solteiro, digite 's'; para casado, digite 'c'; para viúvo, digite 'v'; e para divorciado, digite 'd': "))
while (estado_civil!="s") and (estado_civil!="c")  and (estado_civil!="v") and (estado_civil!="d"):
  estado_civil = str (input("Estado civil inválido. Digite 's', 'c', 'v' ou 'd'. Digite o estado civil correspondente. Para solteiro, digite 's'; para casado, digite 'c'; para viúvo, digite 'v'; e para divorciado, digite 'd': "))

print("Fim do questionário. Todas as informações foram validadas!")
