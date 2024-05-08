

nome = 'Fábio Florêncio'
novo_nome=""

i = 0


while i < len(nome):    
    novo_nome+= f'*{nome[i]}'
    i+= 1

print(novo_nome,end="*")    

print()

for letra in 'Fabio Florêncio ':
    print(letra,end="*")