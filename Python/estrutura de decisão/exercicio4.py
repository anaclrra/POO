""" Escreva um programa que sempre escolhe o menor caminho a ser percorrido pelo usuário em
função do local onde se encontra e as opções de caminho a serem seguidas. O usuário sempre
parte do ponto A. O usuário deverá fornecer os valores de distância entre os pontos e o programa
deverá apresentar o caminho a ser percorrido e a distância, conforme o exemplo. Sua solução
deve utilizar apenas estruturas condicionais. """

AB = int(input("digite a distância AB: "))
AC = int(input("digite a distância AC: "))
BD = int(input("digite a distância BD: "))
BE = int(input("digite a distância BE: "))
CF = int(input("digite a distância CF: "))
CG = int(input("digite a distância CG: "))

if(AB < AC):
  if(BD < BE):
    somaDistancia = AB + BD
    print("Caminho pecorrido A -> B -> D \nDistância   pecorrida:{}".format(somaDistancia))
  else:
    somaDistancia = AB + BE
    print("Caminho pecorrido A -> B -> E \nDistância pecorrida{}".format( somaDistancia))
elif(AC < AB):
  if(CF < CG):
    somaDistancia = AC + CF
    print("Caminho pecorrido A -> C -> F \nDistância   pecorrida:{}".format(somaDistancia))
  else:
    somaDistancia = AC + CG
    print("Caminho pecorrido A -> C -> G \nDistância   pecorrida:{}".format(somaDistancia))