# 🚀 Desafio Técnico - DataViva

Este repositório contém as soluções para o desafio técnico proposto pela **DataViva**. O objetivo foi resolver 5 problemas de lógica e manipulação de dados, focando em clareza de código, boas práticas e eficiência algorítmica.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** [Python 3.x] 
* **Bibliotecas:** [Nenhuma (soluções nativas)]
* **IDE:** [VS Code]

## 📂 Estrutura do Projeto

Cada desafio foi separado em um arquivo independente para facilitar a execução e revisão:

| Arquivo | Desafio | Descrição |
| :--- | :--- | :--- |
| `desafio1.[py/js]` | **O Clássico FizzBuzz** | Algoritmo que imprime múltiplos de 3, 5 e ambos. |
| `desafio2.[py/js]` | **Verificador de Palíndromo** | Função para verificar strings espelhadas. |
| `desafio3.[py/js]` | **Encontrar Duplicados** | Identificação de números repetidos em listas. |
| `desafio4.[py/js]` | **Validação de Parênteses** | Validação de estrutura e ordem de fechamento (`Stacks`). |
| `desafio5.[py/js]` | **Manipulação de Dados** | **(Bônus)** Agrupamento e soma de valores por categoria. |

## 🧠 Abordagem e Decisões de Design

Durante o desenvolvimento, priorizei a **legibilidade** e a **complexidade de tempo (Big O)**. Alguns destaques:


- **Desafio 3 (Duplicados):** Utilizei **conjuntos (sets)** para identificar elementos repetidos de forma eficiente, aproveitando a busca em tempo constante médio (**O(1)**).
- **Desafio 4 (Validação de Parênteses):** A solução foi implementada com o uso de uma **pilha (stack)**, garantindo que os parênteses fossem fechados na **ordem correta** e pelo **tipo correspondente**.
- **Desafio 5 (Bônus):** Optei por **[dicionários nativos ]**, considerando **[performance e controle de memória / facilidade de manipulação e análise de dados]**, de acordo com a natureza do problema proposto.


## 🚀 Como Executar

Certifique-se de ter o [Python/Node.js] instalado em sua máquina.

1. Clone este repositório:
   ```bash
   git clone [https://github.com/](https://github.com/)[SEU-USUARIO]/desafio-dataviva-[SEU-NOME].git
2. Entre na pasta do projeto:
   ```bash
   git clone [https://github.com/](https://github.com/)[SEU-USUARIO]/desafio-dataviva-[SEU-NOME].git
3. Execute os arquivos individualmente. Exemplo:
   ```bash
   python desafio1.py
   python desafio5.py
