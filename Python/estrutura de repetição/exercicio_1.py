num = int(input("Digite um número: "))
fator = num
 
fat = 1
while(num > 1): 
    fat *= num # fat = fat * num 
    num -= 1 

print(f"O fatorial de {fator} é {fat}")