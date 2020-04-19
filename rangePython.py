#
# for num in range(101):
#     div = 0
#     for x in range(1, num):
#         resto = num % x
#         if resto == 0:
#             div +=1
#     if div == 2:
#         print(num)

nota = float(input('Entrecom sua nota: '))
while nota > 10:
    nota = float(input('Informe nota válida:'))
