"""
Hello World Multi Linguas. 

Dependendo da lingua configurada no ambiente o programa exibe a mensagem correspondente. 

Como usar?

Tenha a variável LANG devidamente configurada.

        export LANG=pt_BR
Execução: 
        python 3 hello.py
        ou
        ./hello.py
"""
__version__ = "0.0.1"
__author__ = " Dara Aragao"
__license__ = "Unlicense"

import os 

current_language="pt_BR"

#Essa parte está exibindo hello wold#
msg="Hello, World"

if current_language=="pt_BR":
    msg="Olá, Mundo!"
elif current_language=="it_IT":
    msg="Ciao, Mondo!"
elif current_language=="es_SP":
    msg="Hola, Mundo!"
        
print(msg)
