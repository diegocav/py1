class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message
while True:
    try:
        x = float(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota acima de 10 não permitida')
        elif x < 0:
            raise InputError('Nota menor que zero não permitida')
        break
    except ValueError:
        print('Valor inválido. Apenas números permitidos')
    except InputError as ex:
        print(ex)