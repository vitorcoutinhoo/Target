# Questão 4

faturamentoEstado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27129.48,
    "Outros": 19849.53
}

def percentFaturamento(faturamentoEstado):
    total = sum(faturamentoEstado.values())
    percent = {}
    for key, value in faturamentoEstado.items():
        percent[key] = f"{value / total * 100:.2f}"
    return percent

percent = percentFaturamento(faturamentoEstado)
print("Faturamento Total:")
print(f"R$ {sum(faturamentoEstado.values()):.2f}")
print("\nPercentual de faturamento por estado:")
for key, value in percent.items():
    print(f"{key}: {value}%")