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


while True:
    estoque = list(zip(nomes, quantidades, categorias))
    print("\n♦♦♦♦♦♦♦\n" \
        "BEM VINDO AO ESTOQUE!\n" \
        "♦♦♦♦♦♦♦♦♦♦♦♦\n")
    print("Menu: \n" \
        " 1 - Cadastrar Ativo \n" \
        " 2 - Remover Ativo \n" \
        " 3 - Listar Ativos \n" \
        " 4 - Listar por Categoria \n" \
        " 5 - Ordenar por nome ou quantidade \n" \
        " 6 - Calcular quantidade em Estoque\n" \
        " 0 - Sair")
    opcao_menu = input("Selecione a opção: ")

    #Função para Cadastrar Ativos no Estoque
    def cadastra_ativo(nome, qtd, categoria):
        nomes.append(nome)
        quantidades.append(qtd)
        categorias.append(categoria)
        print(f"\nAtivo adicionado.. \nNome: {nome} | Quantidade: {qtd} | Categoria: {categoria}")

    # Função para Remover Ativos no Estoque
    def remove_ativo(nome):
        if nome in nomes: 
            indice = nomes.index(nome)
            nomes.pop(indice)
            quantidades.pop(indice)
            categorias.pop(indice)
            print(f"\n Ativo Removido..")
        else: 
            print("Produto Não Encontrado.")

    # Função para Listar os Ativos em Estoque
    def ativos_estoque():
        for nome, qtd, cat in zip(nomes,quantidades,categorias):
            print(f"Nome: {nome} | Quantidade: {qtd} | Categoria: {cat}")

    # Função para Listar por Categoria
    def lista_por_categoria(cat):
        if cat in categorias:
            for x in range(len(categorias)):
                if categorias[x] == cat:
                    print(f"Nome: {nomes[x]} | Quantidade: {quantidades[x]} | Categoria: {categorias[x]}")   
        else:
            print("Categoria Não Encontrada")

    # Função para Ordenar por Nome ou Quantidade
    def ordenaLista(estoque, ordem):
        if ordem == "Nome":
            estoque.sort(key=lambda item: item[0])
            for nome, qtd, cat in estoque:
                print(f"\nNome: {nome} | Quantidade: {qtd} | Categoria: {cat}")
        else: 
            estoque.sort(key=lambda item: item[1])
            for nome, qtd, cat in estoque:
                print(f"\nNome: {nome} | Quantidade: {qtd} | Categoria: {cat}")

    # Função para Calcular a Quantidade Total de ativos no Estoque
    def qtdTotal():
        qtdTotal = sum([item[1] for item in estoque])
        print(f"\nTemos um total de {qtdTotal} itens em Estoque")

    if opcao_menu == "1":
        nome = input("Nome do Produto: ")
        qtd = int(input("Quantidade do Produto: "))
        cat = input("Categoria do Produto: ")
        cadastra_ativo(nome, qtd, cat)

    elif opcao_menu == "2":
        nome = input("Nome do Produto: ")
        remove_ativo(nome)

    elif opcao_menu == "3":
        print("\Ativos em Estoque...\n")
        ativos_estoque()

    elif opcao_menu == "4":
        cat = input("Categoria: ")
        lista_por_categoria(cat)

    elif opcao_menu == "5":
        ordem = input("Deseja ordenar por Nome ou Quantidade? ")
        ordenaLista(estoque, ordem)
    
    elif opcao_menu == "6":
        qtdTotal()
    
    elif opcao_menu == "0":
        print("\nTchau, até logo..\n")
        break

    else: 
        print("Opção Inválida")