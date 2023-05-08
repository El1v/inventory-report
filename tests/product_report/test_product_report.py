from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Nome do Produto",
        "Nome da Empresa",
        "08-05-2023",
        "10-05-2023",
        "Numero de Série",
        "...instrucoes...",
    )

    assert product.__repr__() == (
        "O produto Nome do Produto fabricado em 08-05-2023 "
        "por Nome da Empresa com validade até 10-05-2023 "
        "precisa ser armazenado ...instrucoes...."
    )
