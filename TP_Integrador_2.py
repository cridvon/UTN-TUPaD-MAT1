
# Importa las librerías necesarias
from datetime import datetime #Libreria para determinar la fecha actual
import os #Libreria para manejar OS

#region Funciones

def limpiar_pantalla():
    os.system("cls") # Limpia la pantalla en Windows



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

# Parte B: Operaciones con años de nacimiento

# 1. Ingreso de los años de nacimiento (Si dos o mas integrantes del grupo tienen el mismo año, ingresar algún dato ficticio, según el caso).
#region Ingreso de Fechas
def solicitar_fechas():
    cantidad=4
    fechas=[]
    for i in range(cantidad):
        fecha=input(f"Ingrese año de nacimiento N° {i+1}: ")
        #Se valida la fecha ingresada
        fecha_valida=validar(fecha,i)
        fechas.append(fecha_valida)
    return fechas

#Funcion que valida la fecha ingresada por el usuario
def validar(fecha,i):
    while True:
        try:
            entrada = int(fecha)
            if entrada > 0:
                return entrada
            else:
                print ("Ingresó un valor incorrecto")
                fecha=input(f"Ingrese nuevamente la fecha N° {i+1}: ")
        except ValueError:
            print ("Ingresó un valor incorrecto")
            fecha=input(f"Ingrese nuevamente la fecha N° {i+1}: ")
#endregion

# 2. Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.
#region Funcion para determinar si la fecha es par o impar
def anios_pares(fechas):
    pares=0
    for fecha in fechas:
        if fecha%2 == 0:
            pares+=1
    return pares
#endregion

# 3. Funcion para determinar si pertenecemos al Grupo Z
#region Funcion para determinar si pertenecemos al Grupo Z
def grupo_z(fechas):
    z=0
    for fecha in fechas:
        if fecha >= 2000:
            z+=1
    if z < 4:
        return "No Grupo Z"
    else:
        return "Grupo Z"
#endregion

# 4. Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".
#region Funcion para determinar si las fechas pertenecen a años bisiestos
def anio_bisiesto(fechas):
    bisiesto=0
    for fecha in fechas:
        bisiesto += es_bisiesto(fecha)
    return bisiesto
#endregion

# 5. Implementar una función para determinar si un año es bisiesto.
#region Funcion que determina si una fecha específica es año bisiesto            
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return 1
    return 0
#endregion 



# 6. Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.
#region Funcion que determina el producto cartesiano entre el conjunto de fechas y el de edades
def producto_cartesiano(fechas,edades):
    prod_cartesiano=[]
    for fecha in fechas:
        for edad in edades:
            prod_cartesiano.append({fecha,edad})
    return prod_cartesiano
#endregion

#region Funcion que calcula las edades según la fecha actual y las fechas ingresadas
def calcular_edades(fechas):
    edades=[]
    #Se determina el año actual
    anio_actual = datetime.now().year
    for fecha in fechas:
        #Se genera un array con las edades
        edades.append(anio_actual - fecha)   
    return edades
#endregion



#endregion

#Programa Principal-----------------------------------------------------------------------------------------------------------------

seccion = -1
while seccion != 0:
    print("Seleccione una sección:")
    print("1 - Parte A: Operaciones con DNI")
    print("2 - Parte B: Operaciones con Fechas de Nacimiento")
    print("0 - Salir")
    try: # Solicita al usuario que ingrese una sección 
        seccion = int(input("Seleccione una sección: "))
    except ValueError: # Manejo de excepción para entradas no válidas
        print("Entrada no válida. Por favor, ingrese un número del menú.")
        input("Presione Enter para continuar...")
        limpiar_pantalla()
        continue

    if seccion == 1:
    # 1. Ingreso de los DNIs (reales o ficticios).
    #region Pedir al usuario la cantidad de DNIs que va a ingresar
        while True:
            entrada = input("¿Cuántos DNI vas a ingresar?: ")
            if entrada.isdigit():
                cantidad = int(entrada)
                break
            else:
                print("Por favor, ingresá solo números enteros.")

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
            print("0 - Volver al menú principal")
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
    elif seccion == 2: 
        #region Se solicitan las fechas y calculan edades
        hay_bisiesto = 0 #Variable para determinar si hay año bisiesto
        fechas = solicitar_fechas()
        edades = calcular_edades(fechas)
        #endregion

        #region Se calcula el producto cartesiano
        prod_cartesiano=producto_cartesiano(fechas,edades)
        #endregion

        #region Se determinan años pares
        pares = anios_pares(fechas)
        #endregion

        #region Se determina Grupo Z
        grupoz=grupo_z(fechas)
        #endregion

        #region Se determina si hay años bisiestos
        hay_bisiesto = anio_bisiesto(fechas)
        #endregion

        #region Formato de texto
        #Variable para formato
        thickness=24

        #Se formatea y muestran los resultados
        print("-"*thickness*5)
        print("| B - Operaciones con años de nacimiento".ljust((thickness*5))+"|")
        print("-"*thickness*5)
        print("| Años: ".ljust(16)+f"{fechas[0]}".center(thickness)+" | "+f"{fechas[1]}".center(thickness)+" | "+f"{fechas[2]}".center(thickness)+" | "+f"{fechas[3]}".center(thickness-1)+"|")
        print("| Edades: ".ljust(16)+f"{edades[0]}".center(thickness)+" | "+f"{edades[1]}".center(thickness)+" | "+f"{edades[2]}".center(thickness)+" | "+f"{edades[3]}".center(thickness-1)+"|")
        print("-"*thickness*5)
        print(f"| » {pares} fechas nacieron en años pares y {4-pares} en años impares".ljust((thickness*5))+"|")
        print("-"*thickness*5)
        print(f"| » {grupoz}".ljust((thickness*5))+"|")
        print("-"*thickness*5)
        if hay_bisiesto > 0:
            print(f"| » Tenemos un año especial (bisiesto)".ljust((thickness*5))+"|")
        else:
            print(f"| » No hay año bisiesto".ljust((thickness*5))+"|")
        print("-"*thickness*5)
        print(f"| » El producto cartesiano del conjunto formado por las fechas con el conjunto formado por las edades actuales es: ".ljust((thickness*5))+"|")
        print("-"*thickness*5)
        for conjunto in prod_cartesiano[:8]:
            print(conjunto, end=" ; ")
        print()
        for conjunto in prod_cartesiano[8:]:
            print(conjunto, end=" ; ")
        print()
        print("-"*thickness*5)
        input("Presione Enter para continuar...")
    elif seccion == 0:
        print("Saliendo del programa...")
        input("Presione Enter para continuar...")
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")   
        input("Presione Enter para continuar...")
    limpiar_pantalla()
# Fin del programa principal
