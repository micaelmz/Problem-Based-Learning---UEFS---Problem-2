# Autor: Micael Muniz de Oliveira Santos
# Componente Curricular: Algoritmos I
# Concluído em: 21/05/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

'''
SEVEN ELEVEN:
Assim como o 7-Eleven da realidade, este arquivo funciona como uma loja de conveniências, fornecendo diversas funções
e utilitários a todos os arquivos do projeto. Por consequência, ele é chamado com from seven_eleven import *
para assim, utilizar as funções deste, como se fossem nativas daquele arquivo.
'''

# MUDAR CORES DO TEXTO
def color(c):
    if c == 'red':
        return "\033[1;31m"
    elif c == "yellow":
        return "\033[1;93m"
    elif c == 'blue':
        return "\033[1;34m"
    elif c == 'green':
        return "\033[1;32m"
    elif c == 'purple':
        return "\033[1;35m"
    elif c == 'cyan':
        return "\033[1;96m"
    elif c == 'bold':
        return "\033[;1m"
    else:
        return "\033[0;0m"

# LIMPA A TELA
def clearConsole():
    '''
    import os
    import platform
    if platform.system() == 'Windows':
        return os.system('cls') or None
    elif platform.system() == 'Linux':
        return os.system('clear')
    else:
        return '\n'*150
    '''
    return print('\n' * 150)

# IMPRIME UMA LINHA, PADRONIZADA
def line(type):
    if type == 1:
        return "================================================="
    elif type == 2:
        return "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="

# ESPERA UM COMANDO DO USUÁRIO, UTILIZADO QUANDO UMA INFORMAÇÃO QUE DEVE SER LIDA, SERÁ APAGADA POSTERIORMENTE
def wait():
    print(color('bold'), color('red'), 'pressione enter para continuar!')
    '''
    print(" ___________\n"
          "| |  𝙀𝙉𝙏𝙀𝙍 ||\n"
          "| |________||\n"
          "| /________\|\n")
    '''
    input(color(''))