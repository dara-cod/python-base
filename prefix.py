"""Calculadora Prefix

Funcionamento:

[operação] [n1] [n2]

Operações: 
sum -> +
sub -> -
mul -> *
div -> /

Uso: 
$ prefix.py sum 5 2 
7

$ prefix.py mul 10 5
50 

$ prefix.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvador em `prefixcalc.log`
"""

__version__ = "0.1.0"

import sys
import os

from datetime import datetime

arguments = sys.argv[1:]

if not arguments:
    operation = input("operacao:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation,n1,n2]
elif len(arguments) != 3:
    print("Número de argumentos invalidos")
    print("ex: `sum 5 5` ") 
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul",'div')
if operation not in valid_operations:
    print(" Operação inválida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    #TODO: Repetição de while + exceptions
    if not num.replace (".", "").isdigit():
        print(f"Numero iválido {num}")
        sys.exit(1)
    if "." in num: 
        num = float(num)
    else: 
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

# TODO: USAR UM DICIONARIO DE FUNÇÕES
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER','anonymous')

with open (filepath, "a") as file_:
     file_.write(f"{timestamp} - {user} - {operation},{n1},{n2} = {result}\n")
    
print(f"O resultado é {result}")