# Autor: Micael Muniz de Oliveira Santos
# Componente Curricular: Algoritmos I
# Concluído em: 21/05/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

'''
MENU:
Responsável por imprimir diversos menus, a intenção inicialmente era de imprimir todos os menus do projeto, porém
ficou muito complexo, e desnecessário, já que precisava ficar enviando e recebendo diversas informações para imprimir
um simples menu, então muitos menus que tinha aqui, foram movidos para dentro dos codigos.
'''


from seven_eleven import *

def new_game():
    pass

def game_rules():
    clearConsole()
    print(line(1), color('cyan'), f"\n{'REGRAS DO JOGO':^49}\n", color('blue'), line(2))
    print("# Matrix adivinhation é um jogo de tabuleiro, jogado\n"
            "por DOIS jogadores.\n"
            "# É possível escolher um ou dois tabuleiros para jogar\n"
            "# É possível escolher entre 3 dificuldades para jogar:\n"
            "fácil, medio ou difícil.\n"
            "# Deve ser definido o número IMPAR máximo de rodadas, ou\n"
            "0 para rodadas ilimitadas, nesse caso o jogo só finaliza\n"
            "ao tabuleiro ser completo\n"
            "# A cada rodada, cada jogador precisa escolher uma linha\n"
            "ou coluna do tabuleiro único, ou de seu tabuleiro, então\n"
            "tentar adivinhar o valor da soma do eixo escolhido.\n"
            "# Caso o jogador tente jogar em uma soma já adivinhada, \n"
            "o mesmo não ganhará pontos e perderá a rodada.\n"
            "[ PARTE 1 DE 2 ]\n", line(1))
    wait()
    clearConsole()
    print(color('blue'), line(1), color('cyan'), f"\n{'REGRAS DO JOGO':^49}\n", color('blue'), line(2))
    print("# O jogo termina ao tabuleiro ser completo, ou ao atingir\n"
            "o numero de rodadas definidas como maxima.\n"
            "# A cada casa revelada, o jogador que a revelou ganha um\n"
            "ponto, caso ambos revelem ambos ganham os pontos.\n"
            "# Ao final do jogo, o jogador que tiver mais pontos vence.\n\n"
            f"{color('bold')} {color('yellow')}* Como consultar o histórico de um determinado eixo *{color('blue')}\n"
            "1. Digite a linha ou coluna que deseja jogar ou consultar.\n"
            "2. No lugar do valor do seu chute, digite \"historico\".\n"
            "3. Pressione enter. Após visualizar o histórico, sua rodada\n"
            "NÃO SERÁ PERDIDA e você poderá jogar em seguida.\n\n"
            f"{color('bold')} {color('yellow')}* Como cancelar sua jogada, por erro ou arrependimento *{color('blue')}\n"
            "1. Caso tenha digitado um eixo inexistente, basta prosseguir\n"
            "com a jogada que o jogo irá pedir uma nova tentativa, nenhuma \n"
            "penalidade será aplicada.\n"
            "2. Caso tenha acertado o eixo, porém não foi o eixo que queria,\n"
            "basta digitar qualquer simbolo, ou deixar o campo de valor vazio.\n"
            "[ PARTE 2 DE 2 ]\n", line(1))
    wait()


def credits():
    clearConsole()
    print(line(1), color('cyan'), f"\n{'CRÉDITOS':^49}\n", color('blue'), line(2))
    print(f"Matrix adivinhation é um jogo produzido por {color('purple')}Micael Muniz{color('blue')}\n"
          "Todavia, foi idealizado no componente MI - Algoritmos do\n"
          "curso de Engenharia de Computação da UEFS.  Abril de 2022\n",
          line(1))
    wait()


def scoreboard(result, player1, player2, rounds_text, dif_text, board_text, rounds_played, player1_points, player2_points):
    if result == 0:
        winner_message = "UM EMPATE"
    elif result == 1:
        winner_message = f"UMA VITÓRIA PARA {player1}"
    elif result == 2:
        winner_message = f"UMA VITÓRIA PARA {player2}"

    clearConsole()
    print(color('blue'))
    print(line(2))
    print(f"{f'{player1} [{player1_points} pts]  vs  {player2} [{player2_points} pts]':^49}")
    print(line(1))
    print(f"{f'RESULTADO: {winner_message}':^49}")
    print(line(1))
    print(f"{f'MODO DE JOGO: {board_text}':^49}")
    print(f"{f'NÚMERO DE RODADAS: {rounds_played-1}/{rounds_text}':^49}")
    print(f"{f'DIFICULDADE DE JOGO: {dif_text}':^55}{color('blue')}")
    print(line(2))