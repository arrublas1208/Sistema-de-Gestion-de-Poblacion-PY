# main.py
from reportes import *

# Función para el submenú de reportes
def submenu_reportes():
    while True:
        print("\n--- Módulo de Reportes ---")
        print("1. Obtener todos los datos de población para un país en un rango de años")
        print("2. Listar los países con su información de código ISO y código ISO3")
        print("3. Datos de población para el indicador 'SP.POP.TOTL'")
        print("4. Obtener los datos de población de los últimos 10 años para todos los países")
        print("5. Total de población para un país en un año específico")
        print("6. Población total registrada antes del año 2000")
        print("7. Población total registrada después del año 2010")
        print("8. Porcentaje de crecimiento de la población de un país entre dos años")
        print("9. Población de un país en un año específico (si está disponible)")
        print("10. Obtener el año con la población más baja para un país")
        print("11. Número de registros de población por año")
        print("12. Países con un crecimiento poblacional mayor al 2% anual en los últimos 5 años")
        print("13. Listar los años en los que la población de un país superó un valor específico")
        print("14. Obtener la población total registrada para todos los países en un año específico")
        print("15. Obtener la población menos registrada para un país en los últimos 20 años")
        print("16. Promedio de población registrada por año para un país en un rango de años")
        print("17. Cantidad de años con datos de población disponibles para un país")
        print("18. Listar los países con datos de población disponibles para cada año entre 2000 y 2023")
        print("19. Población total de un país en un año específico")
        print("20. Años en los que la población de un país creció más de un valor específico en comparación con el año anterior")
        print("21. Población registrada de un país en cada década desde 1960")
        print("22. Población total registrada para todos los países en un año específico")
        print("23. Años en los que no hay datos de población disponibles para un país")
        print("24. Año con la población más alta registrada para un país")
        print("25. Años con datos de población disponibles para más de 50 países")
        print("26. Volver al menú principal")
        opcion_reporte = input("Seleccione una opción: ")

        if opcion_reporte == "1":
            pais = input("Ingrese el nombre del país: ")
            año_inicio = int(input("Ingrese el año de inicio: "))
            año_fin = int(input("Ingrese el año de fin: "))
            datos = obtener_poblacion_por_pais_y_año(pais, año_inicio, año_fin)
            print(f"Datos de población para {pais} desde {año_inicio} hasta {año_fin}:")
            for dato in datos:
                print(f"Año: {dato['ano']}, Población: {dato['valor']}")

        elif opcion_reporte == "2":
            print("Listado de países con códigos ISO e ISO3:")
            paises = listar_paises()
            for pais in paises:
                print(f"Nombre: {pais['nombre']}, Código ISO: {pais['codigo_iso']}, Código ISO3: {pais['codigo_iso3']}")

        elif opcion_reporte == "3":
            datos = obtener_poblacion_por_indicador('SP.POP.TOTL')
            print("Datos de población para el indicador 'SP.POP.TOTL':")
            for dato in datos:
                print(f"Año: {dato['ano']}, País: {dato['pais']}, Población: {dato['valor']}")

        elif opcion_reporte == "4":
            datos = obtener_poblacion_ultimos_10_años()
            print("Datos de población de los últimos 10 años para todos los países:")
            for dato in datos:
                print(f"Año: {dato['ano']}, País: {dato['pais']}, Población: {dato['valor']}")

        elif opcion_reporte == "5":
            pais = input("Ingrese el nombre del país: ")
            año = int(input("Ingrese el año: "))
            poblacion = obtener_poblacion_por_pais_y_año_especifico(pais, año)
            print(f"Población total de {pais} en {año}: {poblacion}")

        elif opcion_reporte == "6":
            poblacion = obtener_poblacion_antes_2000()
            print(f"Población total registrada antes del año 2000: {poblacion}")

        elif opcion_reporte == "7":
            poblacion = obtener_poblacion_despues_2010()
            print(f"Población total registrada después del año 2010: {poblacion}")

        elif opcion_reporte == "8":
            pais = input("Ingrese el nombre del país: ")
            año_inicio = int(input("Ingrese el año de inicio: "))
            año_fin = int(input("Ingrese el año de fin: "))
            crecimiento = calcular_crecimiento_poblacional(pais, año_inicio, año_fin)
            print(f"Crecimiento poblacional de {pais} entre {año_inicio} y {año_fin}: {crecimiento}")

        elif opcion_reporte == "9":
            pais = input("Ingrese el nombre del país: ")
            año = int(input("Ingrese el año: "))
            poblacion = obtener_poblacion_por_pais_y_año_especifico(pais, año)
            print(f"Población de {pais} en {año}: {poblacion}")

        elif opcion_reporte == "10":
            pais = input("Ingrese el nombre del país: ")
            año = obtener_ano_poblacion_mas_baja(pais)
            print(f"Año con la población más baja para {pais}: {año}")

        elif opcion_reporte == "11":
            conteo = contar_registros_por_año()
            print("Número de registros de población por año:")
            for año, cantidad in conteo.items():
                print(f"Año: {año}, Registros: {cantidad}")

        elif opcion_reporte == "12":
            paises = paises_crecimiento_mayor_2_porciento()
            print("Países con un crecimiento poblacional mayor al 2% anual en los últimos 5 años:")
            for pais in paises:
                print(pais)

        elif opcion_reporte == "13":
            pais = input("Ingrese el nombre del país: ")
            valor = float(input("Ingrese el valor de población: "))
            años = años_poblacion_mayor_que(pais, valor)
            print(f"Años en los que la población de {pais} superó {valor}: {años}")

        elif opcion_reporte == "14":
            año = int(input("Ingrese el año: "))
            poblacion = obtener_poblacion_total_por_año(año)
            print(f"Población total registrada para todos los países en {año}: {poblacion}")

        elif opcion_reporte == "15":
            pais = input("Ingrese el nombre del país: ")
            poblacion = obtener_poblacion_minima_ultimos_20_años(pais)
            print(f"Población menos registrada para {pais} en los últimos 20 años: {poblacion}")

        elif opcion_reporte == "16":
            pais = input("Ingrese el nombre del país: ")
            año_inicio = int(input("Ingrese el año de inicio: "))
            año_fin = int(input("Ingrese el año de fin: "))
            promedio = promedio_poblacion_por_pais_y_rango(pais, año_inicio, año_fin)
            print(f"Promedio de población registrada por año para {pais} entre {año_inicio} y {año_fin}: {promedio}")

        elif opcion_reporte == "17":
            pais = input("Ingrese el nombre del país: ")
            años = contar_años_datos_por_pais(pais)
            print(f"Cantidad de años con datos de población disponibles para {pais}: {años}")

        elif opcion_reporte == "18":
            paises_por_año = paises_con_datos_2000_2023()
            print("Países con datos de población disponibles para cada año entre 2000 y 2023:")
            for año, paises in paises_por_año.items():
                print(f"Año: {año}, Países: {paises}")

        elif opcion_reporte == "19":
            pais = input("Ingrese el nombre del país: ")
            año = int(input("Ingrese el año: "))
            poblacion = obtener_poblacion_por_pais_y_año_especifico(pais, año)
            print(f"Población total de {pais} en {año}: {poblacion}")

        elif opcion_reporte == "20":
            pais = input("Ingrese el nombre del país: ")
            valor = float(input("Ingrese el valor de crecimiento: "))
            años = años_crecimiento_mayor_que(pais, valor)
            print(f"Años en los que la población de {pais} creció más de {valor}: {años}")

        elif opcion_reporte == "21":
            pais = input("Ingrese el nombre del país: ")
            decadas = poblacion_por_decada(pais)
            print(f"Población registrada de {pais} en cada década desde 1960:")
            for decada, poblacion in decadas.items():
                print(f"Década: {decada}, Población: {poblacion}")

        elif opcion_reporte == "22":
            año = int(input("Ingrese el año: "))
            poblacion = obtener_poblacion_total_por_año(año)
            print(f"Población total registrada para todos los países en {año}: {poblacion}")

        elif opcion_reporte == "23":
            pais = input("Ingrese el nombre del país: ")
            años = años_sin_datos_por_pais(pais)
            print(f"Años en los que no hay datos de población disponibles para {pais}: {años}")

        elif opcion_reporte == "24":
            pais = input("Ingrese el nombre del país: ")
            año = obtener_ano_poblacion_mas_alta(pais)
            print(f"Año con la población más alta registrada para {pais}: {año}")

        elif opcion_reporte == "25":
            años = años_con_datos_mas_de_50_paises()
            print("Años con datos de población disponibles para más de 50 países:")
            for año in años:
                print(año)

        elif opcion_reporte == "26":
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Función principal del programa
def main():
    while True:
        print("\n--- Sistema de Gestión de Población ---")
        print("1. Obtener datos de población para un país y rango de años")
        print("2. Calcular crecimiento poblacional para un país")
        print("3. Listar todos los países")
        print("4. Agregar nuevo país")
        print("5. Registrar nuevo dato de población")
        print("6. Acceder al módulo de reportes")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:  # Validar país
                pais = input("Ingrese el nombre del país: ")
                if validar_pais(pais):
                    break
                else:
                    print(f"El país '{pais}' no existe en la base de datos. Intente nuevamente.")
            año_inicio = int(input("Ingrese el año de inicio: "))
            año_fin = int(input("Ingrese el año de fin: "))
            datos = obtener_poblacion_por_pais_y_año(pais, año_inicio, año_fin)
            if datos:
                for dato in datos:
                    print(f"Año: {dato['ano']}, Población: {dato['valor']} {dato['unidad']}")
            else:
                print("No se encontraron datos para el país y rango de años especificados.")

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
            paises = listar_paises()
            for pais in paises:
                print(f"Nombre: {pais['nombre']}, Código ISO: {pais['codigo_iso']}, Código ISO3: {pais['codigo_iso3']}")

        elif opcion == "4":
            agregar_nuevo_pais()

        elif opcion == "5":
            registrar_nuevo_dato_poblacion()

        elif opcion == "6":
            submenu_reportes()

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()