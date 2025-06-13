# Parte B: Operaciones con años de nacimiento

#Libreria para determinar la fecha actual
from datetime import datetime

#region Funciones
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
def es_bisiesto(fecha):
    if fecha % 4 == 0:
            if fecha % 100 != 0:
                return 1
            elif fecha % 400 == 0:
                return 1
            else:
                return 0
    else:
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

#region Se solicitan las fechas y calculan edades
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
print(f"| » Tenemos un año especial (bisiesto)".ljust((thickness*5))+"|" if {hay_bisiesto >0} else "| » No hay año bisiesto".ljust((thickness*5))+"|")
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

#endregion





