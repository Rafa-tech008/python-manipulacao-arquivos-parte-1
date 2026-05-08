#OP.ARQ_LT01.38
#Declaração de variáveis

#Início
import os

def fat_operacao (num):
    fat = 1
    for i in range (1, num + 1):
        fat *= i
    return fat


def div_operacao (num):
    div = 0
    buffer: str = ''  
    for i in range (1, num + 1):
        fat = fat_operacao (i)
        div += i / fat
        buffer += (f"{div: 4f} \n")
    return buffer
        

def escreve_func (dir00, arq00, buffer_conteudo):
    tipo: str = ''
    enc: str = ''
    arquivo00 = dir00 + arq00

    if os.path.exists (dir00) and os.path.isdir (dir00):
        if os.path.exists (arquivo00):
                tipo = 'w'
                enc ='utf-8'
                with open (arquivo00, tipo, encoding=enc) as file:
                    file.write (buffer_conteudo)
    else:
        ("Diretório inválido.")


def main ():
    dir: str = ''
    arq: str = ''
    numero: int = 0

    dir = '/media/sf_VS_Code/Atividades_python/atividade_07/Arquivos.txt/'
    arq =  'exercicio38.txt'

    numero = int(input("Digite um valor: "))
    buffer = div_operacao (numero)

    fat_operacao (numero)

    div_operacao (numero)

    escreve_func (dir, arq, buffer)

if (__name__ == "__main__"):
    main()