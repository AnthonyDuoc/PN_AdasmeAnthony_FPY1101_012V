import random
import statistics
import csv

SUELDO = []
TRABAJADORES = [
    {"nombre": "Juan Perez", "cargo": "Consultor TI"},
    {"nombre": "Maria Garcia", "cargo": "Analista"},
    {"nombre": "Carlos Lopez", "cargo": "Programador"},
    {"nombre": "Ana Martinez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Pedro Rodriguez", "cargo": "Consultor TI"},
    {"nombre": "Laura Hernandez", "cargo": "Analista"},
    {"nombre": "Miguel Sanchez", "cargo": "Programador"},
    {"nombre": "Isabel Gomez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Francisco Diaz", "cargo": "Consultor TI"},
    {"nombre": "Elena Fernandez", "cargo": "Analista"}
]
#Revision
#Menu principal
while True:
    print("\nBienvenido al asistente de sueldos")
    print("1.Asignar sueldos aleatorios")
    print("2.Clasificar sueldos")
    print("3.Ver estadísticas")
    print("4.Reporte de sueldos")
    print("5.Salir")

    opcion = int(input("Seleccione una opción: "))

    #Asignacion de sueldos
    def asignar_sueldos(TRABAJADORES, SUELDO):
        print("\nSueldos generados...")
        for i in range(len(TRABAJADORES)):
            sueldo = random.randint(300000, 2500000)
            sueldo_format = f"$ {sueldo:,}"
            SUELDO.append(sueldo)
            print(f"{TRABAJADORES[i]['nombre'].ljust(20)} {TRABAJADORES[i]['cargo'].ljust(20)} - {str(sueldo_format).rjust(5)}")

    #Clasificacion de sueldos
    def clasificar_sueldos(TRABAJADORES, SUELDO):
        total_personas_sueldo1 = 0
        total_personas_sueldo2 = 0
        total_personas_sueldo3 = 0
        print("\nSueldos clasificados: \n")
        print("Sueldos menor a 800.000: \n")
        for t in range(len(TRABAJADORES)):
            sueldo = SUELDO[t]
            if sueldo < 800000:
                print(f"{TRABAJADORES[t]['nombre'].ljust(20)}{TRABAJADORES[t]['cargo'].ljust(20)} - $ {sueldo:,.0f}")
                total_personas_sueldo1 += 1
        print(f"Total : {total_personas_sueldo1:,}")
    
        print("\nSueldos entre 800.000 y 2.000.000: \n")
        for t in range(len(TRABAJADORES)):
            sueldo = SUELDO[t]
            if sueldo >= 800000 and sueldo < 2000000:
                print(f"{TRABAJADORES[t]['nombre'].ljust(20)}{TRABAJADORES[t]['cargo'].ljust(20)} - $ {sueldo:,.0f}")
                total_personas_sueldo2 += 1
        print(f"Total : {total_personas_sueldo2:,}")
    
        print("\nSueldos superiores a 2.000.000: \n")
        for t in range(len(TRABAJADORES)):
            sueldo = SUELDO[t]
            total_sueldos = int(sum(SUELDO))
            if sueldo >= 2000000:
                print(f"{TRABAJADORES[t]['nombre'].ljust(20)}{TRABAJADORES[t]['cargo'].ljust(20)} - $ {sueldo:,.0f}")
                total_personas_sueldo3 += 1
        print(f"Total : {total_personas_sueldo3:,}")
        print(f"\nTotal suma de todos los sueldos:  {total_sueldos:,}")

    #Estadisticas de sueldos
    def ver_estadisticas(TRABAJADORES,SUELDO):
        print("\nEstadísticas sueldos: ")
        suelo_alto = max(SUELDO)
        suelo_bajo = min(SUELDO)
        geometrica = statistics.geometric_mean(SUELDO)
        promedio = sum(SUELDO) / len(SUELDO)
        media = statistics.mean(SUELDO)

        print(f"{'Sueldo más alto:'.ljust(20)} $ {suelo_alto:,.0f}")
        print(f"{'Sueldo más bajo:'.ljust(20)} $ {suelo_bajo:,.0f}")
        print(f"{'Geométrica:'.ljust(20)} $ {geometrica:.2f}")
        print(f"{'Promedio:'.ljust(20)} $ {promedio:.2f}")
        print(f"{'Media:'.ljust(20)} $ {media:.2f}")
        
    #Reporte de sueldos
    def reporte_sueldos(TRABAJADORES,SUELDO):
        titulo_nombre = "Empleado"
        titulo_cargo = "Cargo"
        titulo_sueldo = "Sueldo Base"
        titulo_afp = "Desc. AFP"
        titulo_salud = "Desc. Salud"
        titulo_liquido = "Sueldo Liquido"
        print("\n Reporte de sueldos: ")
        print(f"{titulo_nombre.ljust(20)} {titulo_cargo.ljust(20)} {titulo_sueldo.rjust(22)} {titulo_afp.rjust(21)} {titulo_salud.rjust(23)} {titulo_liquido.rjust(20)}")
        
        with open("reporte_sueldos.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre".center(20), "Cargo".center(20), "Sueldo Base".center(22), "Desc. AFP 7%".center(22), "Desc. Salud 12%".center(22), "Sueldo Liquido".center(20)])
            for i in range(len(TRABAJADORES)):
                descuento_afp = 0.07 * SUELDO[i]
                descuento_salud = 0.12 * SUELDO[i]
                sueldo_liquido = SUELDO[i] - descuento_afp - descuento_salud
                sueldo_format_liquido = f"$ {sueldo_liquido:,.0f}"
                sueldo_format = f"$ {SUELDO[i]:,.0f}"
                descuento_afp_format = f"$ {descuento_afp:,.0f}"
                descuento_salud_format = f"$ {descuento_salud:,.0f}"
                writer.writerow([TRABAJADORES[i]['nombre'].center(20), TRABAJADORES[i]['cargo'].center(20), str(sueldo_format).center(20) , str(descuento_afp_format).center(20), str(descuento_salud_format).center(20), str(sueldo_format_liquido).center(20)])
                print(f"{TRABAJADORES[i]['nombre'].ljust(20)}, {TRABAJADORES[i]['cargo'].ljust(20)}, {str(sueldo_format).rjust(20)}, {str(descuento_afp_format).rjust(20)}, {str(descuento_salud_format).rjust(20)}, {str(sueldo_format_liquido).rjust(20)}")
            print("\n Reporte de sueldos creado en CSV \n")
            

    #Opciones del mennu principal
    if opcion == 1:
        asignar_sueldos(TRABAJADORES,SUELDO)
    elif opcion == 2:
        clasificar_sueldos(TRABAJADORES,SUELDO)
    elif opcion == 3:
        ver_estadisticas(TRABAJADORES,SUELDO)
    elif opcion == 4:
        reporte_sueldos(TRABAJADORES,SUELDO)
    elif opcion == 5:
        print("\nFinalizando el programa... \nDesarrollado por Anthony Adasme \nRut : 19.345.014-8")
        break
    else:
        print("Esta opcion no es valida. Por favor, intente nuevamente.")
