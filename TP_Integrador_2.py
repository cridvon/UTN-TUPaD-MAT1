# ============================================================================
# TRABAJO PRÁCTICO INTEGRADOR 2 - REESTRUCTURADO
# ============================================================================

# Importa las librerías necesarias
from datetime import datetime  # Librería para determinar la fecha actual
import os  # Librería para manejar OS

# ============================================================================
# SECCIÓN 1: FUNCIONES AUXILIARES Y UTILIDADES
# ============================================================================

def limpiar_pantalla():
    """Limpia la pantalla en Windows"""
    os.system("cls")

# ============================================================================
# SECCIÓN 2: OPERACIONES CON DNI - FUNCIONES DE CONJUNTOS
# ============================================================================

def union_conjuntos(*conjuntos):
    """
    3. Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.
    Calcula la unión de múltiples conjuntos
    """
    if not conjuntos:
        return set()
    
    resultado = set()
    for conjunto in conjuntos:
        resultado = resultado.union(conjunto)
    return resultado

def interseccion_conjuntos(*conjuntos):
    """Calcula la intersección de múltiples conjuntos"""
    if not conjuntos:
        return set()

    resultado = conjuntos[0]
    for conjunto in conjuntos[1:]:
        resultado = resultado.intersection(conjunto)
    return resultado

def diferencia_conjuntos(*conjuntos):
    """Calcula la diferencia de múltiples conjuntos"""
    if not conjuntos:
        return set()
    
    resultado = conjuntos[0]
    for conjunto in conjuntos[1:]:
        resultado = resultado.difference(conjunto)
    return resultado

def diferencia_simetrica(*conjuntos):
    """Calcula la diferencia simétrica de múltiples conjuntos"""
    if not conjuntos:
        return set()
    
    resultado = conjuntos[0]
    for conjunto in conjuntos[1:]:
        resultado = resultado.symmetric_difference(conjunto)
    return resultado

# ============================================================================
# SECCIÓN 3: OPERACIONES CON DNI - ANÁLISIS DE DÍGITOS
# ============================================================================

def contar_frecuencia_digitos(dni):
    """
    4. Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
    """
    frecuencia = {}
    for digito in dni:
        if digito in frecuencia:
            frecuencia[digito] += 1
        else:
            frecuencia[digito] = 1
    print("Frecuencia de dígitos:", frecuencia)
    return frecuencia

def suma_total_digitos_de_DNI(dni):
    """
    5. Suma total de los dígitos de cada DNI.
    """
    suma = 0
    for digito in dni:
        suma += int(digito)  # Convertimos y sumamos en una sola línea
    print(f"La suma de los dígitos del DNI ingresado {dni} es {suma}.")

# ============================================================================
# SECCIÓN 4: OPERACIONES CON DNI - EVALUACIÓN DE CONDICIONES LÓGICAS
# ============================================================================

def union_conjuntos_total(lista_de_conjuntos):
    """
    6. Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.
    A - Si la unión de todos los conjuntos tiene más de 6 elementos distintos, 
    entonces el conjunto global es considerado diverso
    """
    union_total = set()
    for conjunto in lista_de_conjuntos:
        union_total = union_total.union(conjunto)
    
    if len(union_total) > 6:
        resultado = "Conjunto global diverso. La unión de todos los conjuntos tiene más de 6 elementos distintos: "
    else:
        resultado = "Conjunto global no diverso. La unión de todos los conjuntos NO tiene más de 6 elementos distintos: "
    print(f"{resultado}{union_total}")

def hay_nucleo_compartido(lista_conjuntos):
    """
    B - Si hay al menos un número común a todos los conjuntos, 
    entonces se considera que hay un núcleo compartido
    """
    interseccion = set.intersection(*lista_conjuntos)

    if interseccion:
        print(f"Hay un núcleo compartido de los conjuntos estudiados: {sorted(interseccion)}")
    else:
        print("No hay núcleo compartido en los conjuntos estudiados.")

# ============================================================================
# SECCIÓN 5: OPERACIONES CON AÑOS DE NACIMIENTO - ENTRADA DE DATOS
# ============================================================================

def solicitar_fechas():
    """
    Parte B: Operaciones con años de nacimiento
    1. Ingreso de los años de nacimiento (Si dos o más integrantes del grupo tienen el mismo año, 
    ingresar algún dato ficticio, según el caso).
    """
    cantidad = 4
    fechas = []
    print("Debe ingresar 4 fechas diferentes.")
    for i in range(cantidad):
        fecha = input(f"Ingrese año de nacimiento N° {i+1}: ")
        # Se valida la fecha ingresada
        fecha_valida = validar_fecha(fecha, i)
        fechas.append(fecha_valida)
    return fechas

