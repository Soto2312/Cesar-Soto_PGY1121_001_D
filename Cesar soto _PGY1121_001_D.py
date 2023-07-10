from os import system
system = "cls"

evento = [{j + 10  * i for j in range(10) for i in range (10)}]
platinum = 120.000
gold = 80.000
siver = 50.000
persona= {}
def mostar_ubicacion ():
    print("Estado de asiento")
    for fila in evento:
        for ubicacion in fila:
            if ubicacion in persona:
                print("x",end="\t")
            else:
                print(ubicacion, end="\t")
        print()
    print()
    
def comprar_entradas():
    ubicacion= int(input(" Ingrese la ubicacion que desea comprar"))
    
    if ubicacion in persona:
        print(" La ubicacion no esta disponible") 
    else:
        rut= int(input("Ingrese el rut (sin puntos y gion)"))
        persona[ubicacion]=rut
        print("Operacion exitosamente")
        
def asiento_disponible():
    asiento = 0
    for fila in evento:
        if asiento not in persona: 
            asiento +=1
        print(f"ubicacion disponible: {asiento}")  
        
def listas_registrada():
    if not persona:
        print(" No se encuentra personas registrada")
    else:
        print("Listado persona: ")
        for ubicacion , rut in sorted(persona.items()):
            print(f"ubicacion{ubicacion}: run {rut}") 
            
def ganacias():
    total = 0
    for ubicacion, rut in persona.items():
        if ubicacion <= 20:
            total += platinum
        elif ubicacion <= 50 :
            total += gold
        else:
            total += siver
    print(f"Total ganancia: ${total}")

while True:
    print("** MENU***")
    print("1, COMPRA ENTRADA")
    print("2, MOSTRAR UICACION")
    print("3, LISTA DE ASIENTOS")
    print("4, MOSTRAS GANACIAS")
    print("5, SALIR")
    
    
    opcion= input( "Ingrese una opcion:")
    
    if opcion == "1":
        mostar_ubicacion()
        comprar_entradas()
        mostar_ubicacion()
    elif opcion =="2":
        mostar_ubicacion()
        mostar_ubicacion()
    elif opcion =="3":
        listas_registrada()
    elif opcion =="4":
        ganacias()
    elif opcion =="5":
        print("Hazta luego")
            
        
        
        
       
    
            
        
                
                
            
            
                
          
            
    
            
    