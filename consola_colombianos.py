"""
Ejercicio nivel 3: Colombianos en Wikipedia.
Interfaz basada en consola para la interaccion con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos
@author: Cupi2
"""
import csv
import os

def ejecutar_cargar_datos() -> dict:
    """Solicita al usuario que ingrese el nombre del archivo CSV con los datos de los jugadores.
    Retorno: dict
        El diccionario de ocupaciones con la información de los colombianos en el archivo
    """
    colombianos = {}

    archivo = input("Por favor ingrese el nombre del archivo CSV con los datos de los colombianos: ")
    
    try:
        with open(archivo, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                nombre = row['nombre']
                genero = row['genero']
                anio_nacimiento = int(row['anio_nacimiento'])
                anio_muerte = int(row['anio_muerte'])
                ocupacion = row['ocupacion']
                ciudadania = row['ciudadania']
                numero_lectores = int(row['numero_lectores'])

                colombianos[nombre] = {
                    'genero': genero,
                    'anio_nacimiento': anio_nacimiento,
                    'anio_muerte': anio_muerte,
                    'ocupacion': ocupacion,
                    'ciudadania': ciudadania,
                    'numero_lectores': numero_lectores
                }

        print("Se cargaron los siguientes ocupaciones a partir del archivo.")
        for nombre in colombianos:
            print(nombre)
    
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al cargar los datos: {str(e)}")

    return colombianos



def ejecutar_mayor_lectores(colombianos: dict) -> None:
    """Ejecuta la opción de encontrar el colombiano con el mayor número de lectores.
    El mensaje que se le muestra al usuario tiene el siguiente formato:
        'El colombiano con el mayor número de lectores en Wikipedia es (nombre del colombiano)'
    """

    if not colombianos:
        print("No se han cargado datos de colombianos. Cargue un archivo primero.")
    else:
        # Definir una función para obtener el colombiano con el mayor número de lectores.
        def colombiano_con_mayor_lectores(colombianos):
            max_lectores = -1
            colombiano_mayor_lectores = None

            for nombre, datos in colombianos.items():
                lectores = datos.get("numero_lectores", 0)
                if lectores > max_lectores:
                    max_lectores = lectores
                    colombiano_mayor_lectores = nombre

            return colombiano_mayor_lectores

        # Llamada a la función y obtención del resultado
        colombiano_mayor_lectores = colombiano_con_mayor_lectores(colombianos)

        if colombiano_mayor_lectores:
            print(f"El colombiano con el mayor número de lectores en Wikipedia es {colombiano_mayor_lectores}")
        else:
            print("No se encontró ningún colombiano en los datos.")

def ejecutar_hay_3_colombianos(colombianos: dict) -> None:
    """Ejecuta la opción que busca si hay 3 colombianos que superen un número de lectores
       dada una ocupación, un género y un número de lectores a superar.
    La consola debe mostrar un mensaje con el siguiente mensaje según el caso:
        'Sí existen 3 colombianos de este género y ocupación que superen este tope.'
        'No existen 3 colombianos de este género y ocupación que superen este tope.'
    """
    if not colombianos:
        print("No se han cargado datos de colombianos. Cargue un archivo primero.")
        return

    ocupacion = input("Ingrese la ocupación: ")
    genero = input("Ingrese el género (Male o Female): ")
    lectores_a_superar = int(input("Ingrese el número de lectores a superar: "))

    # Filtrar colombianos que coincidan con la ocupación y género
    colombianos_filtrados = {
        nombre: datos for nombre, datos in colombianos.items()
        if datos['ocupacion'] == ocupacion and datos['genero'] == genero
    }

    # Contar cuántos colombianos superan el número de lectores especificado
    num_colombianos_superan = sum(1 for datos in colombianos_filtrados.values() if datos['numero_lectores'] > lectores_a_superar)

    if num_colombianos_superan >= 3:
        print(f'Sí existen {num_colombianos_superan} colombianos de género {genero} y ocupación {ocupacion} que superan {lectores_a_superar} lectores.')
    else:
        print(f'No existen 3 colombianos de género {genero} y ocupación {ocupacion} que superen {lectores_a_superar} lectores.')


def ejecutar_promedio_lectores(colombianos: dict) -> None:
    """Ejecuta la opción de calcular el promedio de lectores de las personas de una ocupación específica. 
    El mensaje que se le muestra al usuario tiene el siguiente formato:
        'El número de lectores promedio de los colombianos con ocupación (ocupación) es (número de lectores promedio).'
    """

    if not colombianos:
        print("No se han cargado datos de colombianos. Cargue un archivo primero.")
        return

    ocupacion = input("Ingrese la ocupación para calcular el promedio de lectores: ")

    # Filtrar colombianos que tienen la ocupación especificada
    colombianos_filtrados = {
        nombre: datos for nombre, datos in colombianos.items()
        if datos['ocupacion'] == ocupacion
    }

    if not colombianos_filtrados:
        print(f"No se encontraron colombianos con la ocupación '{ocupacion}'.")
        return

    # Calcular el promedio de lectores
    total_lectores = sum(datos['numero_lectores'] for datos in colombianos_filtrados.values())
    numero_colombianos = len(colombianos_filtrados)

    promedio_lectores = total_lectores / numero_colombianos

    print(f'El número de lectores promedio de los colombianos con ocupación "{ocupacion}" es {promedio_lectores:.2f}.')


def ejecutar_mayor_rating(colombianos: dict) -> None:
    """Ejecuta la opción de encontrar la ocupación con mayor número de lectores promedio.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'La ocupación con mayor número de lectores promedio es (ocupación).'
    """

    if not colombianos:
        print("No se han cargado datos de colombianos. Cargue un archivo primero.")
        return

    ocupaciones_promedio_lectores = {}  # Diccionario para almacenar el promedio de lectores por ocupación

    # Calcular el promedio de lectores por ocupación
    for nombre, datos in colombianos.items():
        ocupacion = datos['ocupacion']
        numero_lectores = datos['numero_lectores']

        if ocupacion in ocupaciones_promedio_lectores:
            ocupaciones_promedio_lectores[ocupacion].append(numero_lectores)
        else:
            ocupaciones_promedio_lectores[ocupacion] = [numero_lectores]

    # Calcular el promedio de lectores para cada ocupación
    for ocupacion, lectores in ocupaciones_promedio_lectores.items():
        promedio_lectores = sum(lectores) / len(lectores)
        ocupaciones_promedio_lectores[ocupacion] = promedio_lectores

    # Encontrar la ocupación con el mayor promedio de lectores
    ocupacion_mayor_promedio = max(ocupaciones_promedio_lectores, key=ocupaciones_promedio_lectores.get)
    mayor_promedio = ocupaciones_promedio_lectores[ocupacion_mayor_promedio]

    print(f'La ocupación con el mayor número de lectores promedio es "{ocupacion_mayor_promedio}" con un promedio de {mayor_promedio:.2f} lectores.')


def ejecutar_colombianos_rango(colombianos: dict) -> None:
    """Ejecuta la opción que consulta colombianos con una ocupación específica que hayan nacido en un rango de años.
    Se debe mostrar al usuario solo los nombres de los colombianos que cumplen con la condición.
    """

    if not colombianos:
        print("No se han cargado datos de colombianos. Cargue un archivo primero.")
        return

    ocupacion = input("Ingrese la ocupación para filtrar: ")
    anio_inicio = int(input("Ingrese el año de inicio del rango: "))
    anio_fin = int(input("Ingrese el año de fin del rango: "))

    colombianos_filtrados = {}

    # Filtrar los colombianos que tienen la ocupación especificada y nacieron en el rango de años
    for nombre, datos in colombianos.items():
        if datos['ocupacion'] == ocupacion and anio_inicio <= datos['anio_nacimiento'] <= anio_fin:
            colombianos_filtrados[nombre] = datos

    if colombianos_filtrados:
        print(f'Colombianos con ocupación "{ocupacion}" nacidos entre {anio_inicio} y {anio_fin}:')
        for nombre in colombianos_filtrados:
            print(nombre)
    else:
        print(f"No se encontraron colombianos con ocupación '{ocupacion}' nacidos entre {anio_inicio} y {anio_fin}.")


def ejecutar_nacionalidades(colombianos: dict) -> None:
    """Ejecuta la opción que cuenta cuantas personas hay de cada nacionalidad.
    Se debe mostrar al usuario un mensaje que luzca así:
        '(nacionalidad) --> (número de personas con esa nacionalidad)'
    Ejemplo:
        Colombia - Peru --> 2
        Colombia - Mexico --> 7
    """

    if not colombianos:
        print("No se han cargado datos de colombianos. Cargue un archivo primero.")
        return

    nacionalidades = {}

    # Contar cuántas personas hay de cada nacionalidad
    for nombre, datos in colombianos.items():
        nacionalidad = datos['ciudadania']

        if nacionalidad in nacionalidades:
            nacionalidades[nacionalidad] += 1
        else:
            nacionalidades[nacionalidad] = 1

    print("Número de personas por nacionalidad:")
    for nacionalidad, cantidad in nacionalidades.items():
        print(f"{nacionalidad} --> {cantidad}")


def ejecutar_calcular_edad(colombianos: dict) -> None:
    """Ejecuta la opción de calcular la edad de cada persona.
    Se debe mostrar al usuario el diccionario de colombianos con la edad incluida.
    """

    if not colombianos:
        print("No se han cargado datos de colombianos. Cargue un archivo primero.")
        return

    # Calcular la edad de cada persona y agregarla al diccionario de colombianos
    for nombre, datos in colombianos.items():
        anio_nacimiento = datos['anio_nacimiento']
        anio_muerte = datos['anio_muerte']
        edad = anio_muerte - anio_nacimiento if anio_muerte != 0 else 2023 - anio_nacimiento
        datos['edad'] = edad

    # Mostrar el diccionario de colombianos con la edad calculada
    print("Diccionario de colombianos con la edad calculada:")
    for nombre, datos in colombianos.items():
        print(nombre, datos)


def ejecutar_colombianos_fallecidos(colombianos: dict) -> None:
    """Ejecuta la opción que consulta qué colombianos han fallecido.
    Se debe mostrar al usuario los nombres de los colombianos que han fallecido.
    """

    if not colombianos:
        print("No se han cargado datos de colombianos. Cargue un archivo primero.")
        return

    colombianos_fallecidos = []

    # Identificar los colombianos que han fallecido
    for nombre, datos in colombianos.items():
        anio_muerte = datos['anio_muerte']

        if anio_muerte != 0:
            colombianos_fallecidos.append(nombre)

    if colombianos_fallecidos:
        print("Colombianos fallecidos:")
        for nombre in colombianos_fallecidos:
            print(nombre)
    else:
        print("No se encontraron colombianos fallecidos en los datos cargados.")


def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de colombianos.")
    print("2. Encontrar el colombiano con mayor número de lectores.")
    print("3. Encontrar si hay 3 colombianos que superen el tope de lectores.")
    print("4. Calcular el promedio de lectores de las personas de una ocupación específica.")
    print("5. Encontrar qué ocupación es la que tiene mayor número de lectores promedio.")
    print("6. Consultar colombianos con una ocupación específica que hayan nacido en un rango de años.")
    print("7. Contar cuantas personas hay de cada nacionalidad.")
    print("8. Calcular la edad de cada persona. ")
    print("9. Consultar qué colombianos han fallecido.")
    print("10. Salir.")


def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    colombianos = {}
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            colombianos = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_mayor_lectores(colombianos)
        elif opcion_seleccionada == 3:
            ejecutar_hay_3_colombianos(colombianos)
        elif opcion_seleccionada == 4:
            ejecutar_promedio_lectores(colombianos)
        elif opcion_seleccionada == 5:
            ejecutar_mayor_rating(colombianos)
        elif opcion_seleccionada == 6:
            ejecutar_colombianos_rango(colombianos)
        elif opcion_seleccionada == 7:
            ejecutar_nacionalidades(colombianos)
        elif opcion_seleccionada == 8:
            ejecutar_calcular_edad(colombianos)
        elif opcion_seleccionada == 9:
            ejecutar_colombianos_fallecidos(colombianos)
        elif opcion_seleccionada == 10:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")

        # Esperar a que el usuario presione una tecla antes de continuar
        input("Presione Enter para continuar...")
        # Limpiar la pantalla para mostrar nuevamente el menú
        os.system("cls" if os.name == "nt" else "clear")



# PROGRAMA PRINCIPAL
iniciar_aplicacion()
