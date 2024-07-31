'''

    List comprehension

'''

string = 'Fábio Florêncio'
nova_string = [letra for letra in string]
nova_string_1 = ''.join([letra for letra in string])

print(nova_string)
print(nova_string_1)