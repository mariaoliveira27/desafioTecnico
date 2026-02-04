
# Função para verificar se uma sequência de parênteses, colchetes e chaves está válida
def parenteses_validos(s):
    pilha = []  # Pilha para armazenar os símbolos de abertura
    mapa = {')': '(', '}': '{', ']': '['}  # Mapeia cada fechamento para sua abertura correspondente
    for char in s:
        if char in mapa.values():  # Se for símbolo de abertura, adiciona à pilha
            pilha.append(char)
        elif char in mapa.keys():  # Se for símbolo de fechamento
            # Verifica se há símbolo de abertura correspondente no topo da pilha
            if not pilha or pilha[-1] != mapa[char]:
                return False  # Ordem errada ou falta de abertura
            pilha.pop()  # Remove o símbolo de abertura correspondente
    # Se a pilha estiver vazia ao final, está tudo válido
    return len(pilha) == 0


# Bloco principal do programa
if __name__ == "__main__":
    # Solicita ao usuário uma sequência de parênteses, colchetes e chaves
    s = input("Digite uma sequência de parênteses: ")
    # Chama a função e exibe o resultado
    if parenteses_validos(s):
        print("A sequência é válida.")
    else:
        print("A sequência é inválida.")

# Exemplos de uso
#print (parenteses_validos("{[()]}"))     # True
#print (parenteses_validos("{[(])}"))     # False
#print (parenteses_validos("{{[[(]]}}"))  # False
