
# Função para encontrar números duplicados em uma lista
# Recebe uma lista de inteiros e retorna um conjunto com os duplicados
def encontrar_duplicados(nums):
    vistos = set()      # Armazena os números já vistos
    duplicados = set()  # Armazena os números duplicados
    for num in nums:
        if num in vistos:      # Se o número já foi visto, é duplicado
            duplicados.add(num)
        else:
            vistos.add(num)   # Se não foi visto, adiciona ao conjunto de vistos
    return duplicados         # Retorna o conjunto de duplicados


# Bloco principal do programa
if __name__ == "__main__":
    # Solicita ao usuário uma lista de números separados por vírgula
    s = input("Digite uma lista de números separados por vírgula: ")
    # Converte a string de entrada em uma lista de inteiros
    lista = [int(x.strip()) for x in s.split(",") if x.strip()]
    # Chama a função para encontrar duplicados
    duplicados = encontrar_duplicados(lista)
    # Exibe o resultado
    if duplicados:
        print("Números duplicados:", ", ".join(str(x) for x in sorted(duplicados)))
    else:
        print("Nenhum número duplicado encontrado.")
    