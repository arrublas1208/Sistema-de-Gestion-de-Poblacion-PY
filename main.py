import json

# Función para cargar datos desde un archivo JSON
def cargar_datos(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

# Función para guardar datos en un archivo JSON
def guardar_datos(ruta, datos):
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

# Función para obtener datos de población por país y año
def obtener_poblacion_por_pais_y_año(pais, año_inicio, año_fin):
    datos_poblacion = cargar_datos('poblacion.json')
    return [dato for dato in datos_poblacion if dato['pais'] == pais and año_inicio <= dato['ano'] <= año_fin]

# Función para calcular el crecimiento poblacional porcentual
def calcular_crecimiento_poblacional(pais, año_inicio, año_fin):
    datos = obtener_poblacion_por_pais_y_año(pais, año_inicio, año_fin)
    if len(datos) < 2:
        return "No hay suficientes datos para calcular el crecimiento."
    crecimiento = []
    for i in range(1, len(datos)):
        valor_anterior = datos[i-1]['valor']
        valor_actual = datos[i]['valor']
        porcentaje = ((valor_actual - valor_anterior) / valor_anterior) * 100
        crecimiento.append({'ano': datos[i]['ano'], 'crecimiento': porcentaje})
    return crecimiento

# Función para listar países con su información
def listar_paises():
    paises = cargar_datos('paises.json')
    for pais in paises:
        print(f"Nombre: {pais['nombre']}, Código ISO: {pais['codigo_iso']}, Código ISO3: {pais['codigo_iso3']}")

def agregar_nuevo_pais():
    nombre = input("Ingrese el nombre del país: ")
    codigo_iso = input("Ingrese el código ISO del país: ")
    codigo_iso3 = input("Ingrese el código ISO3 del país: ")

    nuevo_pais = {
        "nombre": nombre,
        "codigo_iso": codigo_iso,
        "codigo_iso3": codigo_iso3
    }

    # Cargar los países existentes
    paises = cargar_datos('paises.json')
    
    # Verificar si el país ya existe
    if any(pais['nombre'] == nombre for pais in paises):
        print("El país ya existe en la base de datos.")
    else:
        # Agregar el nuevo país
        paises.append(nuevo_pais)
        guardar_datos('paises.json', paises)
        print(f"País '{nombre}' agregado correctamente.")   
def registrar_nuevo_dato_poblacion():
    pais = input("Ingrese el nombre del país: ")
    año = int(input("Ingrese el año del dato: "))
    indicador_id = input("Ingrese el ID del indicador (ej. SP.POP.TOTL): ")
    descripcion = input("Ingrese la descripción del indicador: ")
    valor = float(input("Ingrese el valor de la población: "))
    estado = input("Ingrese el estado de la observación (disponible/no disponible): ")
    unidad = input("Ingrese la unidad de medida (ej. personas): ")

    nuevo_dato = {
        "ano": año,
        "pais": pais,
        "codigo_iso3": "",  # Puedes agregar lógica para obtener el código ISO3 automáticamente
        "indicador_id": indicador_id,
        "descripcion": descripcion,
        "valor": valor,
        "estado": estado,
        "unidad": unidad
    }

    # Cargar los datos de población existentes
    datos_poblacion = cargar_datos('poblacion.json')
    
    # Verificar si el dato ya existe
    if any(dato['pais'] == pais and dato['ano'] == año and dato['indicador_id'] == indicador_id for dato in datos_poblacion):
        print("El dato ya existe en la base de datos.")
    else:
        # Agregar el nuevo dato
        datos_poblacion.append(nuevo_dato)
        guardar_datos('poblacion.json', datos_poblacion)
        print(f"Dato de población para '{pais}' en el año {año} registrado correctamente.")    
                 

# Función principal del programa
def main():
    while True:
        print("\n--- Sistema de Gestión de Población ---")
        print("1. Obtener datos de población para un país y rango de años")
        print("2. Calcular crecimiento poblacional para un país")
        print("3. Listar todos los países")
        print("4. Agregar nuevo país")
        print("5. Registrar nuevo dato de población")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pais = input("Ingrese el nombre del país: ")
            año_inicio = int(input("Ingrese el año de inicio: "))
            año_fin = int(input("Ingrese el año de fin: "))
            datos = obtener_poblacion_por_pais_y_año(pais, año_inicio, año_fin)
            for dato in datos:
                print(f"Año: {dato['ano']}, Población: {dato['valor']} {dato['unidad']}")

        elif opcion == "2":
            pais = input("Ingrese el nombre del país: ")
            año_inicio = int(input("Ingrese el año de inicio: "))
            año_fin = int(input("Ingrese el año de fin: "))
            crecimiento = calcular_crecimiento_poblacional(pais, año_inicio, año_fin)
            if isinstance(crecimiento, list):
                for c in crecimiento:
                    print(f"Año: {c['ano']}, Crecimiento: {c['crecimiento']:.2f}%")
            else:
                print(crecimiento)

        elif opcion == "3":
            listar_paises()

        elif opcion == "4":
            agregar_nuevo_pais()

        elif opcion == "5":
            registrar_nuevo_dato_poblacion()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()