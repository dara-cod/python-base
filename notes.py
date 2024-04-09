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
    
while True:
    
    if arguments [0] == "read":
        try: 
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual a tag?").strip().lower()
            
        # leitura das notas
        for line in open(filepath):
            tittle, tag, text = line.split("\t")
            if tag.lower() == arg_tag:
                print(f"title: {tittle}")
                print(f"text: {text}")
                print("-" * 30)
                print ()

    if arguments [0] == "new":
        try: 
            title = arguments[1]
        except IndexError:
            title = input("qual é o titulo?"),strip().tittle()
        
        text = [ 
            f"{title}\n",
            input("tag:").strip(),
            input("text:\n").strip(),
            "\n"   
        ]
        # \t - tsv 
        with open (filepath, "a") as file_:
            file_.write("\t".join(text))
            
    cont = input("Quer continuar {arguments[0]} notas? [N/y]").strip().lower()
    if cont != "y":
        break
 
    