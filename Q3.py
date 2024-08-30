import json

# Questão 3

# exemplo de 5 dias de faturamento
with open('Q3.json') as file:
    data = json.load(file)
    aux = data['faturamento']

faturamento = []
for key, value in aux.items():
    if value != 0:
        faturamento.append(value)

# poderia usar a func sum() do python
# mas a ideia é mostrar como fazer manualmente
def mediaFaturamento(faturamento):
    soma = 0
    for i in faturamento:
        soma += i
    return soma / len(faturamento)

# poderia usar a func min() e max() do python
# mas a ideia é mostrar como fazer manualmente
def minFaturamento(faturamento):
    minimo = faturamento[0]
    for i in faturamento:
        if i < minimo:
            minimo = i
    return minimo


def maxFaturamento(faturamento):
    maximo = faturamento[0]
    for i in faturamento:
        if i > maximo:
            maximo = i
    return maximo


def diasAcimaMedia(faturamento):
    media = mediaFaturamento(faturamento)
    dias = 0
    for i in faturamento:
        if i > media:
            dias += 1
    return dias


print(f"O menor faturamento foi de R${minFaturamento(faturamento)}")
print(f"O maior faturamento foi de R${maxFaturamento(faturamento)}")
print(f"A média de faturamento foi de R${mediaFaturamento(faturamento)}")
print(f"\nO número de dias em que o faturamento foi superior à média foi de {diasAcimaMedia(faturamento)}")
print(f"Representando {diasAcimaMedia(faturamento)/len(faturamento)*100}% dos dias")
