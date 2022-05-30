# Autor: Micael Muniz de Oliveira Santos
# Componente Curricular: Algoritmos I
# Concluído em: 21/05/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

'''
MAIN:
Principal modulo do projeto, ele é responsável por coletar as informações iniciais, passando-as como parâmetros para o
play_game.py processa-las, ao final ele chama o menu final.
'''


from seven_eleven import *
from play_game import run_game
import menu

# VARIAVÉIS VALIDADORAS DE CICLO
ask_dif = "REPEAT"
ask_board = "REPEAT"
ask_rounds = "REPEAT"
start = "REPEAT"
keep_playing = True

# CICLO VALIDADOR DO MAIN MENU
while keep_playing:
    while start != '1':
        clearConsole()
        print(color('blue'))
        print(line(1),
              f"\n{'MATRIX ADIVINHATION':^49}\n",
              line(2))
        print("(1) Novo Jogo\n"
              "(2) Regras\n"
              "(3) Créditos\n"
              "(4) Sair\n",
              line(1))

        start = input()

        if start == '2':
            menu.game_rules()
        elif start == '3':
            menu.credits()
        elif start == '4':
            keep_playing = False
            exit()


    clearConsole()

    print(color('blue'))
    print(line(1),
          f"\n{'BEM VINDOS':^49}\n",
          line(1))
    # NOME DO PLAYER 1 E PLAYER 2
    player1 = input(f"{color('cyan')}Player 1 Nickname: ").strip().capitalize()
    player2 = input(f"{color('yellow')}Player 2 Nickname: ").strip().capitalize()


    # CICLO VALIDADOR DO MENU DE DIFICULDADE
    '''
    Os menus trabalham com tres tipos variáveis: 
    "variável"          # variável em si, raw, que será passada como parâmetro para funções caso esteja de acordo com o esperado
    "ask_variável"      # valida o ciclo, até que digite o tipo de valor esperado, só então o valor é adicionado a raw variable
    "variável_text"     # a variável que é utilizada como label, possui modificações, cores, é puramente usada para exibição
    '''
    while ask_dif == "REPEAT":
        clearConsole()

        print(color('blue'))
        print(line(1), f"\n{'ESCOLHAM A DIFICULDADE DO JOGO':^49}\n", line(2))
        print(f"{color('green')}Fácil -> Tabuleiro 3x3 (random de 1 a 30)\n"
              f"{color('yellow')}Médio -> Tabuleiro 4x4 (random de 1 a 60)\n"
              f"{color('red')}Difícil -> Tabuleiro 5x5 (random de 1 a 100)\n")

        dif = input(f"{color('')}(F / M / D) ").strip().upper()

        if dif == "F" or dif == "FÁCIL" or dif == "FACIL":
            dif = 'easy'
            ask_dif = 'STOP'
            dif_text = color('green')+'fácil'

        elif dif == "M" or dif == "MÉDIO" or dif == "MEDIO":
            dif = 'medium'
            dif_text = color('yellow')+'médio'
            ask_dif = 'STOP'

        elif dif == "D" or dif == "DIFÍCIL" or dif == "DIFICIL":
            dif = 'hard'
            ask_dif = 'STOP'
            dif_text = color('red')+'difícil'

        else:
            ask_dif = "REPEAT"


    # CICLO VALIDADOR DO MENU DE ESCOLHA DE TABULEIRO (Modo de jogo)
    while ask_board == "REPEAT":
        clearConsole()

        print(color('blue'))
        print(line(1),
              f"\n{'ESCOLHAM COM QUANTOS TABULEIROS VÃO JOGAR':^49}\n",
              line(2))
        print(f"[1] -> Apenas um tabuleiro, dividido para ambos os jogadores\n"
              f"[2] -> Tabuleiros individuais, um para cada jogador\n")

        board = input(f"{color('')}(Um / Dois) ").strip().upper()

        if board == "UM" or board == "1":
            board = 'um'
            ask_board = 'STOP'
            board_text = 'um tabuleiro'

        elif board == "DOIS" or board == "2":
            board = 'dois'
            ask_board = 'STOP'
            board_text = 'dois tabuleiros'

        else:
            ask_board = "REPEAT"


    # CICLO VALIDADOR DO MENU DE QUANTIDADE DE RODADAS
    while ask_rounds == "REPEAT":
        clearConsole()
        print(color('blue'))
        print(line(1), f"\n{'RODADAS PARA FINALIZAR O JOGO':^49}\n", line(2))
        print(f"[  0  ] Sem limite, o jogo finaliza ao completar o tabuleiro\n"
              f"[Impar] Valor limite de rounds para finalizar o jogo\n")

        rounds = input(f"{color('')}Rounds: ").strip().upper()

        try:
            if int(rounds) % 2 != 0 and int(rounds) > 0 or rounds == '0':
                ask_rounds = "STOP"
                if int(rounds) == 0:
                    rounds_text = 'infinitas'
                    rounds = 256    # Valor utilizado para simular rodadas infinitas
                else:
                    rounds_text = rounds
                    rounds = int(rounds)
        except:
            ask_rounds = "REPEAT"

    clearConsole()

    print(color('blue'))
    print(line(1))
    print(f"{f'{player1} vs {player2}':^49}")
    print(f"{f'MODO DE JOGO: {board_text}':^49}")
    print(f"{f'NÚMERO DE RODADAS: {rounds_text}':^49}")
    print(f"{f'DIFICULDADE DE JOGO: {dif_text}':^55}{color('blue')}")
    print(line(2))

    wait()

    '''
    Todas informações sobre a partida foram coletadas, o código chama o modulo que roda o jogo, com base nas regras estipuladas 
    como parâmetro de run_game. Como resultado, ele recebe o resultado do jogo, que é o vencedor do jogo e as rodadas jogadas.
    '''
    # INICIO DO JOGO
    result = run_game(dif, rounds, board, player1, player2)


    '''
    A partida terminou, tudo foi impresso na tela durante a jogatina, além que as regras do jogo já haviam sido pré-definidas
    neste modulo, sendo assim, só é necessário receber como resultado quantas rodadas foram jogadas, e o vencedor do jogo.
    0 = empate
    1 = jogador 1 venceu
    2 = jogador 2 venceu
    Com essas informações, o placar final do jogo é chamado
    '''
    menu.scoreboard(result[0], player1, player2, rounds_text, dif_text, board_text, result[1], result[2], result[3])

    wait()

    start = "REPEAT"