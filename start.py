""" Script para iniciar tanto la aplicación principal 'app' como el modulo de detección de movimiento """
import subprocess
import os
scripts_paths = (os.getcwd()+"\\app.py", os.getcwd()+"\\modulos\\moduloDeteccion.py")

ps = [subprocess.Popen(["python", script]) for script in scripts_paths]
exit_codes = [p.wait() for p in ps]

if not any(exit_codes):
    print("Todos los procesos terminaron con éxito")
else:
    print("Algunos procesos terminaron de forma inesperada.")