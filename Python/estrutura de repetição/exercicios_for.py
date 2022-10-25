def exe01():
  print("f1")
  for i in range(2, 14, 2):
    print(i, end = ",")
exe01()

def exe02():
  print("f2")

  num = int(input("Digite um número positivo:"))
  for i in range(1, num):
    print(i, end = ",")
  
exe02()

def exe03():
  print("f3")
  inicio = int(input("Início do intervalo"))
  fim = int(input("Fim do intervalo"))
  for i in range(inicio, fim+1):
    print(i, end = ",")
exe03()

def exe04():
  print("f4")
  inicio = int(input("Início do intervalo"))
  fim = int(input("Fim do intervalo"))
  for i in range(inicio+1, fim):
    print(i, end = ",")
exe04()