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
    1. Administrar usuarios
    2. Administrar archivos
    3. Salir
    """)

    opcion = input("Opción: ")

    if opcion == "1":
        while True:
            print("""
            Seleccione una opción:
            1. Agregar usuario
            2. Eliminar usuario
            3. Salir
            """)
            opcion = input("Opción: ")
            if opcion == "1" :
                agregar_usuario()  
            elif opcion == "2" :
                eliminar_usuario()
            elif opcion == "3" :
                break
    
    elif opcion == "2" :
        while True:
            print ("""
            Seleccione una opción:
            1. Agregar archivo
            2. Eliminar archivo
            3. Salir
            """)
            opcion = input ("Opción: ")
            if opcion == "1" :
                agregar_archivo()
            elif opcion == "2" :
                eliminar_archivo()
            elif opcion == "3" :
                break
    elif opcion == "3" :
        break
    else:
        print("Opción no válida.")
