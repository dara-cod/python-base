import sys
import logging
log = logging.Logger("alerta")

# TODO: Usar funções para ler input

info = { 
    "temperatura": None,
    "umidade": None
}
keys = info.keys()

for key in keys:
    try: 
        info[key] = float(input(f"Qual a {key}?").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)
        
temp = info ["temperatura"]
umidade = info["umidade"]

if temp > 45: 
    print ("ALETRA!!! Perigo calor extermo")
elif temp * 3 >= umidade:
    print("ALERTA!!! Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("Normal")
elif temp >= 0 and temp <= 10:
    print("Frio")
elif temp < 0:
    print("ALERTA!! Frio Extremo.")