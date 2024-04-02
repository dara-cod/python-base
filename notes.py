"""Bloco de notas 

$ note.py new "Minha nota"
tag: tech
text: 
Anotacao geral sobre carreira de TI

$ notes.py read --tag=tech
...
...
"""

__version__ = "0.1.0"

import os
import sys

cmds = ("read, new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments: 
    print("Utilização inválida")
    print(f"eh necessario especificar o subcomando {cmds}")
    sys.exit(1)


if arguments [0] not in cmds:
    print(f"Invalid command {arguments[0]}")
    
if arguments [0] == "read":
    # leitura das notas
    pass

if arguments [0] == "new":
    titulo = arguments [1] # TODO: tratar exception
    text = [ 
        f"{titulo}\n",
        input("tag:").strip(),
        input("text:\n").strip(),
        "\n"   
    ]
    # \t - tsv 
    with open (filepath, "a") as file_:
        file_.write("\t".join(text))
 
    