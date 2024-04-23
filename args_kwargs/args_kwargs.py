
#####
#*args: Es una lista para cuando no sabes cuantos parametros tienen las variables 
def escribir_nombres(*args): 
    print ("    Inicio")
    for i in range(len(args)):
        print(args[i])
escribir_nombres("Luciana",
                 "Sosa",
                 "Rosario",
                "Juñent")
escribir_nombres("Rocio ", 
                 "Goulu")

#**kwargs: keyword arguments: Puede llamarse de cualquier manera. Sirve para cuando no sabes cuantos argumentos tiene la función con nombre de parametros

def escribir_nombres(**kwargs): 
    print ("    Inicio")
    print(kwargs)
escribir_nombres(primer_nombre = "Luciana",
                 primer_apellido ="Sosa",
                 segundo_nombre ="Guadalupe",
                segundo_apellido ="Carmona")
escribir_nombres(primer_nombre="Rosario", 
                 primer_apellido="Juñent")

#####items. ES una forma de crear una lista de key y su valor asociado con un diccionario que le damos en este caso es kwargs
def escribir_nombres1(**kwargs):
    print ("    Inicio")
    print (kwargs.items())
escribir_nombres(primer_nombre = "Luciana",
                 primer_apellido ="Sosa",
                 segundo_nombre ="Guadalupe",
                segundo_apellido ="Sosa")
escribir_nombres(primer_nombre="Rosario", 
                 primer_apellido="Juñent")
####### ACA USAMOS Las dos juntas para probar si funciona y como nos daria el resultado
def escribir_nombres1(*args,**kwargs):
    print ("    Inicio")
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("key",key,"valor", value)
    
escribir_nombres1("Ludmila", 
                primer_nombre = "Luciana",
                primer_apellido ="Sosa",
                segundo_nombre ="Guadalupe",
                segundo_apellido ="Carmona")
escribir_nombres1("Liz", 
                primer_nombre="Rosario", 
                primer_apellido="Juñent")