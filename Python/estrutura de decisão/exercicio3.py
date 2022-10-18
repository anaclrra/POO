""" Escreva um programa que leia dois valores que representem o início
e o fim de um intervalo. O programa deverá ler um terceiro valor
digitado e verificar se este terceiro valor está dentro do intervalo ou
fora. Caso esteja fora do intervalo, deverá informar se está na parte
inferior ou superior do intervalo. """

inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
meio = int(input("Digite um número: "))

if (meio >= inicio and meio <= fim):
  print(f"O número {meio}, pertence ao intervalo entre {inicio} e {fim}")
elif(meio < inicio):
  print(f"O número {meio} é inferior ao intervalo entre {inicio} e {fim}")
else:
  print(f"O número {meio}, é superior ao intervalo entre {inicio} e {fim}")