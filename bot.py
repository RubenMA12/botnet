import subprocess

def run():
    # Especifica el comando nc
    comando_nc = "nc -lvp 5555"

    # Ejecuta el comando utilizando subprocess
    proceso_nc = subprocess.Popen(comando_nc, shell=True)

    # Espera a que el proceso nc termine
    proceso_nc.wait()

    # El código después de esto no se ejecutará hasta que el proceso nc haya terminado
    print("El proceso nc ha finalizado.")

if __name__ == "__main__":
    run()
