'''
📝 Desafio: Sistema Simples de Controle de Estoque com Listas

📦 Cenário:
Você vai criar um pequeno sistema que controla os produtos de um estoque de equipamentos (ex: notebooks, monitores, teclados). 
Cada produto deve ter: Nome, Quantidade e Categoria.

🎯 O que você deve fazer:
1. Criar três listas: nomes, quantidades, categorias.
2. Criar uma função para adicionar novos produtos ao estoque.
3. Criar uma função para exibir todos os produtos.
4. Criar uma função para remover um produto pelo nome.
5. Criar uma função para mostrar todos os produtos de uma categoria específica.
6. Ordenar os produtos pelo nome ou pela quantidade.
7. Calcular a quantidade total de itens no estoque.
'''

'''Pseudocódigo:
1. Definir as listas
2. Criar uma função para povoar as listas com interação do usuário
3. Criar função para apresentar os equipamentos cadastrados
5. Criar uma função para remover equipamentos cadastrados
6. Criar uma função para mostr  
'''

nomes = []
quantidades = []
categorias = []

print("\n*****\n" \
    "BEM VINDO AO ESTOQUE!\n" \
    "**********\n")
print("Menu: \n" \
    " 1 - Cadastrar Ativo \n" \
    " 2 - Remover Ativo \n" \
    " 3 - Listar Ativos \n" \
    " 4 - Listar por Categoria \n" \
    " 5 - Ordenar por nome ou quantidade \n" \
    " 6 - Calcular quantidade em Estoque\n")
opcao_meno = input("Selecione a opção: ")
