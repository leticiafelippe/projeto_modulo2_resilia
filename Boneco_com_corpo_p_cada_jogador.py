multiplayer = ["jogador1", "jogador2", "jogador3"]  # referente regra 0

# def jogador1():
palavra_secreta = "casado" # regra 1  FELIPE JÁ FEZ A PARTE DA PALAVRA SECRETA

# palavra_secreta = "casado"  # regra 1 FELIPE JÁ FEZ A PARTE DA PALAVRA SECRETA
tentativas = 18
jogador_atual = 0
erros = 0
erros2 = 0
erros3 = 0

def corpo():
    corpo = []
    # corpo.append("+"*7 + "\n|       \n| \n| \n| \n| \n") # sem cabeça
    corpo.append("+" * 7 + "\n|       \n|     👽\n| \n| \n| \n****")  # cabeça
    corpo.append("+" * 7 + "\n|       \n|     👽\n|     TT\n|     ||\n|\n|\n****")  # cabeça, tronco
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT\n|     ||\n|\n|\n****")  # cabeça, tronco, 1 braço,
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|\n|\n****")  # cabeça, tronco, 2 braços
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /\n|\n****")  # cabeça, tronco, 1 perna
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /  \\n|\n****")  # cabeça, tronco, 2 pernas

def corpo2():
    corpo2 = []
    # corpo.append("+"*7 + "\n|       \n| \n| \n| \n| \n") # sem cabeça
    corpo2.append("+" * 7 + "\n|       \n|     👽\n| \n| \n| \n****")  # cabeça
    corpo2.append("+" * 7 + "\n|       \n|     👽\n|     TT\n|     ||\n|\n|\n****")  # cabeça, tronco
    corpo2.append("+" * 7 + "\n|       \n|     👽\n|  o==TT\n|     ||\n|\n|\n****")  # cabeça, tronco, 1 braço,
    corpo2.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|\n|\n****")  # cabeça, tronco, 2 braços
    corpo2.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /\n|\n****")  # cabeça, tronco, 1 perna
    corpo2.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /  \\n|\n****")  # cabeça, tronco, 2 pernas

def corpo3():
    corpo3 = []
    #corpo.append("+"*7 + "\n|       \n| \n| \n| \n| \n****") # sem cabeça
    corpo3.append("+"*7 + "\n|       \n|     👽\n| \n| \n| \n****")  # cabeça
    corpo3.append("+"*7 + "\n|       \n|     👽\n|     TT\n|     ||\n|\n|\n****") # cabeça, tronco
    corpo3.append("+"*7 + "\n|       \n|     👽\n|  o==TT\n|     ||\n|\n|\n****") # cabeça, tronco, 1 braço,
    corpo3.append("+"*7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|\n|\n****") # cabeça, tronco, 2 braços
    corpo3.append("+"*7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /\n|\n****") # cabeça, tronco, 1 perna
    corpo3.append("+"*7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /  \\n|\n****") # cabeça, tronco, 2 pernas

test = [corpo, corpo2, corpo3]

for i in range(0, tentativas):
    print(f"Jogador atual é {multiplayer[jogador_atual]}")
    letra = input("Digite uma letra:  ")
    if letra in palavra_secreta:
        print("Você acertou. ")
        palavra_secreta = palavra_secreta.replace("", letra)  # regra 2.1
        condicao = False
    elif jogador_atual == 0:
        print("ERROU! Errou feio, errou rude!")  # regra 2.2
        print(corpo[erros])
        erros += 1
        if jogador_atual == len(multiplayer) - 1:
            jogador_atual = 0
        else:
            jogador_atual += 1
    elif jogador_atual == 1:
        print("ERROU! Errou feio, errou rude!")  # regra 2.2
        print(corpo2[erros2])
        erros2 += 1
        if jogador_atual == len(multiplayer) - 1:
            jogador_atual = 0
        else:
            jogador_atual += 1
    elif jogador_atual == 2:
        print("ERROU! Errou feio, errou rude!")  # regra 2.2
        print(corpo3[erros3])
        erros3 += 1
        if jogador_atual == len(multiplayer) - 1:
            jogador_atual = 0
        else:
            jogador_atual += 1

corpo()
corpo2()
corpo3()