import subprocess

def check_rhel_updates():
    # Ejecutar el comando para verificar actualizaciones disponibles
    result = subprocess.run(['sudo', 'dnf', 'check-update'], capture_output=True, text=True)

    if result.returncode == 0:
        updates_available = result.stdout.strip().split('\n')
        if updates_available:
            print("Hay actualizaciones disponibles:")
            for update in updates_available:
                print(update)
            choice = input("¿Desea instalar las actualizaciones? (S/N): ")
            if choice.lower() == 's':
                # Ejecutar el comando para instalar las actualizaciones
                install_updates()
            else:
                print("No se instalarán las actualizaciones.")
        else:
            print("No hay actualizaciones disponibles.")
    else:
        print("Ocurrió un error al verificar las actualizaciones.")

def install_updates():
    # Ejecutar el comando para instalar las actualizaciones
    result = subprocess.run(['sudo', 'dnf', 'upgrade', '-y'], capture_output=True, text=True)

    if result.returncode == 0:
        print("Las actualizaciones se han instalado correctamente.")
    else:
        print("Ocurrió un error al instalar las actualizaciones.")

# Llamar a la función para verificar las actualizaciones de RHEL
check_rhel_updates()
