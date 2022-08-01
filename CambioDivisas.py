
print("BIENVENIDO AL COVERSOR DE DIVISAS")
print("""Opciones de divisas:
A)Euro
B)Dolar Estadounidense
C)Libra
D)Yen""")
moneda_cambiar = str(input("Introduce la divisa que desea cambiar: "))
moneda_cambiar_min = moneda_cambiar.lower()

if moneda_cambiar_min == "a" :
    print("La moneda seleccionada es el EURO")
    
    
elif moneda_cambiar_min == "b":
    print("La moneda seleccionada es el DOLAR")
    
    
elif moneda_cambiar_min == "c":
    print("La moneda seleccionada es la LIBRA")
    
    
elif moneda_cambiar_min == "d":
    print("La moneda seleccionada es el YEN")
    
    
else :
    print("El valor seleccionado no existe")



moneda_cambio = str(input("Introduzca la divisa a la que desea cambiar: "))
moneda_cambio_min = moneda_cambio.lower()

if moneda_cambio_min == "a" :
    print("La moneda seleccionada es el EURO")
    
    
elif moneda_cambio_min == "b":
    print("La moneda seleccionada es el DOLAR")

    
elif moneda_cambio_min == "c":
    print("La moneda seleccionada es la LIBRA")

    
elif moneda_cambio_min == "d":
    print("La moneda seleccionada es el YEN")

else :
    print("El valor seleccionado no existe")


if moneda_cambiar_min == "a" and moneda_cambio_min == "b":
    print("Vas a convertir de Euros a Dolares estadounidenses.")
    cantidad = float(input("Introduzca la cantidad de Euros que desea convertir: "))
    print("La cantidad de Dolares es: ", cantidad * 1.19)
    
elif moneda_cambiar_min == "b" and moneda_cambio_min == "a":
    print("Vas a cambiar de Dolares estadounidenses a Euros ")
    cantidad = float(input("Introduzca la cantidad de Dolares que desea convertir: "))
    print("La cantidad de Euros es: ", cantidad * 0.84)
    
elif moneda_cambiar_min == "a" and moneda_cambio_min == "c":
    print("Vas a cambiar de Euros a Libras ")
    cantidad = float(input("Introduzca la cantidad de Euros que desea convertir: "))
    print("La cantidad de Libras es: ", cantidad * 0.87)
    
elif moneda_cambiar_min == "c" and moneda_cambio_min == "a":
    print("Vas a cambiar de Libras a Euros ")
    cantidad = float(input("Introduzca la cantidad de Libras que desea convertir: "))
    print("La cantidad de Euros es: ", cantidad * 1.15)
    
elif moneda_cambiar_min == "a" and moneda_cambio_min == "d":
    print("Vas a cambiar de Euros a Yenes ")
    cantidad = float(input("Introduzca la cantidad de Euros que desea convertir: "))
    print("La cantidad de Yenes es: ", cantidad * 130.5)
    
elif moneda_cambiar_min == "d" and moneda_cambio_min == "a":
    print("Vas a cambiar de Yen a Euros ")
    cantidad = float(input("Introduzca la cantidad de Yenes que desea convertir: "))
    print("La cantidad de Euros es: ", cantidad * 0.0077)   
    
elif moneda_cambiar_min == "b" and moneda_cambio_min == "c":
    print("Vas a cambiar de Dolares estadounidenses a Libras ")
    cantidad = float(input("Introduzca la cantidad de Dolares que desea convertir: "))
    print("La cantidad de Libras es: ", cantidad * 0.73)
    
elif moneda_cambiar_min == "c" and moneda_cambio_min == "b":
    print("Vas a cambiar de Libras a Dolares estadounidenses ")
    cantidad = float(input("Introduzca la cantidad de Libras que desea convertir: "))
    print("La cantidad de Dolares es: ", cantidad * 1.37)   
    
elif moneda_cambiar_min == "b" and moneda_cambio_min == "d":
    print("Vas a cambiar de Dolares estadounidenses a Yen")
    cantidad = float(input("Introduzca la cantidad de Dolares que desea convertir: "))
    print("La cantidad de Yenes es: ", cantidad * 109.64)
    
elif moneda_cambiar_min == "d" and moneda_cambio_min == "b":
    print("Vas a cambiar de Yen a Dolares estadounidense")
    cantidad = float(input("Introduzca la cantidad de Yenes que desea convertir: "))
    print("La cantidad de Dolares es: ", cantidad * 0.0091)   
    
elif moneda_cambiar_min == "c" and moneda_cambio_min == "d":
    print("Vas a cambiar de Libras a Yenes")
    cantidad = float(input("Introduzca la cantidad de Libras que desea convertir: "))
    print("La cantidad de Yenes es: ", cantidad * 150.36)
    
elif moneda_cambiar_min == "d" and moneda_cambio_min == "b":
    print("Vas a cambiar de Yen a Libra")
    cantidad = float(input("Introduzca la cantidad de Yenes que desea convertir: "))
    print("La cantidad de Dolares es: ", cantidad * 0.0067)




