import os
import sys

# EAFP = Easy to ASK Forgiveness than permission
# (É mais facil pedir perdão do que permissão)

try: 
    names = open("names.txt").readlines () #FileNotFoundError
except FileExistsError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: usar retry

else: 
    print("Sucesso!!!")
finally:
    print("Execute isso sempre!")

try: 
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)