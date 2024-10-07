def produto_mais_vendido(produtos):

    contagem = {}

    for produto in produtos:
        produto = produto.strip()
        contagem[produto] = contagem.get(produto, 0) + 1

    print(contagem)
    # Encontrar o produto com a maior contagem de forma mais concisa:
    max_produto = max(contagem, key=contagem.get)

    return max_produto

def obter_entrada_produtos():
    entrada = input()
    produtos = entrada.split(',')
    return produtos

produtos = obter_entrada_produtos()
mais_vendido = produto_mais_vendido(produtos)

print(mais_vendido)