def validar_fecha(fecha, i):
    """Función que valida la fecha ingresada por el usuario"""
    while True:
        try:
            anio_actual = datetime.now().year
            entrada = int(fecha)
            if entrada > 0 and entrada <= datetime.now().year:
                return entrada
            else:
                print("Ingresó un valor incorrecto")
                fecha = input(f"Ingrese nuevamente la fecha N° {i+1}: ")
        except ValueError:
            print("Ingresó un valor incorrecto")
            fecha = input(f"Ingrese nuevamente la fecha N° {i+1}: ")

def calcular_edades(fechas):
    """Función que calcula las edades según la fecha actual y las fechas ingresadas"""
    edades = []
    # Se determina el año actual
    anio_actual = datetime.now().year
    for fecha in fechas:
        # Se genera un array con las edades
        edades.append(anio_actual - fecha)   
    return edades

# ============================================================================
# SECCIÓN 6: OPERACIONES CON AÑOS DE NACIMIENTO - ANÁLISIS Y CÁLCULOS
# ============================================================================

def anios_pares(fechas):
    """
    2. Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.
    Función para determinar si la fecha es par o impar
    """
    pares = 0
    for fecha in fechas:
        if fecha % 2 == 0:
            pares += 1
    return pares

def grupo_z(fechas):
    """
    3. Función para determinar si pertenecemos al Grupo Z
    """
    z = 0
    for fecha in fechas:
        if fecha >= 2000:
            z += 1
    if z < 4:
        return "No Grupo Z"
    else:
        return "Grupo Z"

def anio_bisiesto(fechas):
    """
    4. Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".
    Función para determinar si las fechas pertenecen a años bisiestos
    """
    bisiesto = 0
    for fecha in fechas:
        bisiesto += es_bisiesto(fecha)
    return bisiesto

def es_bisiesto(anio):
    """
    5. Implementar una función para determinar si un año es bisiesto.
    Función que determina si una fecha específica es año bisiesto
    """
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return 1
    return 0

def producto_cartesiano(fechas, edades):
    """
    6. Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.
    Función que determina el producto cartesiano entre el conjunto de fechas y el de edades
    """
    prod_cartesiano = []
    for fecha in fechas:
        for edad in edades:
            prod_cartesiano.append({fecha, edad})
    return prod_cartesiano

# ============================================================================
# SECCIÓN 7: MENÚ Y PROCESAMIENTO DE DNI
# ============================================================================

def procesar_parte_a():
    """Procesa toda la Parte A: Operaciones con DNI"""
    # 1. Ingreso de los DNIs (reales o ficticios).
    # Pedir al usuario la cantidad de DNIs que va a ingresar
    while True:
        entrada = input("¿Cuántos DNI vas a ingresar?: ")
        if entrada.isdigit():
            cantidad = int(entrada)
            break
        else:
            print("Por favor, ingresá solo números enteros.")
    
    # Pedir los DNIs al usuario
    lista_dni = []
    for i in range(cantidad):
        while True:
            dni = input("Por favor, ingrese un número de DNI: ")
            if dni.isdigit() and 7 <= len(dni) <= 8:
                lista_dni.append(dni)
                break
            else:
                print("DNI inválido. Debe ser un número de 7 u 8 dígitos.")

    print(f"Los DNI ingresados son: {lista_dni}")

    # 2. Generación automática de los conjuntos de dígitos únicos.
    conjuntos_dni = []  # Armado de conjuntos con números únicos

    for dni in lista_dni:
        conjunto = set(dni)  # Se crean conjuntos de números únicos
        conjuntos_dni.append(conjunto)

    # Mostrar resultados
    print("\nConjuntos de dígitos únicos por cada DNI ingresado:")
    for dni, conjunto in enumerate(conjuntos_dni, 1):
        print(f"DNI {dni}: {conjunto}")

    # Menú de opciones para la Parte A
    menu_parte_a(lista_dni, conjuntos_dni)

def menu_parte_a(lista_dni, conjuntos_dni):
    """Maneja el menú de opciones para la Parte A"""
    opcion = -1
    while opcion != 0:
        print("\nIngrese la opción que desea:")
        print("1 - Suma total de los dígitos de cada DNI")
        print("2 - Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas")
        print("3 - Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica")
        print("4 - Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas") 
        print("0 - Volver al menú principal")
        print("\nNota Opción 4:")
        print("A - Si la unión de todos los conjuntos tiene más de 6 elementos distintos, entonces el conjunto global es considerado diverso")
        print("B - Si hay al menos un número común a todos los conjuntos, entonces se considera que hay un núcleo compartido.\n")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número del menú.")
            input("Presione Enter para continuar...")
            limpiar_pantalla()
            continue
        
        ejecutar_opcion_parte_a(opcion, lista_dni, conjuntos_dni)

