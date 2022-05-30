# Autor: Micael Muniz de Oliveira Santos
# Componente Curricular: Algoritmos I
# Concluído em: 21/05/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

'''
PLAY GAME:
Onde o jogo é processado, recebe como parâmetro as regras estipulada pelos players, e quem sào os players, retorna o resultado.
'''

import difficulty_select
from math import sqrt
import menu
from seven_eleven import *


def run_game(difficulty, rounds, gamemode, player1, player2):
    # VARIAVEIS GLOBAIS:
    xy = eval(f"difficulty_select.{difficulty}('xy')")  # Dimensões do tabuleiro, se é 3x3, 4x4 ou 5x5
    player1_points = 0  # Pontuação do jogador 1, é lido pelo tabuleiro, é escrito por diversas funções que calculam
    player2_points = 0  # Pontuação do jogador 2, é lido pelo tabuleiro, é escrito por diversas funções que calculam
    current_round = 1   # Rodada atual, é lida pelo tabuleiro, é escrita com +1 ao final do código
    who_call = {'winner': 0, 'loser': 0} # Usado na função historico, porém só pode atribuir valores 0 uma unica vez
    history_xy = {'x1': '', 'x2': '', 'x3': '', 'x4': '', 'x5': '', 'y1': '', 'y2': '', 'y3': '', 'y4': '', 'y5': ''}
    # O Histórico de rodadas é escrito durante o processamento do chute do jogador, por uma função recursiva.
    # Existem dois tipos de histórico, o que essa variável representa é o que pode ser chamado a qualquer momento (global), o outro é local.

    # Principais variáveis globais, representam o tabuleiro que é visto, e o oculto (o oculto pode ser ativado no código)
    back_board = eval(f"difficulty_select.{difficulty}('back_board')")  # O tabuleiro oculto, assume a forma conforme a dificuldade
    front_board = eval(f"difficulty_select.{difficulty}('front_board')")  # O tabuleiro visível, assume a forma conforme a dificuldade

    '''
    O Python, nativamente, não suporta copia de matrizes com .copy ou [:], portanto esse bloco faz uma cópia do back_board
    O current_back_board, diferente do back_board, vai tendo seus elementos substituídos por 0, conforme são revelados,
    possibilitando que posteriormente seja desconsiderado este valor, porém mantendo a forma original da matriz.
    '''
    current_back_board = []
    for array in back_board:
        support_array = []
        for item in array:
            support_array.append(item)
        current_back_board.append(support_array.copy())
        support_array.clear()


    # Processa o chute feito pelo jogador (value_p1, value_p2), descobre qual acertou e como acertou, retorna o vencedor
    def move(pos_p1, value_p1, pos_p2, value_p2):
        # Valor da soma das linhas e colunas, o valor que o player tem que adivinhar.
        x1 = sum(back_board[0])
        x2 = sum(back_board[1])
        x3 = sum(back_board[2])
        try:
            x4 = sum(back_board[3])
        except:
            x4 = 0
        try:
            x5 = sum(back_board[4])
        except:
            x5 = 0
        y1 = sum([i[0] for i in back_board])
        y2 = sum([i[1] for i in back_board])
        y3 = sum([i[2] for i in back_board])
        try:
            y4 = sum([i[3] for i in back_board])
        except:
            y4 = 0
        try:
            y5 = sum([i[4] for i in back_board])
        except:
            y5 = 0

        # Calcula o quão perto o player chegou, com base no eixo que ele jogou, e valor chutado.
        how_close_p1 = eval(f"{pos_p1} - value_p1")     # Função generalizada, que calcula a aproximação do valor chutado com o eixo chutado
        if how_close_p1 < 0:
            reveal_p1 = 'max'                           # Se o número for negativo, ele passou do valor da soma
        elif how_close_p1 > 0:
            reveal_p1 = 'min'                           # Se o número for negativo, ele ficou atrás do valor da soma
        how_close_p1 = sqrt(how_close_p1 ** 2)          # Modulo matemático, remove o sinal negativo, caso exista

        how_close_p2 = eval(f"{pos_p2} - value_p2")
        if how_close_p2 < 0:
            reveal_p2 = 'max'
        elif how_close_p2 > 0:
            reveal_p2 = 'min'
        how_close_p2 = sqrt(how_close_p2 ** 2)

        # Ação tomada após saber quão próximo o player chegou, se acertou, ou chutou menor, ou chutou maior que a soma.
        if how_close_p1 == 0 and how_close_p2 == 0:     # Ambos acertaram a soma do eixo.
            return 'tie_jackpot'
        elif how_close_p1 == 0:                         # Apenas o player 1 acertou a soma do eixo.
            return 'p1_jackpot'
        elif how_close_p2 == 0:                         # Apenas o player 2 acertou a soma do eixo.
            return 'p2_jackpot'
        elif how_close_p1 == how_close_p2:              # Empate, ambos ficaram a mesma distância
            return 'tie', reveal_p1, reveal_p2
        elif how_close_p1 < how_close_p2:               # Player 1 chegou mais próximo, retorna se foi acima ou abaixo
            return 'p1_win', reveal_p1, reveal_p2
        elif how_close_p2 < how_close_p1:               # Player 2 chegou mais próximo, retorna se foi acima ou abaixo
            return 'p2_win', reveal_p2, reveal_p1


    '''
    Utilizando o retorno da função acima, ele processa qual casa será relevada, se será uma casa do eixo X (linha) ou
    uma casa do eixo Y (coluna) com base no valor maior ou menor, ou até toda uma linha ou coluna. Esse processo modifica
    os valores dos tabuleiros.
    Como a pontuação é baseada em quantas casas foram reveladas, calcula e retorna a pontuação do player vencedor.
    '''
    def reveal(pos, max_or_min):
        # Faz uma cópia, em lista, de cada coluna e cada linha, essas listas são usadas para calcular max ou min do eixo.
        # As listas são sempre atualizadas, recebendo o valor da matriz modificável, caso o valor não seja 0, que representam vazio.
        current_x1 = []
        for i in current_back_board[0]:
            if i != 0:
                current_x1.append(i)

        current_x2 = []
        for i in current_back_board[1]:
            if i != 0:
                current_x2.append(i)

        current_x3 = []
        for i in current_back_board[2]:
            if i != 0:
                current_x3.append(i)

        # Todas as dificuldades de jogo possuem os eixos 3x3, então ele tenta pegar o eixo 4x4 e 5x5, caso exista
        try:
            current_x4 = []
            for i in current_back_board[3]:
                if i != 0:
                    current_x4.append(i)
        except:     # Erro do índice ser inexistente por ser uma matriz menor que 4x4
            current_x4 = []
        try:
            current_x5 = []
            for i in current_back_board[4]:
                if i != 0:
                    current_x5.append(i)
        except:     # Erro do índice ser inexistente por ser uma matriz menor que 5x5
            current_x5 = []

        current_y1 = []
        for p, i in enumerate(current_back_board):
            try:
                if i[0] != 0:
                    current_y1.append(i[0])
            except:
                pass

        current_y2 = []
        for p, i in enumerate(current_back_board):
            try:
                if i[1] != 0:
                    current_y2.append(i[1])
            except:
                pass

        current_y3 = []
        for p, i in enumerate(current_back_board):
            try:
                if i[2] != 0:
                    current_y3.append(i[2])
            except:
                pass

        current_y4 = []
        for p, i in enumerate(current_back_board):
            try:
                if i[3] != 0:
                    current_y4.append(i[3])
            except:
                pass

        current_y5 = []
        for i in current_back_board:
            try:
                if i[4] != 0:
                    current_y5.append(i[4])
            except:
                pass

        # Current assume o valor do eixo que está sendo trabalhado no momento, generalizando.
        current = eval(f"current_{pos}")
        pontos = 1
        if max_or_min == 'read':
            return len(current)
        if len(current) == 0:  # Se tiver vazio, caso já tenham acertado aquela linha ou coluna, não ganha pontos
            return 0
        if max_or_min == 'max':
            for position, item in enumerate(back_board):
                for position2, item2 in enumerate(back_board[position]):
                    if item2 == max(current):   # Achou o valor máximo ATUAL (que não foi revelado ainda)
                        front_board[position][position2] = back_board[position][position2]
                        if max(current) in current_back_board[position]:
                            current_back_board[position][position2] = 0     # A matriz que é modificável, põem 0 no lugar do item revelado
            current.remove(max(current))

        elif max_or_min == 'min':
            for position, item in enumerate(back_board):
                for position2, item2 in enumerate(back_board[position]):
                    if item2 == min(current):   # Achou o valor minimo ATUAL (que não foi revelado ainda)
                        front_board[position][position2] = back_board[position][position2]
                        if min(current) in current_back_board[position]:
                            current_back_board[position][position2] = 0     # A matriz que é modificável, põem 0 no lugar do item revelado
            current.remove(min(current))

        elif max_or_min == 'jackpot' or 'tie_jackpot':
            pontos = len(current)       # Pontos é igual ao total de itens que serão revelados no eixo
            for position, item in enumerate(back_board):
                for position2, item2 in enumerate(back_board[position]):
                    if item2 in current:
                        # O Current assume uma lista ou coluna, a soma foi acertada, a matriz será preenchida com o current
                        front_board[position][position2] = back_board[position][position2]
                        current_back_board[position][position2] = 0     # A matriz que é modificável, põem 0 no lugar dos itens revelados
            current.clear()     # Limpa o current, deixando-o livre para assumir um novo eixo (linha ou coluna)
        # Caso não caia no caso jackpot (revelar toda linha ou coluna) retorna apenas 1 casa revelada
        return pontos


    '''
    Exibe a mensagem de quem acertou, se foi acima ou abaixo, e qual valor chutado que acertou.
    Seu caso recursivo utiliza essa mensagem gerada, para separar e armazenar em uma variável global no eixo que 
    representa a jogada, para assim, mais tarde ser lido o histórico daquele eixo, caso solicitado pelo usuário.
    '''
    def history(call, value, bid_p1, bid_p2):

        loser = ""
        winner = ""
        if call == "read_xy":   # Chamada para leitura, causa por uma solicitação do histórico pelo usuário
            if value == 'all':
                return history_xy
            else:   # Para entender o retorno, olhe a estrutura do dicionário global no início do código
                # O value passado, ex: x1, y1, é um valor desconhecido pela função, então cai no caso do else que o recicla
                return history_xy[value]

        # Mensagem gerada após cada round, histórico apenas da última jogada, no caso recursivo é repassada como value e guardada no dicionário
        elif call == 'round':
            if 'p1_win' == value[0]:
                if 'min' == value[1]:
                    winner = f"{player1} ganhou! O valor chutado {bid_p1:^3} foi ABAIXO da soma\n"
                if 'max' == value[1]:
                    winner = f"{player1} ganhou! O valor {bid_p1:^3} chutado foi ACIMA da soma\n"
                if 'min' == value[2]:
                    loser = f"{player2} perdeu! O valor {bid_p2:^3} chutado foi ABAIXO da soma\n"
                if 'max' == value[2]:
                    loser = f"{player2} perdeu! O valor chutado {bid_p2:^3} foi ACIMA da soma\n"
                who_call['winner'] = 0
                who_call['loser'] = 1

            elif 'p2_win' == value[0]:
                if 'min' == value[1]:
                    winner = f"{player2} ganhou! O valor {bid_p2:^3} chutado foi ABAIXO da soma\n"
                if 'max' == value[1]:
                    winner = f"{player2} ganhou! O valor {bid_p2:^3} chutado foi ACIMA da soma\n"
                if 'min' == value[2]:
                    loser = f"{player1} perdeu! O valor {bid_p1:^3} chutado foi ABAIXO da soma\n"
                if 'max' == value[2]:
                    loser = f"{player1} perdeu! O valor {bid_p1:^3} chutado foi ACIMA da soma\n"
                who_call['winner'] = 1
                who_call['loser'] = 0

            elif 'tie' == value[0]:
                if 'min' == value[1]:
                    winner = f"{player1} chutou {bid_p1:^3} e  {player2} empataram, ABAIXO da soma\n"
                if 'min' == value[2]:
                    loser = f"{player2} chutou {bid_p2:^3} e  {player1} empataram, ABAIXO da soma\n"
                if 'max' == value[1]:
                    winner = f"{player1} chutou {bid_p1:^3} e  {player2} empataram, ACIMA da soma\n"
                if 'max' == value[2]:
                    loser = f"{player2} chutou {bid_p2:^3} e  {player1} empataram, ACIMA da soma\n"
                else:
                    winner = f"{player1} chutou {bid_p1:^3} e  {player2} chutou {bid_p2:^3} e empataram entre a soma\n"
                    loser = f"{player1} chutou {bid_p1:^3} e  {player2} chutou {bid_p2:^3} e empataram entre a soma\n"
                who_call['winner'] = 0
                who_call['loser'] = 1

            elif 'p1_jackpot' == value[0]:
                winner = f"{player1} chutou {bid_p1:^3} e acertou a soma, parabéns!\n"
                if 'min' == value[2]:
                    loser = f"{player2} perdeu, o valor {bid_p2:^3} chutado foi ABAIXO da soma\n"
                elif 'max' == value[2]:
                    loser = f"{player2} perdeu, o valor {bid_p2:^3} chutado foi ACIMA da soma\n"
                who_call['winner'] = 0
                who_call['loser'] = 1

            elif 'p2_jackpot' == value[0]:
                winner = f"{player2} chutou {bid_p2:^3} e acertou a soma, parabéns!\n"
                if 'min' == value[2]:
                    loser = f"{player1} perdeu, o valor {bid_p1:^3} chutado foi ABAIXO da soma\n"
                elif 'max' == value[2]:
                    loser = f"{player1} perdeu, o valor {bid_p1:^3} chutado foi ACIMA da soma\n"
                who_call['winner'] = 1
                who_call['loser'] = 0

            elif 'tie_jackpot' in value[0]:
                winner = f"{player1} chutou {bid_p1:^3} e  {player2} chutou {bid_p2:^3} e ambos acertaram a soma, parabéns!\n"
                who_call['winner'] = 0
                who_call['loser'] = 1
            return winner, loser
        else:
            # O call passado, ex: x1, y1, é um valor desconhecido pela função, então cai no caso do else, que o recicla evitando a
            # necessidade de um parâmetro exclusivo para isso, no caso de vim uma tupla (empate) também é outra forma de reciclar parâmetro
            history_xy[call[who_call['winner']]] += value[0]
            history_xy[call[who_call['loser']]] += value[1]
    '''
    O tabuleiro do jogo, exibe a matriz front_board, histórico da rodada, pontuação de cada jogador, não recebe parâmetros
    pelo fato de exibir somente as variáveis globais, que só são globais para serem enxergadas pelo board
    Para ativar a matriz back_board durante a jogatina, basta remover o comentário da linha 327 e 333.
    '''
    def board():
        if rounds == 256:
            rounds_text = "∞"       # Label de rodadas totais no caso de rodadas infinitas
        else:
            rounds_text = rounds    # Label de rodadas totais no caso de rodadas finitas

        clearConsole()
        print(f"{color('cyan')}{player1} {player1_points} pontos\n"
              f"{color('yellow')}{player2} {player2_points} pontos\n"
              f"{color('')}"
              f"{color('purple')}Rodada atual: ({current_round} / {rounds_text})\n")

        # REMOVA O COMENTÁRIO DE BLOCO ABAIXO PARA VISUALIZAR AMBOS TABULEIROS EM FORMA DE MATRIZ MONTADA ENQUANTO JOGA
        '''
        for linha in range(0, xy):
            for coluna in range(0, xy):
                print(f" {back_board[linha][coluna]:^5} ", end='')
            print("\n")
        print('\n\n')
        '''

        if current_round > 1:   # O histórico só é exibido a partir da segunda rodada
            show_round_history = history('round', come_back, value_p1, value_p2)
            print(show_round_history[0])
            print(show_round_history[1])
            print("\n")

        if xy == 3:
            board_color = color('green')
        elif xy == 4:
            board_color = color('yellow')
        else:
            board_color = color('red')

        # MATRIZ DO TABULEIRO
        for linha1 in range(0, xy):
            for coluna1 in range(0, xy):
                print(f"{board_color} {front_board[linha1][coluna1]:^5} ", end='')
            print("\n")
        print(color(''))

    # Começo da main, fim das funções
    while current_round <= rounds:
        # Como a matriz só vai ser preenchida lá em cima, isso verifica se existem X no front_board, caso não tenha, finaliza o jogo
        count_x = 0
        for list in front_board:
            for item in list:
                if item == 'X':
                    count_x += 1
        # Exibe o board antes de dar break, para a ultima tela do jogador ser como o board final ficou
        board()
        if count_x == 0:
            break


        # TELA DE CHUTAR A SOMA E VALIDAÇÕES DA TENTATIVA DE JOGADA
        # VEZ DO JOGADOR UM
        valid_move = False
        valid_move_value = False
        while not valid_move or not valid_move_value:
            # VALIDA O EIXO JOGADO (ex: x1, x3, u5 [invalido])
            pos_p1 = input(f'{color("cyan")}Posição {player1}: ').upper().strip()
            value_p1 = input(f'{color("")}')
            if len(pos_p1) > 1:                         # VERIFICA SE DIGITOU AO MENOS 2 CARACTERES (impedindo digitar so L ou C)
                if pos_p1[1].isdigit():                 # VERIFICA SE DIGITOU UM NUMERO INTEIRO PARA LINHA / COLUNA
                    if xy >= int(pos_p1[1]) > 0:        # VERIFICA SE O VALOR DIGITADO ESTÁ DENTRO DAS DIMENSÕES DA DIFICULDADE
                        if pos_p1[0] == "L":            # VERIFICA SE JOGOU (L)INHA OU (C)OLUNA, E TRANSFORMA A STRING EM X E Y
                            pos_p1 = f"x{pos_p1[1]}"
                            pos_p1_len = reveal(pos_p1, 'read')
                            if pos_p1_len != 0:         # VERIFICA SE A LINHA JA FOI REVELADA
                                valid_move = True
                            else:
                                print(f"\033[1;31mJogada invalida, {pos_p1} já foi completamente relevado!\033[0;0m")
                                valid_move = False
                        elif pos_p1[0] == "C":
                            pos_p1 = f"y{pos_p1[1]}"
                            pos_p1_len = reveal(pos_p1, 'read')
                            if pos_p1_len != 0:         # VERIFICA SE A COLUNA JA FOI REVELADA
                                valid_move = True
                            else:
                                print(f"\033[1;31mJogada invalida, {pos_p1} já foi completamente relevado!\033[0;0m")
                                valid_move = False
                    else:                               # Registra se a jogada do eixo foi valida, ambas precisam ser
                        valid_move = False
                else:
                    valid_move = False

                # VALIDA O VALOR JOGADOR
                if value_p1.isdigit() or value_p1 == 'historico':
                    # FUNÇÃO DE CHAMAR O HISTÓRICO
                    if value_p1 == 'historico':
                        if pos_p1[0] == 'x':
                            message = f'Linha {pos_p1[1]}'
                        else:
                            message = f'Coluna {pos_p1[1]}'

                        # Constrói o menu de histórico (inicialmente localizado em menu.py)
                        clearConsole()
                        print(color('cyan'), line(1))
                        print(f"{f'HISTÓRICO da {message}':^49}")
                        print(line(2))
                        # Chamada da função histórico, passando um parâmetro aparentemente invalido, caindo no caso do else
                        print(history('read_xy', pos_p1, 0, 0))
                        print(line(1), color(''))
                        # Espera o jogador terminar de ler o histórico, limpa tudo e volta para tela de uma nova tentativa de jogada
                        wait()
                        clearConsole()
                        board()
                        valid_move_value = False
                    else:
                        valid_move_value = True
                else:
                    valid_move_value = False
            else:
                valid_move_value = False
        value_p1 = int(value_p1)

        # VEZ DO JOGADOR DOIS
        valid_move = False
        valid_move_value = False
        while not valid_move or not valid_move_value:
            # VALIDA O LOCAL JOGADO
            pos_p2 = input(f'{color("yellow")}Posição {player2}: ').upper().strip()
            value_p2 = input(f'{color("")}')
            if len(pos_p2) > 1:                         # VERIFICA SE DIGITOU AO MENOS 2 CARACTERES (impedindo digitar so L ou C)
                if pos_p2[1].isdigit():                 # VERIFICA SE DIGITOU UM NUMERO INTEIRO PARA LINHA / COLUNA
                    if xy >= int(pos_p2[1]) > 0:        # VERIFICA SE O VALOR DIGITADO ESTÁ DENTRO DAS DIMENSÕES DA DIFICULDADE
                        if pos_p2[0] == "L":            # VERIFICA SE JOGOU (L)INHA OU (C)OLUNA, E TRANSFORMA A STRING EM X E Y
                            pos_p2 = f"x{pos_p2[1]}"
                            pos_p2_len = reveal(pos_p2, 'read')
                            if pos_p2_len != 0:         # VERIFICA SE A LINHA JA FOI REVELADA
                                valid_move = True
                            else:
                                print(f"\033[1;31mJogada invalida, {pos_p2} já foi completamente relevado!\033[0;0m")
                                valid_move = False
                        elif pos_p2[0] == "C":
                            pos_p2 = f"y{pos_p2[1]}"
                            pos_p2_len = reveal(pos_p2, 'read')
                            if pos_p2_len != 0:         # VERIFICA SE A COLUNA JA FOI REVELADA
                                valid_move = True
                            else:
                                print(f"\033[1;31mJogada invalida, {pos_p2} já foi completamente relevado!\033[0;0m")
                                valid_move = False
                    else:                               # REPETE ATÉ O JOGADOR FAZER UM MOVIMENTO VALIDO
                        valid_move = False
                else:
                    valid_move = False

                # VALIDA O VALOR JOGADOR
                if value_p2.isdigit() or value_p2 == 'historico':
                    if value_p2 == 'historico':
                        if pos_p2[0] == 'x':
                            message = f'Linha {pos_p2[1]}'
                        else:
                            message = f'Coluna {pos_p2[1]}'

                        # Constrói o menu de histórico (inicialmente localizado em menu.py)
                        clearConsole()
                        print(color('yellow'), line(1))
                        print(f"{f'HISTÓRICO da {message}':^49}")
                        print(line(2))
                        # Chamada da função histórico, passando um parâmetro aparentemente invalido, caindo no caso do else
                        print(history('read_xy', pos_p2, 0, 0))
                        print(line(1), color(''))
                        # Espera o jogador terminar de ler o histórico, limpa tudo e volta para tela de uma nova tentativa de jogada
                        wait()
                        clearConsole()
                        board()
                        valid_move_value = False
                    else:
                        valid_move_value = True
                else:
                    valid_move_value = False
            else:
                valid_move_value = False
        value_p2 = int(value_p2)

        # Após ambos terem suas jogadas validadas, o jogo chama a função move para registrar a jogada, passando como
        # parâmetro o chute de ambos e aonde chutaram, salva o return de quem venceu e se foi max ou min na variável come_back
        come_back = move(pos_p1, value_p1, pos_p2, value_p2)
        # come_back volta com 2 valores, quem venceu e como venceu, se foi um valor acima (max) ou abaixo (min)

        # checar os comentários da função move para saber o que cada valor retornado representa
        if 'p1_win' in come_back:
            player1_points += reveal(pos_p1, come_back[1])
        elif 'p2_win' in come_back:
            player2_points += reveal(pos_p2, come_back[1])
        elif 'tie' in come_back:
            if pos_p1 == pos_p2:
                tie_points = reveal(pos_p1, come_back[1])
                player1_points += tie_points
                player2_points += tie_points
            else:
                player1_points += reveal(pos_p1, come_back[1])
                player2_points += reveal(pos_p2, come_back[1])
        elif 'p1_jackpot' in come_back:
            player1_points += reveal(pos_p1, 'jackpot')
        elif 'p2_jackpot' in come_back:
            player2_points += reveal(pos_p2, 'jackpot')
        elif 'tie_jackpot' in come_back:
            if pos_p1 == pos_p2:
                tie_jackpot_points = reveal(pos_p1, 'jackpot')
                player1_points += tie_jackpot_points
                player2_points += tie_jackpot_points
            else:
                tie_jackpot_points = reveal(pos_p1, 'jackpot')
                player1_points += tie_jackpot_points
                try_to_get = reveal(pos_p2, 'jackpot')
                if try_to_get == 0:
                    player2_points += tie_jackpot_points
                else:
                    player2_points += try_to_get
                if pos_p1[0] != pos_p2[0]:
                    player2_points += 1
        # Função recursiva que armazena o histórico do round e histórico geral
        history((pos_p1, pos_p2), history('round', come_back, value_p1, value_p2), value_p1, value_p2)
        current_round += 1

    # FIM DA EXECUÇÃO, O JOGO TERMINOU
    if player1_points == player2_points:    # EMPATE
        return 0, current_round, player1_points, player2_points

    elif player1_points > player2_points:   # JOGADOR 1 VENCEU POR TER MAIS PONTOS
        return 1, current_round, player1_points, player2_points

    else:                                   # JOGADOR 2 VENCEU POR TER MAIS PONTOS
        return 2, current_round, player1_points, player2_points

