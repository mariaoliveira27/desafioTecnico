
# Lista de dicionários representando despesas, cada um com uma categoria e valor
bancoDeDados = [
    {"Categoria": "Alimentação", "valor": 150.0},
    {"Categoria": "Transporte", "valor": 100.0},
    {"Categoria": "Lazer", "valor": 200.0},
    {"Categoria": "Hospedagem", "valor": 300.0},
    {"Categoria": "Hospedagem", "valor": 150.0},
    {"Categoria": "Transporte", "valor": 75.5}
]

    
# Função para somar os valores das despesas por categoria
# Recebe uma lista de despesas e retorna um dicionário com o total por categoria
def calcular_Por_Categoria(despesas):
    total = {}  # Dicionário para armazenar o total por categoria
    for item in despesas:
        categoria = item["Categoria"]  # Extrai a categoria da despesa
        valor = item["valor"]          # Extrai o valor da despesa
        if categoria in total:
            total[categoria] += valor  # Soma ao total existente
        else:
            total[categoria] = valor  # Cria nova entrada para a categoria
    return total

# Bloco principal do programa
if __name__ == "__main__":
    # Chama a função para calcular o total por categoria
    totais = calcular_Por_Categoria(bancoDeDados)
    # Exibe o resultado formatado
    for categoria, valor in totais.items():
        print(f"{categoria}: {valor:.2f}")