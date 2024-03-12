email_tmpl = """

Ola %(nome)s,

Tem interesse em comprar %(produto)s?

Este produto é ótimo para resolver %(texto)s.

Clique agora em %(link)s.

Apenas %(quantidade)d disponíveis!

Preço promocional %(preco).2f.
"""

clientes = ["Rita", "Lourdes", "Paloma"]

for cliente in clientes:
    print(
        email_tmpl % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "Escrever muito bem.",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 20.6
        }
    )
