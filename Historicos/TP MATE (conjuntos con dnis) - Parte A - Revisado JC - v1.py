
# Parte A: Operaciones con DNI

import os
#region Funciones

def limpiar_pantalla():
    os.system("cls")


# 3. Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.
#region Funciones Cálculo y visualización
def union_conjuntos(*conjuntos):
    if not conjuntos:
        return set()
    
    resultado = set()
    
    for conjunto in conjuntos:
        resultado = resultado.union(conjunto)
    return resultado

def interseccion_conjuntos(*conjuntos):
    if not conjuntos:
        return set()

    resultado = conjuntos[0]
    
    for conjunto in conjuntos[1:]:
        resultado = resultado.intersection(conjunto)
    return resultado

def diferencia_conjuntos(*conjuntos):
    if not conjuntos:
        return set()
    
    resultado = conjuntos[0]
    for conjunto in conjuntos[1:]:
        resultado = resultado.difference(conjunto)
    return resultado

def diferencia_simetrica(*conjuntos):
    if not conjuntos:
        return set()
    
    resultado = conjuntos[0]
    for conjunto in conjuntos[1:]:
        resultado = resultado.symmetric_difference(conjunto)
    return resultado

#endregion

# 4. Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
#region Conteo frecuencia
def contar_frecuencia_digitos(dni):
    frecuencia = {}
    for digito in dni:
        if digito in frecuencia:
            frecuencia[digito] += 1
        else:
            frecuencia[digito] = 1
    print("Frecuencia de dígitos:", frecuencia)
    return frecuencia
#endregion

# 5. Suma total de los dígitos de cada DNI.
# region Suma Digitos DNI
def suma_total_digitos_de_DNI(dni):
    suma = 0
    for digito in dni:
        suma += int(digito)  # Convertimos y sumamos en una sola línea
    print(f"La suma de los dígitos del dni ingresado {dni} es {suma}.")
#endregion

# 6. Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.
#region Evaluación de condiciones lógicas
# A - Si la unión de todos los conjuntos tiene más de 6 elementos distintos, entonces el conjunto global es considerado diverso
def union_conjuntos_total(lista_de_conjuntos):
    union_total = set()
    for conjunto in lista_de_conjuntos:
        union_total = union_total.union(conjunto)
    
    if len(union_total) > 6:
        resultado = "Conjunto global diverso, la unión de todos los conjuntos tiene más de 6 elementos distintos: "
    else:
        resultado = "Conjunto global no diverso la unión de todos los conjuntos NO tiene más de 6 elementos distintos: "
    print(f"{resultado}{union_total}")

# B - Si hay al menos un número común a todos los conjuntos, entonces se considera que hay un núcleo compartido
def hay_nucleo_compartido(lista_conjuntos):
    interseccion = set.intersection(*lista_conjuntos)

    if interseccion:
        print (f"Hay un núcleo compartido de los conjuntos estudiados: {sorted(interseccion)}")
    else:
        print ("No hay núcleo compartido en los conjuntos estudiados.")

#endregion

#endregion

#Programa Principal-----------------------------------------------------------------------------------------------------------------

# 1. Ingreso de los DNIs (reales o ficticios).
#region Pedir al usuario la cantidad de DNIs que va a ingresar
cantidad = int(input("¿Cuántos DNI vas a ingresar?: "))
lista_dni = []
#endregion

#region Pedir los DNIs al usuario
for i in range (cantidad):
    dni = input("Por favor, ingrese un número de DNI: ")
    lista_dni.append(dni)   
print(f"Los DNI ingresados son: {lista_dni}")
#endregion

# 2. Generación automática de los conjuntos de dígitos únicos.
#region Listas DNI
conjuntos_dni = [] #Armado de conjuntos con números únicos

for dni in lista_dni:
    conjunto = set(dni) # Se crean conjuntos de números únicos
    conjuntos_dni.append(conjunto)
#endregion

#region Mostrar resultados
print("\nConjuntos de dígitos únicos por cada DNI ingresado:")

for dni, conjunto in enumerate(conjuntos_dni, 1):
    print(f"DNI {dni}: {conjunto}")
#endregion

#region Menu
opcion = -1
while opcion != 0:
    print("\nIngrese la opción que desea :")
    print("1 - Suma total de los dígitos de cada DNI")
    print("2 - Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas")
    print("3 - Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica")
    print("4 - Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas") 
    print("0 - Salir")
    print("\nNota Opción 4:")
    print("A - Si la unión de todos los conjuntos tiene más de 6 elementos distintos, entonces el conjunto global es considerado diverso")
    print("B - Si hay al menos un número común a todos los conjuntos, entonces se considera que hay un núcleo compartido.\n")

    try: # Solicita al usuario que ingrese una opción
        opcion = int(input("Seleccione una opción: "))
    except ValueError: # Manejo de excepción para entradas no válidas
        print("Entrada no válida. Por favor, ingrese un número del menú.")
        input("Presione Enter para continuar...")
        limpiar_pantalla()
        continue
    
    if opcion == 1:
        for dni in lista_dni:
            suma_total_digitos_de_DNI(dni)
    
    if opcion == 2:
        for dni in lista_dni:
            contar_frecuencia_digitos(dni)
    
    if opcion == 3:
        resultado_union = union_conjuntos(*conjuntos_dni)
        print(f"\nUnión de todos los conjuntos: {resultado_union}")

        resultado_interseccion = interseccion_conjuntos(*conjuntos_dni)
        print(f"\nIntersección de todos los conjuntos: {resultado_interseccion}")

        resultado_diferencia = diferencia_conjuntos(*conjuntos_dni)
        print(f"\nDiferencia de los conjuntos: {resultado_diferencia}")
        
        resultado_diferencia_simetrica = diferencia_simetrica(*conjuntos_dni)
        print(f"\nDiferencia simétrica de los conjuntos: {resultado_diferencia_simetrica}")
    
    if opcion == 4:
        union_conjuntos_total(conjuntos_dni)
        hay_nucleo_compartido(conjuntos_dni)

    if opcion == 0:
        print("Saliendo del programa...")   

    input("Presione Enter para continuar...")
    limpiar_pantalla()
#endregion
