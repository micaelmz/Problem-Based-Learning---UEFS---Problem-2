# Autor: Micael Muniz de Oliveira Santos
# Componente Curricular: Algoritmos I
# Concluído em: 21/05/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

'''
DIFFICULTY SELECT:
Inicialmente, processava todos os parâmetros relacionados a matriz necessários para o funcionamento do jogo, porém a
biblioteca random gerava novos valores todas as vezes que o modulo era chamado, portanto, ele apenas fornece algumas
informações iniciais sobre o tabuleiro, com base na dificuldade escolhida pelo jogador.
'''


from random import sample


def easy(request):
    numbers = sample(range(1, 31), 9)
    if request == 'xy':
        return 3
    if request == 'back_board':
        return [[numbers[0], numbers[1], numbers[2]],
                [numbers[3], numbers[4], numbers[5]],
                [numbers[6], numbers[7], numbers[8]]]
    if request == 'front_board':
        return [['X', 'X', 'X'],
                ['X', 'X', 'X'],
                ['X', 'X', 'X']]


def medium(request):
    numbers = sample(range(1, 61), 16)
    if request == 'xy':
        return 4
    if request == 'back_board':
        return [[numbers[0], numbers[1], numbers[2], numbers[3]],
                [numbers[4], numbers[5], numbers[6], numbers[7]],
                [numbers[8], numbers[9], numbers[10], numbers[11]],
                [numbers[12], numbers[13], numbers[14], numbers[15]]]

    if request == 'front_board':
        return [['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X']]


def hard(request):
    numbers = sample(range(1, 101), 25)
    if request == 'xy':
        return 5
    if request == 'back_board':
        return [[numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]],
                [numbers[5], numbers[6], numbers[7], numbers[8], numbers[9]],
                [numbers[10], numbers[11], numbers[12], numbers[13], numbers[14]],
                [numbers[15], numbers[16], numbers[17], numbers[18], numbers[19]],
                [numbers[20], numbers[21], numbers[22], numbers[23], numbers[24]]]

    if request == 'front_board':
        return [['X', 'X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X', 'X']]
