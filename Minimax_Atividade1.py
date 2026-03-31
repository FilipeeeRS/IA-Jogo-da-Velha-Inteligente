# PUC-Campinas Engenharia de Software
# Inteligencia Artificial e Aprendizado de Maquina

# mostra o tabuleiro do jogo
def mostra_tabuleiro(tabuleiro):
    print("-------------")
    for linha in tabuleiro:
        print("|", linha[0], "|", linha[1], "|", linha[2], "|")
        print("-------------")


# checa se algum jogador ganhou (linha, coluna ou diagonal)
def verifica_vitoria(tabuleiro, jogador):

    # linhas
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True

    # colunas
    for i in range(3):
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True

    # diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False


# verifica se nao tem mais espaco no tabuleiro
def verifica_empate(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula == " ":
                return False
    return True


# retorna as posicoes que ainda estao vazias
def posicoes_vazias(tabuleiro):
    vazias = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                vazias.append((i, j))
    return vazias


# algoritmo minimax - vai testar todas as jogadas possiveis e retornar o valor do melhor caminho
# maximizador = agente (O), minimizador = usuario (X)
def minimax(tabuleiro, profundidade, maximizando):

    # casos de parada
    if verifica_vitoria(tabuleiro, "O"):
        return 10 - profundidade  # ganhamos, buscar ganhar rapido

    if verifica_vitoria(tabuleiro, "X"):
        return -10 + profundidade  # perdemos, buscar demorar mais pra perder

    if verifica_empate(tabuleiro):
        return 0

    if maximizando:
        # vez do agente - quer o maior valor possivel
        melhor = float('-inf')
        for (l, c) in posicoes_vazias(tabuleiro):
            tabuleiro[l][c] = "O"
            resultado = minimax(tabuleiro, profundidade + 1, False)
            tabuleiro[l][c] = " "  # desfaz pra testar a proxima opcao
            if resultado > melhor:
                melhor = resultado
        return melhor

    else:
        # vez do usuario - assume que ele vai jogar o melhor possivel 
        melhor = float('inf')
        for (l, c) in posicoes_vazias(tabuleiro):
            tabuleiro[l][c] = "X"
            resultado = minimax(tabuleiro, profundidade + 1, True)
            tabuleiro[l][c] = " "
            if resultado < melhor:
                melhor = resultado
        return melhor


# percorre as jogadas possiveis e escolhe a de maior valor minimax
def jogada_agente(tabuleiro):
    melhor_val = float('-inf')
    jogada = None

    for (l, c) in posicoes_vazias(tabuleiro):
        tabuleiro[l][c] = "O"
        val = minimax(tabuleiro, 0, False)
        tabuleiro[l][c] = " "

        if val > melhor_val:
            melhor_val = val
            jogada = (l, c)

    return jogada


def start_jogo():

    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    print("\nJogo da Velha - Voce (X) vs Agente (O)")
    print("Linhas e colunas de 1 a 3\n")
    mostra_tabuleiro(tabuleiro)

    turno = "X"

    while True:

        if turno == "X":
            print("\nSua vez:")

            # fica pedindo ate o usuario digitar algo valido
            while True:
                try:
                    linha = int(input("Linha (1-3): ")) - 1
                    coluna = int(input("Coluna (1-3): ")) - 1

                    if linha not in range(3) or coluna not in range(3):
                        print("Fora do tabuleiro, tenta de novo.")
                        continue

                    if tabuleiro[linha][coluna] != " ":
                        print("Ja tem alguem ai, escolhe outra.")
                        continue

                    break

                except ValueError:
                    print("Digita um numero.")

            tabuleiro[linha][coluna] = "X"

        else:
            print("\nAgente pensando...")
            linha, coluna = jogada_agente(tabuleiro)
            tabuleiro[linha][coluna] = "O"
            print(f"Agente jogou em ({linha + 1}, {coluna + 1})")

        mostra_tabuleiro(tabuleiro)

        if verifica_vitoria(tabuleiro, turno):
            if turno == "X":
                print("Voce ganhou!")
            else:
                print("O agente ganhou!")
            return

        if verifica_empate(tabuleiro):
            print("Empatou!")
            return

        # troca o turno
        turno = "O" if turno == "X" else "X"


if __name__ == "__main__":
    start_jogo()
