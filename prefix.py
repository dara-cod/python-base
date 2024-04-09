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
import logging

from datetime import datetime

while True:
    arguments = sys.argv[1:]
    
    # Validacao
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

    try: 
        n1, n2 = validated_nums
    except ValueError as e:
        print(str(e))
        sys.exit(1)
        
    # TODO: USAR UM DICIONARIO DE FUNÇÕES
    if operation == "sum":
        result = n1 + n2
    elif operation == "sub":
        result = n1 - n2
    elif operation == "mul":
        result = n1 * n2
    elif operation == "div":
        result = n1 / n2

    path = "/"
    filepath = os.path.join(path, "prefixcalc.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv('USER','anonymous')

    print(f"O resultado é {result}")

        log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
    log = logging.Logger("Dara", log_level)
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    fmt = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s '
        'l:%(lineno)d f:%(filename)s: %(message)s'
    )
    ch.setFormatter(fmt)
    log.addHandler(ch)

    try: 
        with open(filepath, "a") as file_:
            file_.write(f"{timestamp} - {user} - {operation},{n1},{n2} = {result}\n")
    except: PermissionError as e:
        #TODO logging - VERIFICAR DEPOIS
        
        print(str(e))
        sys.exit(1)