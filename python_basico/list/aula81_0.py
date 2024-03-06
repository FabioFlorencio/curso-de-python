''' 
# Métodos úteis:

    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop    - Remove do final ou do índice escolhido
    del    - apaga um índice
    clear  - limpa lista
    extend - extend a lista

    CRUD -> Create read, update, delete
    Criar, ler, alterar, apagar,

    Evite remover itens no meio da lista, devido que a lista será reorganizada gerando um processamento. Se possível retire itens no final da  lista.
'''

lista = [10,20,30,40]

print('Lista sem alterração:',lista)

# O del apaga um elemento da lista conforme o índice indicado.

del lista[2]

print('Lista após alterração:',lista)

# append -> inclui um item no final da lista
lista.append(50)

lista.append(int(input('Adicione um item na lista:')))

print(lista)

# guarda o valor que foi retirado
ultimo_valor = lista.pop()

print('O método pop retira um item do final da lista:',lista,'Retira mais um item',lista.pop())
print(lista,'Item removido da lista:', ultimo_valor)

posicao = int(input('Indique a posição para retirar um item da lista:'))

guarda_valor_retirado = lista.pop(posicao)

print(f'Foi retirado da posição {posicao}, o item {guarda_valor_retirado} da lista.\nVeja a nova lista',lista)



