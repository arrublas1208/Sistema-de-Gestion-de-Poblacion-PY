# reportes.py
import json
from collections import defaultdict

# Función para cargar datos desde un archivo JSON
def cargar_datos(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

# Función para guardar datos en un archivo JSON
def guardar_datos(ruta, datos):
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

# Cargar datos iniciales
poblacion = cargar_datos('poblacion.json')
paises = cargar_datos('paises.json')
indicadores = cargar_datos('indicadores.json')

# Función para validar si un país existe en la base de datos
def validar_pais(nombre_pais):
    return any(pais['nombre'] == nombre_pais for pais in paises)

# Función para agregar un nuevo país
def agregar_nuevo_pais():
    nombre = input("Ingrese el nombre del país: ")
    codigo_iso = input("Ingrese el código ISO del país: ")
    codigo_iso3 = input("Ingrese el código ISO3 del país: ")

    nuevo_pais = {
        "nombre": nombre,
        "codigo_iso": codigo_iso,
        "codigo_iso3": codigo_iso3
    }

    if validar_pais(nombre):
        print("El país ya existe en la base de datos.")
    else:
        paises.append(nuevo_pais)
        guardar_datos('paises.json', paises)
        print(f"País '{nombre}' agregado correctamente.")

# Función para registrar un nuevo dato de población
def registrar_nuevo_dato_poblacion():
    pais = input("Ingrese el nombre del país: ")
    if not validar_pais(pais):
        print(f"El país '{pais}' no existe en la base de datos.")
        return

    año = int(input("Ingrese el año del dato: "))
    indicador_id = input("Ingrese el ID del indicador (ej. SP.POP.TOTL): ")
    descripcion = input("Ingrese la descripción del indicador: ")
    valor = float(input("Ingrese el valor de la población: "))
    estado = input("Ingrese el estado de la observación (disponible/no disponible): ")
    unidad = input("Ingrese la unidad de medida (ej. personas): ")

    nuevo_dato = {
        "ano": año,
        "pais": pais,
        "codigo_iso3": next(pais['codigo_iso3'] for pais in paises if pais['nombre'] == pais),
        "indicador_id": indicador_id,
        "descripcion": descripcion,
        "valor": valor,
        "estado": estado,
        "unidad": unidad
    }

    if any(dato['pais'] == pais and dato['ano'] == año and dato['indicador_id'] == indicador_id for dato in poblacion):
        print("El dato ya existe en la base de datos.")
    else:
        poblacion.append(nuevo_dato)
        guardar_datos('poblacion.json', poblacion)
        print(f"Dato de población para '{pais}' en el año {año} registrado correctamente.")

# 1. Obtener todos los datos de población para un país desde 2000 hasta 2023
def obtener_poblacion_por_pais_y_año(pais, año_inicio=2000, año_fin=2023):
    return [dato for dato in poblacion if dato['pais'] == pais and año_inicio <= dato['ano'] <= año_fin]

# 2. Listar los países con su información de código ISO y código ISO3
def listar_paises():
    return paises

# 3. Datos de población para el indicador 'SP.POP.TOTL'
def obtener_poblacion_por_indicador(indicador_id):
    return [dato for dato in poblacion if dato['indicador_id'] == indicador_id]

# 4. Obtener los datos de población de los últimos 10 años para todos los países
def obtener_poblacion_ultimos_10_años():
    año_actual = 2023  # Puedes cambiarlo dinámicamente
    return [dato for dato in poblacion if año_actual - 10 <= dato['ano'] <= año_actual]

# 5. Total de población para un país en un año específico
def obtener_poblacion_por_pais_y_año_especifico(pais, año):
    for dato in poblacion:
        if dato['pais'] == pais and dato['ano'] == año:
            return dato['valor']
    return "Dato no disponible"

# 6. Población total registrada antes del año 2000
def obtener_poblacion_antes_2000():
    return sum(dato['valor'] for dato in poblacion if dato['ano'] < 2000)

# 7. Población total registrada después del año 2010
def obtener_poblacion_despues_2010():
    return sum(dato['valor'] for dato in poblacion if dato['ano'] > 2010)

# 8. Porcentaje de crecimiento de la población de un país entre dos años
def calcular_crecimiento_poblacional(pais, año_inicio, año_fin):
    datos = [dato for dato in poblacion if dato['pais'] == pais and año_inicio <= dato['ano'] <= año_fin]
    if len(datos) < 2:
        return "No hay suficientes datos para calcular el crecimiento."
    valor_inicio = datos[0]['valor']
    valor_fin = datos[-1]['valor']
    crecimiento = ((valor_fin - valor_inicio) / valor_inicio) * 100
    return f"{crecimiento:.2f}%"

# 10. Obtener el año con la población más baja para un país
def obtener_ano_poblacion_mas_baja(pais):
    datos_pais = [dato for dato in poblacion if dato['pais'] == pais]
    if not datos_pais:
        return "No hay datos disponibles para este país."
    return min(datos_pais, key=lambda x: x['valor'])['ano']

# 11. Número de registros de población por año
def contar_registros_por_año():
    conteo = defaultdict(int)
    for dato in poblacion:
        conteo[dato['ano']] += 1
    return dict(conteo)

# 12. Países con un crecimiento poblacional mayor al 2% anual en los últimos 5 años
def paises_crecimiento_mayor_2_porciento():
    año_actual = 2023
    resultados = []
    for pais in paises:
        datos = [dato for dato in poblacion if dato['pais'] == pais['nombre'] and año_actual - 5 <= dato['ano'] <= año_actual]
        if len(datos) >= 2:
            crecimiento = ((datos[-1]['valor'] - datos[0]['valor']) / datos[0]['valor']) * 100
            if crecimiento > 2:
                resultados.append(pais['nombre'])
    return resultados

# 13. Listar los años en los que la población de un país superó un valor específico
def años_poblacion_mayor_que(pais, valor):
    return [dato['ano'] for dato in poblacion if dato['pais'] == pais and dato['valor'] > valor]

# 14. Obtener la población total registrada para todos los países en un año específico
def obtener_poblacion_total_por_año(año):
    return sum(dato['valor'] for dato in poblacion if dato['ano'] == año)

# 15. Obtener la población menos registrada para un país en los últimos 20 años
def obtener_poblacion_minima_ultimos_20_años(pais):
    año_actual = 2023
    datos = [dato for dato in poblacion if dato['pais'] == pais and año_actual - 20 <= dato['ano'] <= año_actual]
    return min(datos, key=lambda x: x['valor'])['valor'] if datos else "No hay datos disponibles"

# 16. Promedio de población registrada por año para un país en un rango de años
def promedio_poblacion_por_pais_y_rango(pais, año_inicio, año_fin):
    datos = [dato['valor'] for dato in poblacion if dato['pais'] == pais and año_inicio <= dato['ano'] <= año_fin]
    return sum(datos) / len(datos) if datos else "No hay datos disponibles"

# 17. Cantidad de años con datos de población disponibles para un país
def contar_años_datos_por_pais(pais):
    return len(set(dato['ano'] for dato in poblacion if dato['pais'] == pais))

# 18. Listar los países con datos de población disponibles para cada año entre 2000 y 2023
def paises_con_datos_2000_2023():
    años = range(2000, 2024)
    resultados = defaultdict(list)
    for dato in poblacion:
        if dato['ano'] in años:
            resultados[dato['ano']].append(dato['pais'])
    return dict(resultados)

# 20. Años en los que la población de un país creció más de un valor específico en comparación con el año anterior
def años_crecimiento_mayor_que(pais, valor):
    datos = [dato for dato in poblacion if dato['pais'] == pais]
    años = []
    for i in range(1, len(datos)):
        if datos[i]['valor'] - datos[i-1]['valor'] > valor:
            años.append(datos[i]['ano'])
    return años

# 21. Población registrada de un país en cada década desde 1960
def poblacion_por_decada(pais):
    decadas = defaultdict(int)
    for dato in poblacion:
        if dato['pais'] == pais:
            decada = (dato['ano'] // 10) * 10
            decadas[decada] += dato['valor']
    return dict(decadas)

# 23. Años en los que no hay datos de población disponibles para un país
def años_sin_datos_por_pais(pais):
    años_con_datos = set(dato['ano'] for dato in poblacion if dato['pais'] == pais)
    todos_los_años = set(range(2000, 2024))  # Ajusta el rango según tus datos
    return todos_los_años - años_con_datos

# 24. Año con la población más alta registrada para un país
def obtener_ano_poblacion_mas_alta(pais):
    datos_pais = [dato for dato in poblacion if dato['pais'] == pais]
    if not datos_pais:
        return "No hay datos disponibles para este país."
    return max(datos_pais, key=lambda x: x['valor'])['ano']

# 25. Años con datos de población disponibles para más de 50 países
def años_con_datos_mas_de_50_paises():
    conteo = defaultdict(int)
    for dato in poblacion:
        conteo[dato['ano']] += 1
    return [año for año, cantidad in conteo.items() if cantidad > 50]