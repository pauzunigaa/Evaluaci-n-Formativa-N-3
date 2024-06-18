CARGOS = ["ceo","analista programador","desarrollador"]
def registrar_trabajador(trabajadores):#validando nombre , aqui le paso la lista trabajadores del main
    while True:
        nombre=input("Ingrese nombre y apellido trabajador ")
        if nombre =="":
            print(" Porfavor ingrese un dato valido")
        else:
            break
    cargo = ""  
    while cargo not in CARGOS:
        cargo=input("Ingrese cargo ( ceo / Analista programador / desarrollador :").lower()
        
    sueldoBruto=int(input("Ingrese sueldo Bruto:"))
    dsctSalud = sueldoBruto *0.12
    dsctAFP = sueldoBruto *0.07
    liquidoaPagar= sueldoBruto - dsctSalud - dsctAFP
    trabajador={
        "Nombre":nombre,
        "Cargo" :cargo,
        "Sueldo Bruto":sueldoBruto,
        "Descuento Salud":dsctSalud,
        "Liquido a Pagar":liquidoaPagar,
        "Descuento AFP" : dsctAFP
    }
    trabajadores.append(trabajador)
    print(trabajadores)
    
def listar_trabajadores(trabajadores):
    print("{:<20} {:<15} {:<15} {:<15} {:<15}".format("Trabajador", "Cargo", "Sueldo Bruto", "Descuento Salud", "Líquido Pagar","Descuento AFP"))
    print("=" * 80)
    for elemento in trabajadores:
        print("{:<20} {:<15} {:<15} {:<15} {:<15}".format(elemento["Nombre"],elemento["Cargo"],elemento["Sueldo Bruto"],elemento["Descuento Salud"],elemento["Liquido a Pagar"],elemento["Descuento AFP"]))
       
    
def imp_planilla_sueldo(trabajadores):
    print("{:<20} {:<15} {:<15} {:<15} {:<15}".format(elemento["Nombre"],elemento["Cargo"],elemento["Sueldo Bruto"],elemento["Descuento Salud"],elemento["Liquido a Pagar"],elemento["Descuento AFP"]))