def ejecutar_opcion_parte_a(opcion, lista_dni, conjuntos_dni):
    """Ejecuta la opción seleccionada en la Parte A"""
    if opcion == 1:
        for dni in lista_dni:
            suma_total_digitos_de_DNI(dni)
    
    elif opcion == 2:
        for dni in lista_dni:
            contar_frecuencia_digitos(dni)
    
    elif opcion == 3:
        resultado_union = union_conjuntos(*conjuntos_dni)
        print(f"\nUnión de todos los conjuntos: {resultado_union}")

        resultado_interseccion = interseccion_conjuntos(*conjuntos_dni)
        print(f"\nIntersección de todos los conjuntos: {resultado_interseccion}")

        resultado_diferencia = diferencia_conjuntos(*conjuntos_dni)
        print(f"\nDiferencia de los conjuntos: {resultado_diferencia}")
        
        resultado_diferencia_simetrica = diferencia_simetrica(*conjuntos_dni)
        print(f"\nDiferencia simétrica de los conjuntos: {resultado_diferencia_simetrica}")
    
    elif opcion == 4:
        union_conjuntos_total(conjuntos_dni)
        hay_nucleo_compartido(conjuntos_dni)

    elif opcion == 0:
        print("Saliendo del programa...")
        return

    if opcion != 0:
        input("Presione Enter para continuar...")
        limpiar_pantalla()

# ============================================================================
# SECCIÓN 8: PROCESAMIENTO DE AÑOS DE NACIMIENTO
# ============================================================================

def procesar_parte_b():
    """Procesa toda la Parte B: Operaciones con años de nacimiento"""
    # Se solicitan las fechas y calculan edades
    hay_bisiesto = 0  # Variable para determinar si hay año bisiesto
    fechas = solicitar_fechas()
    edades = calcular_edades(fechas)
    
    # Se calcula el producto cartesiano
    prod_cartesiano = producto_cartesiano(fechas, edades)
    
    # Se determinan años pares
    pares = anios_pares(fechas)
    
    # Se determina Grupo Z
    grupoz = grupo_z(fechas)
    
    # Se determina si hay años bisiestos
    hay_bisiesto = anio_bisiesto(fechas)
    
    # Mostrar resultados formateados
    mostrar_resultados_parte_b(fechas, edades, pares, grupoz, hay_bisiesto, prod_cartesiano)

def mostrar_resultados_parte_b(fechas, edades, pares, grupoz, hay_bisiesto, prod_cartesiano):
    """Muestra los resultados de la Parte B con formato"""
    # Variable para formato
    thickness = 24

    # Se formatea y muestran los resultados
    print("-" * thickness * 5)
    print("| B - Operaciones con años de nacimiento".ljust((thickness * 5)) + "|")
    print("-" * thickness * 5)
    print("| Años: ".ljust(16) + f"{fechas[0]}".center(thickness) + " | " + f"{fechas[1]}".center(thickness) + " | " + f"{fechas[2]}".center(thickness) + " | " + f"{fechas[3]}".center(thickness - 1) + "|")
    print("| Edades: ".ljust(16) + f"{edades[0]}".center(thickness) + " | " + f"{edades[1]}".center(thickness) + " | " + f"{edades[2]}".center(thickness) + " | " + f"{edades[3]}".center(thickness - 1) + "|")
    print("-" * thickness * 5)
    print(f"| » {pares} fechas nacieron en años pares y {4 - pares} en años impares".ljust((thickness * 5)) + "|")
    print("-" * thickness * 5)
    print(f"| » {grupoz}".ljust((thickness * 5)) + "|")
    print("-" * thickness * 5)
    
    if hay_bisiesto > 0:
        print(f"| » Tenemos un año especial (bisiesto)".ljust((thickness * 5)) + "|")
    else:
        print(f"| » No hay año bisiesto".ljust((thickness * 5)) + "|")
    
    print("-" * thickness * 5)
    print(f"| » El producto cartesiano del conjunto formado por las fechas con el conjunto formado por las edades actuales es: ".ljust((thickness * 5)) + "|")
    print("-" * thickness * 5)
    
    for conjunto in prod_cartesiano[:8]:
        print(conjunto, end=" ; ")
    print()
    for conjunto in prod_cartesiano[8:]:
        print(conjunto, end=" ; ")
    print()
    print("-" * thickness * 5)
    input("Presione Enter para continuar...")

# ============================================================================
# SECCIÓN 9: PROGRAMA PRINCIPAL
# ============================================================================

def menu_principal():
    """Función principal que maneja el menú principal del programa"""
    seccion = -1
    while seccion != 0:
        print("Seleccione una sección:")
        print("1 - Parte A: Operaciones con DNI")
        print("2 - Parte B: Operaciones con Fechas de Nacimiento")
        print("0 - Salir")
        
        try:
            seccion = int(input("Seleccione una sección: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número del menú.")
            input("Presione Enter para continuar...")
            limpiar_pantalla()
            continue

        if seccion == 1:
            procesar_parte_a()
        elif seccion == 2:
            procesar_parte_b()
        elif seccion == 0:
            print("Saliendo del programa...")
            input("Presione Enter para continuar...")
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")   
            input("Presione Enter para continuar...")
        
        limpiar_pantalla()

# ============================================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================================


menu_principal()

# Fin del programa principal