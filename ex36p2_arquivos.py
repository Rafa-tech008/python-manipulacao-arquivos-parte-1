#OP.ARQ_LT01.36
#Declaração de variáveis

#Início
import os

def ler_conteudo (dir01, arq01):
    arquivo01 :str = ''
    arquivo01= dir01 + arq01
    if (os.path.exists(dir01) and os.path.isdir(dir01)):
        with open (arquivo01) as file:
            for linha in file:
               print (linha, end = '')
    else:
        print ('Diretório inválido')


def ler_conteudo_operacao (dir01, arq01):
    valor: int = 0
    buffer:str = ''
    arquivo01: str = ''
    arquivo01 = dir01 + arq01
    if (os.path.exists(dir01) and os.path.isdir(dir01)):
        with open (arquivo01) as file:
            for linha in file:
                if ("Maior" not in linha and "Menor" not in linha):
                    valor = int(linha)
                    if (valor % 5 == 0):
                        print (f"O valor {linha} é divísivel por 5")
                        buffer += (str(valor) + '\n')
                    else:
                        print (f"O valor {linha} não é divísivel por 5")
        return buffer            
    else:
        print ('Diretório inválido')

def escrever_conteudo_op (dir03, arq04, buffer_conteudo):
    arquivo01: str = ''
    tipo: str = '' 
    enc: str = ''
    arquivo01 = dir03 + arq04

    if (os.path.exists (dir03) and os.path.isdir (dir03)):
        tipo = 'w'
        enc = 'utf-8'
        with open (arquivo01, tipo, encoding=enc) as file:
            file.write (buffer_conteudo)

def main ():   
    dir00:str = ''
    arq00:str = '' 
    arq02:str = ''
    
    dir00= '/media/sf_VS_Code/Atividades_python/atividade_04/'
    arq00= 'exercicio36p01.txt'
    arq02 = 'exercicio36p02.txt'
    buffer= ler_conteudo_operacao (dir00, arq00)

    ler_conteudo (dir00, arq00) 

    ler_conteudo_operacao (dir00, arq00)

    escrever_conteudo_op (dir00, arq02, buffer)

if (__name__ == "__main__"):
    main ()

#Fim