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
__version__ = "0.1.2"
__author__ = " Dara Aragao"
__license__ = "Unlicense"

import os 

current_language= os.getenv("LANG", "es_SP")[:5]

msg = { 
    "en_US": "Hello, World",
    "pt_BR": "Olá, mundo!",
    "es_SP": " Hola, Mundo!",       
    }
       
print(msg[current_language])
