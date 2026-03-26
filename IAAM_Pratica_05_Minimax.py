# PUC-Campinas - Engenharia de Software
# Disciplina: 

def mostra_tabuleiro(tabuleiro):

    print("-------------")
    for linha in tabuleiro:
        print("|", linha[0], "|", linha[1], "|", linha[2], "|")
        print("-------------")


def verifica_vitoria(tabuleiro, jogador):

    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True

    for i in range(3):
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True

    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False


def verifica_empate(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula == " ":
                return False
    return True


def obter_movimentos_possiveis(tabuleiro):
    movimentos = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                movimentos.append((i, j))
    return movimentos

def minimax(tabuleiro, profundidade, eh_maximizador):
    
    if verifica_vitoria(tabuleiro, "O"):
        return 10 - profundidade

    if verifica_vitoria(tabuleiro, "X"):
        return -10 + profundidade

    if verifica_empate(tabuleiro):
        return 0

    movimentos = obter_movimentos_possiveis(tabuleiro)

    if eh_maximizador:
        melhor_valor = float('-inf')
        for (linha, coluna) in movimentos:
            tabuleiro[linha][coluna] = "O"
            valor = minimax(tabuleiro, profundidade + 1, False)
            tabuleiro[linha][coluna] = " "
            melhor_valor = max(melhor_valor, valor)
        return melhor_valor

    else:
        melhor_valor = float('inf')
        for (linha, coluna) in movimentos:
            tabuleiro[linha][coluna] = "X"
            valor = minimax(tabuleiro, profundidade + 1, True)
            tabuleiro[linha][coluna] = " "
            melhor_valor = min(melhor_valor, valor)
        return melhor_valor


def melhor_jogada_agente(tabuleiro):
    melhor_valor = float('-inf')
    melhor_movimento = None

    for (linha, coluna) in obter_movimentos_possiveis(tabuleiro):
        tabuleiro[linha][coluna] = "O"
        valor = minimax(tabuleiro, 0, False)
        tabuleiro[linha][coluna] = " "

        if valor > melhor_valor:
            melhor_valor = valor
            melhor_movimento = (linha, coluna)

    return melhor_movimento

def start_jogo():

    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    print("\n  JOGO DA VELHA - MINIMAX  ")
    print("\nVocê joga com X | Agente joga com O")
    print("Linhas e colunas são numeradas de 1 a 3\n")

    mostra_tabuleiro(tabuleiro)

    jogador_atual = "X"

    while True:

        if jogador_atual == "X":
            print(f"\nSua vez (X):")

            while True:
                try:
                    linha  = int(input("Escolha uma linha  (1-3): ")) - 1
                    coluna = int(input("Escolha uma coluna (1-3): ")) - 1

                    if linha not in range(3) or coluna not in range(3):
                        print("Posição fora do tabuleiro. Tente novamente.")
                        continue

                    if tabuleiro[linha][coluna] != " ":
                        print("Posição já ocupada. Escolha outra.")
                        continue

                    break

                except ValueError:
                    print("Entrada inválida. Digite um número inteiro.")

            tabuleiro[linha][coluna] = "X"

        else:
            print("\nVez do Agente (O) — calculando melhor jogada...")
            linha, coluna = melhor_jogada_agente(tabuleiro)
            tabuleiro[linha][coluna] = "O"
            print(f"Agente jogou na linha {linha + 1}, coluna {coluna + 1}")

        mostra_tabuleiro(tabuleiro)

        if verifica_vitoria(tabuleiro, jogador_atual):
            if jogador_atual == "X":
                print("Parabéns! Você venceu!")
            else:
                print("O Agente venceu! Melhor sorte na próxima. 🤖")
            return

        if verifica_empate(tabuleiro):
            print("O jogo terminou em empate!")
            return

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    start_jogo()
