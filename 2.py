import subprocess

def check_ubuntu_updates():
    # Ejecutar el comando 'apt update' para actualizar los repositorios
    subprocess.run(['sudo', 'apt', 'update'])

    # Ejecutar el comando 'apt list --upgradable' para obtener las actualizaciones disponibles
    result = subprocess.run(['apt', 'list', '--upgradable'], capture_output=True, text=True)
    output = result.stdout.strip()

    if output:
        print("¡Existen actualizaciones disponibles!")
        # Generar el prompt para que el usuario decida si instalar o no las actualizaciones
        choice = input("¿Desea instalar las actualizaciones? (y/n): ")
        if choice.lower() == 'y':
            # Ejecutar el comando 'sudo apt upgrade' para instalar las actualizaciones
            subprocess.run(['sudo', 'apt', 'upgrade'])
            print("Las actualizaciones se han instalado correctamente.")
        else:
            print("No se han instalado las actualizaciones.")
    else:
        print("No hay actualizaciones disponibles.")

# Llamar a la función para verificar las actualizaciones en Ubuntu
check_ubuntu_updates()
