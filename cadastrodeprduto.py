"""Cadastro de Produto"""
__version__ = "0.1.0"

produto = { 
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,
}

compra = {
    "cliente": {"nome": "Dara"},
    "quantidade": 3,
    "produto": produto,
}

total_compra = compra["quantidade"] * produto["preco"]


print(
    f"O cliente {compra['cliente']['nome']}"
    f" Comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
)
