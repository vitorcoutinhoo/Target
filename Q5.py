# Questão 5

# string a ser invertida
string = "Vitor"

# inverte a string
# poderia ser feito com string[::-1]
def inverteString(string):
    aux = ""
    for i in range(len(string) - 1, -1, -1):
        aux += string[i]
    return aux

print(inverteString(string))
