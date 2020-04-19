
lista = [1, 10]
arquivo = open('Teste.src', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 2
    numero = lista[1]
    print('Fechando arquivo.')
    arquivo.close()
except ZeroDivisionError:
    print('Nao é possível divisão por zero')
except IndexError:
    print('Erro ao acessar indíce inválido')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}' .format(ex))
