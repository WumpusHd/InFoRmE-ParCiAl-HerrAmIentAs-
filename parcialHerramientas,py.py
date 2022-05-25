
def tiendita():
    
    print("----Bienvenido a tiendita----")
    print()
    cedula = int(input("Ingrese su cedula: "))

    if cedula != 0:
        rol = input("ingrese su rol (estudiante o profesor): ")
        if rol == "estudiante":
            beca = input("¿Eres becado? ")
        print()

    while cedula != 0:

        ans = []
        codigos = []
        pregunta = input("¿Va realizar alguna compra? ")
        print()

        while pregunta != "no":
            
            if pregunta == "si":
                print("ingrese los datos en el siguiente formato")
                print("codigo: NombreDelProducto Precio NumeroDeUnidades")
                productos = input("- ").split()
                ans.append(productos)
                codigos.append(productos[0])
            print()
            pregunta = input("¿Va realizar alguna otra compra? ")
            print()

        print("Factura:")
        print()
        x = 0
        for i in range(len(ans)):
            x += int(ans[i][2]) * int(ans[i][3])
        if rol == "estudiante" and beca == "si":
            print("el",rol,"con cedula",cedula,"debe pagar","$",(x - (x * 0.5)),"por los productos",codigos)
            print()
        elif rol == "estudiante":
            print("el",rol,"con cedula",cedula,"debe pagar","$",(x - (x * 0.3)),"por los productos",codigos)
            print()
        elif rol == "profesor":
            print("el",rol,"con cedula",cedula,"debe pagar","$",(x - (x * 0.2)),"por los productos",codigos)
            print()
            
        print("----Bienvenido a tiendita----")
        print()
        cedula = int(input("Ingrse su cedula: "))
        if cedula != 0:
            rol = input("ingrese su rol (estudiante o profesor): ")
            if rol == "estudiante":
                beca = input("¿Eres becado? ")
                print()
            print()
tiendita()
           
