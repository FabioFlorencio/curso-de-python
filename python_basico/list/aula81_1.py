
lista = [10,20,30,40]

print('Lista sem alterração:',lista)

# append -> inclui um item no final da lista
lista.append(50)

lista.append(int(input('Adicione um item na lista:')))

print('Nova lista:',lista)

# guarda o valor que foi retirado do final da lista
ultimo_valor = lista.pop()

print(lista,'Item removido da lista:', ultimo_valor)
print('Teste',lista)

posicao = int(input('Indique a posição para retirar um item da lista:'))

guarda_valor_retirado = lista.pop(posicao)

print(f'Foi retirado da posição {posicao}, o item {guarda_valor_retirado} da lista',lista)



