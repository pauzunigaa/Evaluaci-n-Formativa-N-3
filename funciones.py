
CARGOS = ["ceo", "desarrollador", "analista de datos"]
def registrar_trabajador(trabajadores):

    nombre=input (" Ingrese nombre y apellido del trabajador : ")
    cargo=input(" Ingrese el cargo del trabajador ( Ceo / Desarrollador / Analista de datos)").lower()

    while cargo not in CARGOS:# este while verifica que sea verdad
        print(" Cargo no existe, intente nuevamente ")
        cargo=input(" Ingrese el cargo del trabajador ( ceo / Desarrollador / Analista de datos)").lower()
    sueldoBruto=int(input(" Ingrese sueldo bruto del trabajador : "))


    #calcular los descuentos
    descSalud = sueldoBruto*0.07
    descAFP = sueldoBruto* 0.12
    liquidoPagar = sueldoBruto - descSalud - descAFP

    trabajadores.append({
        " Nombre " : nombre,
        " Cargo " : cargo,
        " SueldoBruto " : sueldoBruto,
        " DescSalud " : descSalud,
        " DescAFP " : descAFP,
        " LiquidoPagar " : liquidoPagar
    })

def listar_trabajadores(trabajadores):
    print(" Lista de trabajadores")
    for trabajador in trabajadores:
        print(trabajador)

def  imprimir_plantilla(trabajadores):
    cargoSeleccionado = input(" Ingrese cargo para imprimir planilla o bien presione ENTER par seleccionar todos: ").lower
    if cargoSeleccionado == "":
        trabajadores_a_imprimir = trabajadores
        nombreArchivo = "planilla_todos.txt"
    elif cargoSeleccionado in CARGOS:
        trabajadores_a_imprimir = []
        for trabajador in trabajadores:
            if trabajador["Cargo"] == cargoSeleccionado:
                trabajadores_a_imprimir.append(trabajador)
            nombreArchivo =f' planilla_{cargoSeleccionado}.txt'
    else:
        print(" Cargo no vàlido ")
        return

    with open (nombreArchivo,"w") as archivo:
       for trabajador in trabajadores_a_imprimir:
           archivo.write(f" Nombre y Apellido : {trabajador[" Nombre "]}\n")
           archivo.write(f" Cargo : {trabajador[" Cargo "]}\n")
           archivo.write(f" SueldoBruto : {trabajador[" SueldoBruto "]}\n")
           archivo.write(f" DescSalud : {trabajador[" DescSalud "]}\n")
           archivo.write(f" DescAFP : {trabajador[" DescAFP "]}\n")
           archivo.write(f" LiquidoPagar : {trabajador[" LiquidoPagar "]}\n")
