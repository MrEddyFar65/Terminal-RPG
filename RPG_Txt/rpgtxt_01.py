"""Un juego RPG basado en Texto en Terminal
con algunos toques haciendo alucion a la cultura Mexicana
Un "Dungeons and Tacos" :p"""

import subprocess 
#Algunas variables booleanas globales
run = True
menu = True
juego= False
reglas = False
#i = 0

Vida = 50
Atk = 4

def clear():
    subprocess.run("clear")

def draw():
    print("Xx------------------xX")

def bottom():
    print("0o--------------------------------------------------o0")

#Funcion de Guardado del juego
def guardar():
    list = [
        nombre,
        str(Vida),
        str(Atk)
    ]

    f = open("load.txt", "w")
    for i in list:
        f.write(i + "\n")
    f.close()


#El juego
while run:
#Pantalla principal del juego
    while menu:
        clear() 
        draw()
        print("1, Nuevo Juego")
        print("2, Cargar Juego")
        print("3, Reglas")
        print("4, Quitar Juego")
        draw()
        #i+=1
    #i += 1

    #Elecciones pantalla principal 
    #Eficientar estos ELSE e IF. como los detesto
        if reglas:
            clear()
            bottom()
            print("Soy el diosito creador de este juegazo parce malparido")
            bottom()
            reglas = False
            eleccion = " "
            eleccion =input("> ")
        else:
            eleccion = input("# ")

        if eleccion == "1":
            clear()
            nombre = input("Ingresa tu nickname: ")
            menu= False
            juego = True 

        elif eleccion == "2":
            f = open("load.txt", "r")
            load_list =  f.readlines()
            nombre = load_list[0][:-1]
            Vida = load_list[1][:-1]
            Atk = load_list[2][:-1]
            clear()
            print("La aventura continua "+ nombre +" !")
            input("> ")
            menu = False
            juego = True
            

        elif eleccion == "3":
            reglas = True
        elif eleccion == "4":
            quit()


    while juego:
        
        guardar()

        clear()
        draw()
        print("presiona '0' para continuar")
        draw()
        dest= input("# ")
        
        if dest == "0":
            juego = False
            menu = True
            guardar()


