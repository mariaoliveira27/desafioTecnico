#palindromo

# Função recursiva para verificar se uma palavra é palíndromo
# Recebe a string s, o índice inicial (left) e o final (right)
def isPalindrome(s, left, right):
    return True if left >= right else (s[left] == s[right]) and isPalindrome(s, left + 1, right - 1) if left is not None and right is not None else isPalindrome(s, 0, len(s) - 1)

if __name__ == "__main__":
    # Solicita ao usuário uma palavra para análise
    s = input("Digite uma palavra: ")
    # Chama a função e exibe o resultado
    if isPalindrome(s):
        print(f'"{s}" é um palíndromo')
    else:
        print(f'"{s}" não é um palíndromo')