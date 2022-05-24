
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
            
                
    




"""
def obtenerMasPelicualas(d):

    dic = {}
    lis = []
    x = 0

    for i in d:
        for j in range(len(d[i][5])):
            if d[i][5][j] not in dic:
                dic[d[i][5][j]] = 1
            else:
                dic[d[i][5][j]] += 1
             
    for i in dic:
        if dic[i] >= x:
            lis.append(i)
            x = dic[i]
    return lis


d = {"Erase una vez en Hollywood" :
["Quentin Tarantino", "Humor Negro", 2016 , 90, 374,
["Leonardo Di Caprio", "Brad Pitt", "Margot Robbie"]],
"Avengers Endgame" :
["Hermanos Russo", "Accion", 2019 , 356, 2800 ,
["Mark Ruffalo", "Robert Downey Jr.", "Chris Evans",
"Chris Hemsworth", "Scarlett Johansson"]],
"The wolf of wall street" :
["Martin Scorsese", "Humor Negro", 2013 , 100, 392,
["Leonardo Di Caprio", "Margot Robbie", "Jonah Hill"]],
"The Ladykillers" :
["Alexander Mackendrick", "Humor Negro", 1955 , 2, 10,
["Alec Guinness", "Herbert Lom", "Peter Sellers", "Cecil Parker"]],
"50 First Dates" :
["Peter Segal", "Comedia Romantica", 2004 , 75, 120,
["Adam Sandler", "Drew Barrymore", "Rob Schneider"]],
"Titanic" :
["James Cameron", "Drama", 1997 , 200, 1843 ,
["Leonardo Di Caprio", "Kate Winslet", "Billy Zane", "Gloria Stuart"]]}


#print(obtenerMasPelicualas(d))

def actoresDirector(d,name):


    x = set()

    for i in d:
        if d[i][0] == name:
            for j in range(len(d[i][5])):
                x.add(d[i][5][j])
    z = list(x)
    return z



#print(actoresDirector(d,"Quentin Tarantino"))

def actoresCompañero(d):

    dic = {}
    
    for i in d:
        for j in range(len(d[i][5])):
            if d[i][5][j] not in dic:
                dic[d[i][5][j]] = set()
            for z in range (len(d[i][5])):
                if d[i][5][z] != dic[d[i][5][j]]:
                    dic[d[i][5][j]].add(d[i][5][z])         
                            
    return dic

#print(actoresCompañero(d))












# cad = input()
#    detectar espacio, eliminar caracteres como el salto de linea

from sys import stdin

def leerImprimir():
    
    cad = stdin.readline()

#    while cad != "":
    while len(cad) > 1:
#        print("cadena leida",cad[:-1],"****")
#    listaPalabras = cad.split()
    
        cad = stdin.readline()
    print("fin")

#leerImprimir()

#si el codigo ascci estan en un rango
print(ord("a"))





cad = "hola"

print(cad.upper()) # vuelve las cadenas mayusculas

print(cad.lower()) # vuelve la cadena minuscula



        
# ctrl + d para terminar




# para organizar palabras
ans = ["b","d","e","f","a","c","i"]

ans.sort()

print(ans)


    ans,lista = set(),[]
    for i in range(len(lis)):
        for j in (set(lis[i])):
            if j in ans:lista.append(j)
            ans.add(j)         
    return lista
            
print(obtenerElementos([[1, 8, 4,4], [2,1, 5, 3], [2, 6, 7], [8, 9]]))
"""

















