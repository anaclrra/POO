numPerguntas = int(input("Quantas pessoas irão responder a sua pesquisa?"))
contador = 1
alegre = 0
triste = 0
naoResponder = 0

while (contador <= numPerguntas):
    respostas = input("Digite sua opnião: ")
    if (respostas == "satisfeito" or respostas == "s"):
        alegre = alegre + 1

    elif (respostas == "insatisfeito" or respostas == "in"):
        triste = triste + 1

    elif (respostas == "não quero responder"  or respostas == "nqr" or respostas == " "):
        naoResponder = naoResponder + 1
    contador = contador + 1

totalRespostas = alegre + triste + naoResponder

totalAlegre = (alegre / totalRespostas) * 100
totalTriste = (triste / totalRespostas) * 100
totalNaoResp = (naoResponder / totalRespostas) * 100

print(f"A porcentagem para SATISFEITO é: {totalAlegre}%")
print(f"A porcentagem para INSATISFEITO é: {totalTriste}%")
print(f"A porcentagem para NÃO QUERO RESPONDER é: {totalNaoResp}%")
