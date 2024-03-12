"""
Hello World Multi Linguas. 

Dependendo da lingua configurada no ambiente o programa exibe a mensagem correspondente. 

Como usar?

Tenha a variável LANG devidamente configurada.

        export LANG=pt_BR
Ou informe atraves do CLI arguments ' -- lang ' 
ou o usuário terá que digitar. 

Execução: 
        python 3 hello.py
        ou
        ./hello.py
"""
__version__ = " 0.1.3 "
__author__ = " Dara Aragao "
__license__ = "Unlicense"

import os 
import sys

arguments = {"lang": None,"count": 1}

for arg in sys.argv[1:]:
    #TODO tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Opcao invalida `{key}`")
        sys.exit()
    arguments[key] = value

current_language= arguments["lang"]
if current_language is None: 
    #TODO: Usar repetição
    if "LANG" in os.environ:
    
    current_language = os.getenv("LANG")
    else: 
    if current_language is None: 
        current_language = input("Qual a linguagem:?")
    
current_language = current_language[:5]

msg = { 
    "en_US": "Hello, World",
    "pt_BR": "Olá, mundo!",
    "es_SP": " Hola, Mundo!",       
}
       
print(
    msg[current_language] * int(arguments["count"])
)
