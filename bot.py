import os
def run():
    # Especifica el comando nc
    comando_nc = "nc -lvp 5555"

    # Ejecuta el comando utilizando os.system
    os.system(comando_nc)
    
if __name__ == "__main__":
    run()
