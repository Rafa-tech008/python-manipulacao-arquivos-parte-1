#OP.ARQ_LT01.38
#Declaração de variáveis

#Início
import os
import random


def cria_arquivo (dir, arq, buffer_conteudo):
    arquivo: str = ''
    tipo: str = ''
    enc: str = ''

    arquivo= dir + arq
    if (os.path.exists(dir) and os.path.isdir(dir)):
        enc = 'utf-8'
        tipo = 'w'
        if (os.path.exists(arquivo)):
            with open (arquivo, tipo, encoding=enc) as file:
                file.write(buffer_conteudo)

    else: 
        print ('Diretório inválido.')


def main ():
    dir01:str = ''
    arq01:str = ''
    buffer: str = ''
    maior:int = 0
    menor:int = 0
    
    dir01 = '/media/sf_VS_Code/Atividades_python/atividade_04/Arquivos.txt/'
    arq01 = 'exercicio36p01.txt'

    for i in range (100):
        entrada= random.randint (0,100000) 
        print('Digite um número positivo:', entrada)

        if (entrada < 0):
            print ("Valor inválido")
            continue

        buffer += (str(entrada) + '\n')

    if (maior is None or entrada > maior):
        maior = entrada

    if (menor is None or entrada < menor):
        menor = entrada

    buffer += ('Maior valor:' + str(maior) + '\n')
    buffer += ('Menor valor:' + str(menor) + '\n')


    cria_arquivo (dir01, arq01, buffer)

if __name__ == '__main__':
    main()

#Fim