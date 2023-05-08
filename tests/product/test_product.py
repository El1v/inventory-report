from inventory_report.inventory.product import Product

id = 1
nome_do_produto = "Nome do Produto"
numero_de_serie = "12345678910"
nome_da_empresa = "Nome da Empresa"
data_de_fabricacao = "08/05/2023"
data_de_validade = "09/05/2023"
instrucoes_de_armazenamento = "...instruções..."


def test_cria_produto():
    product = Product(
        id=id,
        nome_do_produto=nome_do_produto,
        numero_de_serie=numero_de_serie,
        nome_da_empresa=nome_da_empresa,
        data_de_fabricacao=data_de_fabricacao,
        data_de_validade=data_de_validade,
        instrucoes_de_armazenamento=instrucoes_de_armazenamento,
    )

    assert isinstance(product.id, int)
    assert isinstance(product.nome_do_produto, str)
    assert isinstance(product.numero_de_serie, str)
    assert isinstance(product.nome_da_empresa, str)
    assert isinstance(product.data_de_fabricacao, str)
    assert isinstance(product.data_de_validade, str)
    assert isinstance(product.instrucoes_de_armazenamento, str)

    assert product.id == id
    assert product.nome_do_produto == nome_do_produto
    assert product.numero_de_serie == numero_de_serie
    assert product.nome_da_empresa == nome_da_empresa
    assert product.data_de_fabricacao == data_de_fabricacao
    assert product.data_de_validade == data_de_validade
    assert product.instrucoes_de_armazenamento == instrucoes_de_armazenamento
