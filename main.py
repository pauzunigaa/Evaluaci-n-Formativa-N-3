import funciones as fn
trabajadores=[]
while True:
    try:
        print(" Menu ")
        print(" 1.- Registrar trabajador")
        print(" 2.- Listar todos los trabajadores")
        print(" 3.- Imprimir planilla sueldos ")
        print(" 4.- Salir")
        2
        opcionMenu=float(input(" Escoja una opción : "))
        
        print("=" * 80)
        print("=" * 80)

        if opcionMenu==1:
            fn.registrar_trabajador(trabajadores)
            print("=" * 80)

        elif opcionMenu==2:
            fn.listar_trabajadores(trabajadores)
            print("=" * 80)
        elif opcionMenu==3:
            print("=" * 80)
        elif opcionMenu==4:
            print("=" * 80)
            print("Saliendo del programa...")
            break
    except ValueError:
        print("Ingrese una opcion valida")