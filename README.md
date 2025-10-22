# Sistema de Gestión de Población (Proyecto Python)

Aplicación de consola para gestionar y consultar datos de población por país, utilizando archivos JSON locales como fuente de datos. Permite agregar países, registrar nuevos datos de población y generar múltiples reportes predefinidos.

## Estructura del proyecto

```
Proyecto_Python_ArrublasJuanJose/
├── main.py            # Punto de entrada (menú principal y submenú de reportes)
├── reportes.py        # Lógica de negocio y funciones de consulta/gestión
├── poblacion.json     # Datos de población por país y año
├── paises.json        # Catálogo de países con códigos ISO e ISO3
└── indicadores.json   # Catálogo de indicadores (ej. SP.POP.TOTL)
```

## Requisitos

- Python 3.8 o superior.
- No se requieren dependencias externas; solo se usa la librería estándar (`json`, `collections`).

## Ejecución

1. Asegúrate de que los archivos `poblacion.json`, `paises.json` e `indicadores.json` estén en la misma carpeta que `main.py`.
2. En una terminal, posiciona el directorio de trabajo en la carpeta del proyecto.
3. Ejecuta el programa:

```
python main.py
```

Se abrirá el menú principal interactivo en consola.

## Menú principal

- `1` Obtener datos de población para un país y rango de años.
- `2` Calcular crecimiento poblacional para un país.
- `3` Listar todos los países.
- `4` Agregar nuevo país.
- `5` Registrar nuevo dato de población.
- `6` Acceder al módulo de reportes.
- `7` Salir.

## Módulo de reportes

Dentro del submenú de reportes encontrarás las siguientes opciones:

1. Obtener todos los datos de población para un país en un rango de años.
2. Listar los países con su información de código ISO y código ISO3.
3. Datos de población para el indicador `SP.POP.TOTL`.
4. Obtener los datos de población de los últimos 10 años para todos los países.
5. Total de población para un país en un año específico.
6. Población total registrada antes del año 2000.
7. Población total registrada después del año 2010.
8. Porcentaje de crecimiento de la población de un país entre dos años.
9. Población de un país en un año específico (si está disponible).
10. Obtener el año con la población más baja para un país.
11. Número de registros de población por año.
12. Países con un crecimiento poblacional mayor al 2% anual en los últimos 5 años.
13. Listar los años en los que la población de un país superó un valor específico.
14. Obtener la población total registrada para todos los países en un año específico.
15. Obtener la población menos registrada para un país en los últimos 20 años.
16. Promedio de población registrada por año para un país en un rango de años.
17. Cantidad de años con datos de población disponibles para un país.
18. Listar los países con datos de población disponibles para cada año entre 2000 y 2023.
19. Población total de un país en un año específico.
20. Años en los que la población de un país creció más de un valor específico en comparación con el año anterior.
21. Población registrada de un país en cada década desde 1960.
22. Población total registrada para todos los países en un año específico.
23. Años en los que no hay datos de población disponibles para un país.
24. Año con la población más alta registrada para un país.
25. Años con datos de población disponibles para más de 50 países.

## Datos y formatos JSON

- `poblacion.json` (ejemplo de entrada):

```json
{
  "ano": 2023,
  "pais": "India",
  "codigo_iso3": "IND",
  "indicador_id": "SP.POP.TOTL",
  "descripcion": "Total de población",
  "valor": 1380000000,
  "estado": "disponible",
  "unidad": "personas"
}
```

- `paises.json` (ejemplo):

```json
{
  "nombre": "India",
  "codigo_iso": "IN",
  "codigo_iso3": "IND"
}
```

- `indicadores.json` (ejemplo):

```json
{
  "id_indicador": "SP.POP.TOTL",
  "descripcion": "Total de población"
}
```

## Cómo agregar datos

- Agregar país: desde el menú principal, opción `4`.
  - Se solicitan `nombre`, `codigo_iso`, `codigo_iso3` y se valida que no exista previamente.
- Registrar dato de población: menú principal, opción `5`.
  - Requiere que el país exista. Se solicitan `ano`, `indicador_id`, `descripcion`, `valor`, `estado`, `unidad`.
  - Se evita duplicar registros con la combinación (`pais`, `ano`, `indicador_id`).

## Notas y consideraciones

- Los nombres de países deben coincidir exactamente con los presentes en `paises.json` (la validación es sensible al texto exacto).
- Algunos cálculos usan el rango fijo 2000–2023 y el año actual configurado como 2023 en `reportes.py`. Se puede ajustar según la necesidad.
- Los reportes agregan/suman y comparan `valor` directamente; la `unidad` no se normaliza, asegúrate de usar la misma unidad para coherencia.
- Todos los archivos JSON deben permanecer en la raíz del proyecto junto a `main.py` y `reportes.py`.

## Desarrollo

- Punto de entrada: `main.py` contiene el menú y orquesta las llamadas a funciones.
- Lógica: `reportes.py` agrupa funciones de consulta y gestión de datos.
- Para nuevas métricas o reportes, añade funciones en `reportes.py` y nuevas opciones en el menú de `main.py`.

---

Autor: Arrublas Juan José