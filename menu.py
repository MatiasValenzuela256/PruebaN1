usuarios = {}
archivos = {}

def agregar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    if nombre in usuarios:
        print("Usuario existente, intente de nuevo")
    else:
        usuarios[nombre] = {}
        print(f"Usuario '{nombre}' agregado.")

def eliminar_usuario():
    nombre = input("Ingrese el nombre del usuario a eliminar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print(f"Usuario '{nombre}' eliminado.")
    else:
        print("Usuario no encontrado.")

def agregar_archivo():
    nombre = input("Ingrese el nombre del archivo: ")
    if nombre in archivos:
        print("Archivo existente, intente de nuevo")
    else:
        archivos[nombre] = {}
        print(f"Archivo '{nombre}' agregado.")

def eliminar_archivo():
    nombre = input("Ingrese el nombre del archivo a eliminar: ")
    if nombre in archivos:
        del archivos[nombre]
        print(f"Archivo '{nombre}' eliminado.")
    else:
        print("Archivo no encontrado.")

while True:
    print("""
    Seleccione una opción:
    1. Agregar usuario
    2. Eliminar usuario
    3. Agregar archivo
    4. Eliminar archivo
    5. Salir
    """)

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_usuario()
    elif opcion == "2":
        eliminar_usuario()
    elif opcion == "3":
        agregar_archivo()
    elif opcion == "4":
        eliminar_archivo()
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")
