clientes={}
crear=''
check=0

def registro(usuario, contrasena):
    try:
        clientes[usuario]=contrasena
        return usuario
    except:
      print('An exception occurred')
      
      
def login(usuario, contrasena):
    try:
        for k in clientes.keys():
            if k == usuario:
                if clientes[usuario]==contrasena:
                    return f"Bienvenido {usuario} !"
                else:
                    return "La contraseña ingresada no es correcta"
    except:
            print('An exception occurred')
            
            
def update(usuario):
    try:
        newPass=input("Ingrese su nueva contraseña: ")
        for k in clientes.keys():
            if k == usuario:
                clientes[usuario]=newPass
                return "Se ha guardado su nueva contraseña"
    except:
      print('An exception occurred')
    

def verBase():
    try:
        if len(clientes)<1:
            print("Aun no se registro ningun cliente")
            return
        else:
            for k in clientes.items():
                print (k)
    except:
            print('An exception occurred')

      
while crear!='fin':
    crear=input("Para finalizar ejercicio ingresa la palabra 'fin' ")
    if crear=='fin':
        break
    else:
        print("Menu:\n Registro\n Login\n Base de Datos\n")
        variable=input("¡Hola!, ¿quieres registrarte, loguearte o ver la base de datos?, presiona 'r' para Registro,  'l' para Login o 'm' para ver la base\n")
        if variable.capitalize()=="R":
            usuario=input("Ingrese su nombre: ")
            password=input("Ingrese contraseña: ")
            resultado=registro(usuario, password)
            print(f"Gracias por registrarte {resultado}!")
        elif variable.capitalize()=="L":
            usuario=input("Ingrese su nombre: ")
            password=input("Ingrese contraseña: ")
            resultado=login(usuario, password)
            if resultado==None:
                print("El usuario ingresado no existe")
            else:
                print(resultado)    
            while resultado == "La contraseña ingresada no es correcta":
                check+=1
                password=input("Por favor ingrese nuevamente la contraseña: ")
                resultado=login(usuario, password)
                print(resultado)
                if check>=3:
                    cambio=input("Necesita cambiar su contraseña? S/N ")
                    if cambio.capitalize()=="S":
                        check=0
                        print(update(usuario))
        elif variable.capitalize()=="M":
                verBase()
                    

                             

      