from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()] # Preparando la ruta para hacer la inyeccion

dependencia = {
    
}

def load(p):    
    paquete = __import__(str(p).replace("/", ".")) # donde vammos a importar los paquetes
    paquete.init() # trae todos los metodos init

map(load, paths)