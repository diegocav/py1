# # lista = [1, 3, 5, 7]
# lista_animal = ['cachorro', 'gato', 'elefante']
# #
# # lista.sort()
# # lista_animal.sort()
# # print(lista)
# # print(lista_animal)
# #
# # lista_animal.reverse()
# # print(lista_animal)
# #
# # if 'lobo' in lista_animal:
# #     print('Existe')
# # else:
# #     print('Não Existe')
# #     lista_animal.append('lobo')
# #     print(lista_animal)
# #
# # lista_animal.pop()
# # print(lista_animal)
# #
# # lista_animal.remove('gato')
# # print(lista_animal)
#
#
# tupla = (1, 10, 12, 14)
# print(len(tupla))
# print(len(lista_animal))
# tupla_animal = tuple(lista_animal)
# print(type(tupla_animal))
# print(tupla_animal)
#
# lista_numerica = list(tupla)
# print(type(lista_numerica))
# print(lista_numerica)


conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
#print(conjunto_uniao)
conjunto_interseccao = conjunto.intersection(conjunto2)
#print(conjunto_interseccao) - iguais entre os conjuntos

conjunto_diferenca = conjunto.difference(conjunto2)
#print(conjunto_diferenca) - diferenca 1 pra 2

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
#print(conjunto_diff_simetrica)

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_a)
print(conjunto_subset)

# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)