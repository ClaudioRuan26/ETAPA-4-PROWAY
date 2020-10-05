a = 4
sair = 0
addMin = 12
addMax = 24
tabela = 0



jogos = ("|  Jogo  |  Placar   |  Min. Temporada  |  Máx. Temporada  | Quebra Recorde Min.  |  Quebra Recorde Máx.  |"
"\n|    1   |     12    |        12        |         12       |         0            |             0         |"
"\n|    2   |     24    |        12        |         24       |         0            |             1         |"
"\n|    3   |     10    |        10        |         24       |         1            |             1         |"
"\n|    4   |     24    |        10        |         24       |         1            |             1         |")



while (sair != 3):
    add = 0
    escolha = int(input("Digite uma operação: 1 -> Ver a tabela | 2 -> Inserir um jogo | 3 -> Sair : "))
    if (escolha == 1):
        if tabela == 0:
            print(jogos)
        else:
            print(jogos)
    elif (escolha == 2):
        addJ = int(input("Jogo: "))
        addP = int(input("Placar: "))
        if (addP < addMin):
            addMin = addP
            addQRMin = 1
        else:
            addMin = 12
            addQRMin = 0
        if (addP > addMax):
            addMax = addP
            addQRMax = 1
        else:
            addMax = 24
            addQRMax = 0
        tabela = "|    " + str(addJ) + "   |" + "     "+ str(addP) +"    |" + "        " + str(addMin) + "        |" + "         " + str(addMax) + "       |" + "         " + str(addQRMin) + "            |" + "             " + str(addQRMax) + "         |"
        jogos = jogos + "\n" +tabela
        
    elif (escolha == 3):
        sair = escolha
        print("Obrigado e volte sempre.")
