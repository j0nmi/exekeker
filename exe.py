import psutil
import datetime
import os
from colorama import init, Fore, Style

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_executables():
    executables = []
    for proc in psutil.process_iter(['name', 'exe', 'create_time']):
        try:
            # Verificar si el proceso es un archivo ejecutable .exe y no es svchost.exe
            if proc.info['name'].lower().endswith('.exe') and proc.info['exe'] != r'C:\Windows\System32\svchost.exe':
                executables.append(proc.info)
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            pass
    return executables

if __name__ == '__main__':
    init()  # Inicializar colorama para imprimir colores en la consola
    clear_console()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "\t    ___  _  _____     / /_____  / /_____  _____")
    print(Fore.LIGHTBLUE_EX + "\t   / _ \| |/_/ _ \   / //_/ _ \/ //_/ _ \/ ___/")
    print(Fore.LIGHTBLUE_EX + "\t _/  __/>  </  __/  / ,< /  __/ ,< /  __/ /    ")
    print(Fore.LIGHTBLUE_EX + "\t(_)___/_/|_|\___/  /_/|_|\___/_/|_|\___/_/  By: j0nmi")
    print(Style.RESET_ALL)
    print()
    input("\tPresiona ENTER para iniciar el script.")
    
    # Guardar ejecutables en el archivo historial_exes.txt
    with open('historial_exes.txt', 'w') as file:
        file.write("Archivos ejecutados desde el inicio del sistema:\n")
        for exe in get_executables():
            create_time = datetime.datetime.fromtimestamp(exe['create_time']).strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"{create_time} | {exe['exe']}\n")
    
    print("\t¡Listo! Los ejecutables se han guardado en el archivo historial_exes.txt")
    print(Style.RESET_ALL)
