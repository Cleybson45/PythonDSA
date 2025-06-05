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
opcao_menu = input("Selecione a opção: ")

#Função de Cadastra Ativos no Estoque
def cadastra_ativo(nome, qtd, categoria):
    nomes.append(nome)
    quantidades.append(qtd)
    categorias.append(categoria)
    print(f"\nAtivo adicionado.. \nNome: {nome} | Quantidade: {qtd} | Categoria: {categoria}")

if opcao_menu == "1":
    nome = input("Nome do Produto: ")
    qtd = int(input("Quantidade do Produto: "))
    cat = input("Categoria do Produto: ")
    cadastra_ativo(nome, qtd, cat)

'''elif opcao_menu == "2":
    nome = input("Nome do Produto: ")
    qtd = int(input("Quantida do Produto: "))
    remove_ativo(nome, qtd)

elif opcao_menu == "3":
    print("\Ativos em Estoque...\n")
    for nome, qtd, cat in zip(nomes, quantidades, categorias):
        print(f"Nome: {nome}, Quantidade: {qtd}, Categoria: {cat}")

elif opcao_menu == "4":
    cat = input("Categoria: ")
    por_categoria(nome, qtd, cat)'''