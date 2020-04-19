#
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo Valor: '))
# c = int(input('Terceiro valor: '))
# if a > b and a > c:
#     print('O maior número é: {}' .format(a))
# elif b > a and b > c:
#     print('O maior numero é: {}' .format(b))
# else:
#     print('O maior número é: {}' .format(c))
# print('Fim do Programa!')
# ---------------------------------------------
# a = int(input('Entre com um valor: '))
# b = int(input('Entre com o segundo valor'))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b ==0:
#     print('Extite número par!')
# else:
#     print('Existe número ímpar')

while True:
    try:
        a = float(input('Primeiro bimestre: '))
        if not 0 <= a <= 10:
            raise ValueError('Valor não permitido.')
        break
    except ValueError as error:
            print('Entre com valor válido: ')
b = float(input('Segundo bimestre: '))
c = float(input('Terceiro bimestre: '))
d = float(input('Quarto bimestre: '))
media = (a + b + c + d) / 4
if media >= 7:
    print('Média final: {} - Aprovado!' .format(media))
else:
    print('Média final: {} - Não aprovado!' .format(media))
