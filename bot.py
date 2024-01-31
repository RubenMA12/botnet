import os
def run():
    # Especifica el comando nc
    comando_nc = "nc -lvp 5555"

    # Ejecuta el comando utilizando os.system
    os.system(comando_nc)

  # Espera a que el proceso nc termine
    proceso_nc.wait()

    # El código después de esto no se ejecutará hasta que el proceso nc haya terminado
    print("El proceso nc ha finalizado.")
    
if __name__ == "__main__":
    run()
