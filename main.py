#Actividad Listas
opVolverMenu = True
opRuns = False
#Atributos globales
numCliente = 0
optionMenu = 0
#Atributos del cliente
clienteNombre = ""
clienteRut = ""
clienteDireccion = ""
clienteComuna = ""
clienteCorreo = ""
clienteEdad = 0
clienteGenero = ""
clienteCelular = ""
clienteTipo = ""
clienteSubscripciones = "Default"
#Listas
tipoCliente = ["Premium","Gold","Silver"]
clientes = []

#Registar Cliente
def menu():
  opValida = False
  while opValida == False:
   optionMenu = int(input("Elija una opcion : \n 1. Registrar Cliente. \n 2. Suscripción. \n 3. Consultar Datos Cliente. \n 4. Salir. \n Opcion :   "))
   if optionMenu == 1 or optionMenu == 2 or optionMenu == 3 or optionMenu == 4:
      opValida = True
   else:
     opValida = False
     print("Intentar Nuevamente")
    
  
  return optionMenu

loop = 1
while loop == 1:
  optionMenu = menu()
  print(optionMenu)
  #Opciones del Menu
  if optionMenu == 1:
          #Registrar un cliente
          print("Registar un Cliente")
          print("Ingresar Datos del Cliente :")
          clienteNombre = input("Ingresar Nombre del cliente : \n")
          opRut = False
          while opRut == False:
            clienteRut = int(input("Ingresar Rut del cliente : \n"))
            if clienteRut > 4000000 and clienteRut < 99999999:
              opRut = True
            else:
              opRut= False
              print("Porfavor Ingresar Informacion Correcta!")
          clienteDireccion = input("Ingresar Direccion del cliente : \n")
          clienteComuna = input("Ingresar Comuna del cliente : \n")
          clienteCorreo = input("Ingresar Correo del cliente : \n")
          opEdad = False
          while opEdad == False:
            clienteEdad = int(input("Ingresar Edad del cliente : \n"))
            if clienteEdad > 100 or clienteEdad < 0:
              opEdad = False
              print("Ingrese un valor correcto e intente nuevamente !")
            elif clienteEdad > 0 and clienteEdad < 101:
              opEdad = True
            else :
              print("Intente Nuevamente , solo numeros")
          opGenero = False
          while opGenero == False :
            clienteGenero = input("Ingresar Genero del cliente : (M O F) \n")
            if clienteGenero == "M" or clienteGenero== "m":
              clienteGenero = "Masculino"
              opGenero = True
            elif clienteGenero == "F" or clienteGenero == "f":
              clienteGenero = "Femenino"
              opGenero = True
            else:
              print("Ingrese un valor correcto e intente nuevamente !")
              opGenero = False
              
          
          clienteCelular = input("Ingresar celular del cliente : \n")
          opTipocliente = False
          while opTipocliente == False:
            intipocliente = int(input("Elija un tipo de cliente , 1 para Premium , 2 para Gold y 3 para Silver : \n"))
            if intipocliente == 1:
              clienteTipo = tipoCliente[0]
              opTipocliente = True
            elif intipocliente == 2:
              clienteTipo = tipoCliente[1]
              opTipocliente = True
            elif intipocliente == 3:
              clienteTipo = tipoCliente[2]
              opTipocliente = True
            else:
              print("Elija el tipo correctamente e intente de nuevo!!")
              opTipocliente = False

          #Registrar los datos
            clientes.append([clienteNombre,clienteRut,clienteDireccion, clienteComuna, clienteCorreo, clienteEdad, clienteGenero, clienteCelular, clienteTipo, clienteSubscripciones])
            
          
      
  elif optionMenu == 2:
        print("Subscripcion")
    #Consultar Datos Cliente
  elif optionMenu == 3:
      print("Consultar Datos Cliente")
      for i in clientes:
        print(i)
    #Salir
  elif optionMenu == 4:
      print("Salir")
      loop = 0
  