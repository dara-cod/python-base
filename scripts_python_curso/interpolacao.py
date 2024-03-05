In [17]: email_tmpl = """
    ...: Ola %(iniciais)s
    ...:
    ...: Tem interesse em comprar %(produto)s?
    ...:
    ...: Este produto é ótimo para resolver
    ...: %(texto)s
    ...:
    ...: Clique agora em %(link)s
    ...:
    ...: Apenas %(quantidade)d disponiveis!
    ...:
    ...: preço promocional %(preco).2f
    ...: """

In [18]: clientes = ["Darildes, "Lourdes", "Dega"]
  Cell In[18], line 1
    clientes = ["Darildes, "Lourdes", "Dega"]
                                           ^
SyntaxError: unterminated string literal (detected at line 1)


In [19]: clientes = ["Debora"]

In [20]: for cliente in clientes:
    ...:     print(
    ...:         email_tmpl
    ...:         %  {
    ...:             "iniciais": cliente,
    ...:             "produto": "caneta",
    ...:             "texto": "Escrever muito bem.",
    ...:             "link": "https://canetaslegais.com",
    ...:             "quantidade": 1,
    ...:             "preco": 50.6
    ...:         }
    ...:     )
    ...: