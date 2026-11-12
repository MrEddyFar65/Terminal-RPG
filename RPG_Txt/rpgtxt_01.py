"""Un juego RPG basado en Texto en Terminal
con algunos toques haciendo alucion a la cultura Mexicana
Un "Dungeons and Tacos" :p"""

import subprocess 
#Algunas variables booleanas globales
run = True
menu = True
juego= False
reglas = False
key = False 

#i = 0

Vida = 50
Atk = 4
pot = 1
elix = 0
oro = 0
x=0
y=0

        #  x = 0      x = 1     x = 2       x = 3      x = 4      x = 5       x = 6
mapa = [["llanura", "llanura", "llanura", "llanura",  "bosque",  "montañas", "cueva"],   # y = 0
        ["bosque",  "bosque",  "bosque",  "bosque",   "bosque",  "colina",   "montaña"], # y = 1
        ["bosque",  "campo",   "puente",  "llanura",  "colina",  "bosque",   "colina"],  # y = 2
        ["llanura", "campaña", "pueblo",  "alcaldia", "llanura", "colina",   "montaña"], # y = 3
        ["llanura", "campo",   "campo",   "llanura",  "colina",  "montaña",  "montaña"]  # y = 4      
        ]

y_len = len(mapa)-1
x_len = len(mapa[0])-1


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
        str(Atk),
        str(pot),
        str(elix),
        str(oro),
        str(x),
        str(y),
        str(key)
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
            #eleccion =input("> ")
            input("> ")
        else:
            eleccion = input("# ")

        if eleccion == "1":
            clear()
            nombre = input("Ingresa tu nickname: ")
            menu= False
            juego = True 

        elif eleccion == "2":
            try:
                f = open("load.txt", "r")
                load_list =  f.readlines()

                if len(load_list) == 9 :
                    nombre = load_list[0][:-1]
                    Vida = int(load_list[1][:-1])
                    Atk = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    clear()
                    print("La aventura continua "+ nombre +"!")
                    print("HP = ", Vida)
                    input("> ")
                    menu = False
                    juego = True
                else: 
                    print("La partida no se guardo adecuadamente")
                    print("Corrupt File!")
                    input("> ")
            except OSError:
                print("No hay partidas guardadas")
                print("> ")

        elif eleccion == "3":
            reglas = True
        elif eleccion == "4":
            clear()
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


