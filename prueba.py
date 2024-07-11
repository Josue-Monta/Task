#Calculadora cientifica
#Nikolai Panchi Josue Monta
#Importamos librerias
import tkinter
import sympy as sym
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

#Empezamos a escribir el codigo
ventana = tkinter.Tk() #Creamos la ventana
ventana.title ('Calculadora Parrillona') #Nombre de la calculadora
ventana.geometry("800x600")
ventana.resizable(False,False) #Esto nos servira para que no se pueda cambiar el tamaño de la ventana
ventana.configure(background='gray20')#fondo
operador = '' #vamos a necesitar una variable
texto_pantalla = tkinter.StringVar() #Con esto creamos las variables de las entradas de texto
pant = tkinter.StringVar()
pant2 = tkinter.StringVar()

#Vamos a usar la pantalla
pantalla = tkinter.Entry(ventana,font=('arial',20), width=23, borderwidth=5, textvariable=texto_pantalla, justify=tkinter.RIGHT)
pantalla.place (x=25, y=25)

pantalla2 = tkinter.Entry(ventana, font=('arial', 20),textvariable=pant, width=24, borderwidth=None)
pantalla2.place (x= 410, y=335, relheight=0.26)

pantalla3 = tkinter.Entry(ventana, width=60, borderwidth=None)
pantalla3.place (x=410, y=25, relheight=0.5)

pantalla4 = tkinter.Entry(ventana, font=('arial', 20),textvariable=pant2, width=24, borderwidth=1)
pantalla4.place (x= 410, y=335, relheight=None)

#Ahora definiremos el codigo para las funciones
i = 0
def AC(): #Esta funcion sirve para borrar el codigo
    global operador
    operador = ''
    texto_pantalla.set('')#Dejamos la pantalla vacia
    pant.set('')
    pant2.set('')

    figura = plt.figure(figsize=(4,3),dpi=100)#Se define las dimensiones de la figura y tamanos
    canvas = FigureCanvasTkAgg(figura, master=ventana) #Se define el area de dibujo
    canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455, relheight=0.44)
    barra_tareas = NavigationToolbar2Tk(canvas, ventana) #Se agrega una barra de herramientas para mejorar graficas
    barra_tareas.place(x=410,y=290, relwidth=0.455)
    canvas.get_tk_widget().place(x=410,y=25,relwidth=0.455)

    plt.clf() #Borrar contenido de la grafica 


def click(n): #Funcion para que aparezca en pantalla con los botones
    global i #Para usar la variable en cualquier parte del codigo
    pantalla.insert(i,n) 
    i+=1 #Los caracteres se van sumando para que no se borren

def calcular_trigonometrica(trig_func, angle_in_degrees):
    try:
        if trig_func == 'sin':
            resultado = np.sin(np.deg2rad(angle_in_degrees))
        elif trig_func == 'cos':
            resultado = np.cos(np.deg2rad(angle_in_degrees))
        elif trig_func == 'tan':
            resultado = np.tan(np.deg2rad(angle_in_degrees))
        else:
            resultado = None
        resultado = round(resultado, 10)
    except:
        resultado = None
    return resultado

def operaciones(b): #Funcion para resolver operaciones aritmeticas
    global i
    if b in ['sin', 'cos', 'tan']:  # Verifica si es una función trigonométrica
        pantalla.insert(i, b + '(')  # Inserta la función con paréntesis de apertura
        i += len(b) + 1  # Incrementa el índice
    elif b in 'sqrt':
        pantalla.insert(i,b+ '(')
        i += len(b) + 1
    else:
        pantalla.insert(i, b)  # Inserta el número o símbolo normalmente
        i += 1  # Incrementa el índice


def CDF(): #Funcion para visualizar las raices
    pant.set("")
    pant2.set("")
    mensaje='Las raices son: '
    pantalla4.insert(0, mensaje)
    cdf = pantalla.get()
    cdf1 = sym.sympify(cdf)
    t1 = sym.roots(cdf1, multiple=True) #Se usa un metodo para sacar los valores de las raices

    raiz = t1[0]
    rd = (raiz).evalf(5) #Se muestran los valores en decimales
    pantalla2.insert(0,rd)

def DEL(): #Funcion para borrar caracter por caracter
    p= pantalla.get () #contenido de pantalla
    if len(p): #Numero de caracteres >0
        np = p[:-1] #Se elimina el ultimo elemento de la pantalla
        AC()
        pantalla.insert(0,np) #Se muestra los caracteres restantes, sin contar con el eliminado
    else:
        AC() #Se llama la funcion en caso de no tener caracteres

#==

def igual():  # Para evaluar las operaciones y presentar resultados
    estado_P = pantalla.get()
    try:
        if any(func in estado_P for func in ['sin', 'cos', 'tan']):
            func, num = estado_P.split('(')
            num = num.rstrip(')')
            resultado = calcular_trigonometrica(func.strip(), float(num))
        else:
            resultado = sym.sympify(estado_P)  # Se vuelve una expresión matemática el contenido de la pantalla
        
        AC()
        pantalla.insert(0, resultado)  # Se imprime la solución
    except:
        AC()

def aprox(): #Mostrar valores en forma decimal
        contenido = pantalla.get()
        aproximacion = (sym.sympify(contenido)).evalf(15) #Se muestran 15 decimales
        AC()
        pantalla.insert(0,aproximacion)

def grafica (): #Graficamos las funciones
    expresion = pantalla.get()
    expresion1 = sym.sympify(expresion)
    x = sym.Symbol('x') #Para usar el simbolo
    v = np.linspace (-15,15,100, endpoint=True) #Valores que tomara la funcion
    valores = []

    figura = plt.figure(figsize=(4,3), dpi=100) #Se crea la grafica
    canvas = FigureCanvasTkAgg(figura, master=ventana)
    canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455,relheight=0.44)
    barras_tareas = NavigationToolbar2Tk(canvas, ventana)
    barras_tareas.place(x=410, y=290, relwidth= 0.455)
    canvas.get_tk_widget().place(x=410,y=25,relwidth=0.455)

    for i in range(len(v)): #Estamos sacando valores para {y}
        c = ((expresion1).evalf(subs={x: v[i]})) #Se evalua la expresion y se va sustituyendo los valores 
        valores.append(c)

    figura.add_subplot(111).plot(v,valores,label='{0}'.format(expresion))
    plt.legend(loc= 'upper left')#se muestra la leyenda
    plt.grid() #Se muestra la cuadricula 
    canvas.draw() #Se muestra la grafica 

def grafica_3d():
    expresion = pantalla.get()
    expresion1 = sym.sympify(expresion)
    x, y = sym.symbols('x y')  #Define símbolos para variables x e y

    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111, projection='3d')

    X = np.linspace(-10, 10, 100) #Genera datos para la superficie 3D
    Y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(X, Y)
    Z = sym.lambdify((x, y), expresion1)(X, Y)

    ax.plot_surface(X, Y, Z, cmap='viridis')#Grafica la superficie

    ax.set_xlabel('X')
    ax.set_ylabel('Z')
    ax.set_zlabel('Y')
    ax.set_title(f'Grafica 3D de {expresion}')

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
    barra_tareas = NavigationToolbar2Tk(canvas, ventana)
    barra_tareas.place(x=410, y=290, relwidth=0.455)
    canvas.get_tk_widget().place(x=410,y=25,relwidth=0.455)
    canvas.draw()#Muestra la Grafica
    
def limites(): #Funcion para Integrales definidas

    pant.set('') #Se usa para borrar el contenido anterior
    pant2.set('')
    c=pantalla.get() #Obtener el contenido de las entradas de texto
    mensaje= 'El valor de la integral definida es :'
    pantalla4.insert(0,mensaje)
    c1=c.split(',') #Se dividen por comas(expresion, limite inferior, limite superior)
    li=c1[1]
    ls=c1[2]
    inte=c1[0]
    inte1 = sym.sympify(inte)
    res = sym.integrate(inte1,('x',li,ls)) #No se necesita la definicion de funcion igual
    pantalla2.insert(1,res) #Se muestra la solucion en pantalla solo haciendo click en el simbolo de la integral definida

def derivada(): #Funcion para derivar
    pant.set('') 
    pant2.set('')
    d = pantalla.get()
    if 'x' in d: #Se muestra la variable por la cual se va a derivar
        d1 = sym.sympify(d)
        r = sym.diff(d1,'x')
        pantalla2.insert(0,r)
        mensaje= 'La derivada es: '
        pantalla4.insert(0, mensaje)
        expresion = pantalla2.get() #Se grafica nuevamente
        expresion1 = sym.sympify(expresion)
        x = sym.Symbol('x')
        v = np.linspace(-15,15,100, endpoint=True)
        valores = []
        figura = plt.figure(figsize=(4,3),dpi=100)
        ax = figura.add_subplot(111)
        canvas = FigureCanvasTkAgg (figura, master=ventana)
        canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455, relheight=0.44)
        barras_tareas = NavigationToolbar2Tk(canvas, ventana)
        barras_tareas.place(x=410,y=290, relwidth=0.455)
        canvas.get_tk_widget().place(x=410,y=25, relwidth=0.455)

        for i in range (len(v)):
            c = ((expresion1).evalf(subs={x: v[i]}))
            valores.append(c)
        ax.clear()
        ax.plot(v,valores,label='{0}'.format(expresion))
        plt.grid()
        canvas.draw()
        expresion = pantalla.get() #Se muestra junto con la grafica de la funcion original
        expresion1 = sym.sympify(expresion)
        x = sym.Symbol('x')
        v = np.linspace(-15,15,100, endpoint=True)
        valores = []
        figura = Figure(figsize=(4,3),dpi=100)
        canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455,relheight=0.44)
        barra_tareas = NavigationToolbar2Tk(canvas,ventana)
        barra_tareas.place(x=410,y=25,relwidth=0.455)
        canvas.get_tk_widget().place(x=410,y=25, relwidth=0.455)

        for i in range(len(v)):
             c = ((expresion1).evalf(subs={x: v[i]}))
             valores.append(c)
        ax.plot(v,valores,label='{0}'.format(expresion))
        plt.legend(loc = 'upper left')
        canvas.draw()

    else: #variable de diferenciacion para y
        d1 = sym.sympify(d)
        r = sym.diff(d1,'y')
        pantalla2.insert(0,r)
        mensaje = 'La derivada es: '
        pantalla4.insert(0,mensaje)
        expresion = pantalla2.get()
        expresion1 = sym.sympify(expresion)
        c = ''
        x = sym.Symbol('y')
        v = np.linspace(-15,15,100, endpoint=True)
        valores = []
        figura = plt.figure(figsize=(4,3), dpi=100)
        ax = figura.add_subplot(111)
        canvas = FigureCanvasTkAgg(figura, master=ventana)
        canvas.get_tk_widget().place(x=410,y=25,relwidth=0.455)
        barra_tareas = NavigationToolbar2Tk(canvas, ventana)
        barra_tareas.place (x=410,y=290, relwidth=0.455)
        canvas.get_tk_widget().place(x=410,y=25,relwidth=0.455)
        for i in range(len(v)):
            c = ((expresion1).evalf(subs={x: v[i]}))
            valores.append(c)
        ax.clear()
        ax.plot(v,valores,label='{0}'.format(expresion))
        plt.grid()
        canvas.draw()
        #Grafica antigua
        expresion = pantalla.get() #Se muestra junto con la grafica de la funcion original
        expresion1 = sym.sympify(expresion)
        x = sym.Symbol('x')
        v = np.linspace(-15,15,100, endpoint=True)
        valores = []
        figura = Figure(figsize=(4,3),dpi=100)
        canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455,relheight=0.44)
        barra_tareas = NavigationToolbar2Tk(canvas,ventana)
        barra_tareas.place(x=410,y=25,relwidth=0.455)
        canvas.get_tk_widget().place(x=410,y=25, relwidth=0.455)

        for i in range(len(v)):
             c = ((expresion1).evalf(subs={x: v[i]}))
             valores.append(c)
        ax.plot(v,valores,label='{0}'.format(expresion))
        plt.legend(loc = 'upper left')
        canvas.draw()


def integralindef(): #integrar funciones
    pant.set('')
    pant2.set('')
    inte = pantalla.get()
    intel1 = sym.sympify(inte)
    res = sym.integrate(inte,('x', None, None)) #Se realiza una integracion indefinida
    pantalla2.insert (0,res)
    expresion = pantalla2.get() #se grafica
    expresion1 = sym.sympify(expresion)
    mensaje = 'La integral indefinida es: '
    pantalla4.insert(0, mensaje)
    x = sym.Symbolo('x')
    v = np.linspace(-15,15,100, endpoint=True)
    valores = []

    figura = plt.figure(figsize=(4,3), dpi=100)
    ax = figura.add.subplot(111)
    canvas = FigureCanvasTkAgg(figura, master=ventana)
    canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455, relheight=0.44)
    barra_tareas = NavigationToolbar2Tk(canvas, ventana)
    barra_tareas.place(x=410,y=290, relwidth=0.455)
    canvas.get_tk_widget().place(x=410,y=25, relwidth=0.455)


    for i in range(len(v)):
        c= ((expresion1)).evalf(subs={x: v[i]})
        valores.append(c)
    ax.clear()
    ax.plot(v, valores, label= '{0}'.format(expresion))
    plt.legend(loc='upper left')
    plt.grid()

    canvas.draw()
    expresion = pantalla.get() #Se muestra junto con la grafica de la funcion original
    expresion1 = sym.sympify(expresion)
    x = sym.Symbol('x')
    v = np.linspace(-15,15,100, endpoint=True)
    valores = []
    figura = Figure(figsize=(4,3),dpi=100)
    canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455,relheight=0.44)
    barra_tareas = NavigationToolbar2Tk(canvas,ventana)
    barra_tareas.place(x=410,y=25,relwidth=0.455)
    canvas.get_tk_widget().place(x=410,y=25, relwidth=0.455)

    for i in range(len(v)):
         c = ((expresion1).evalf(subs={x: v[i]}))
         valores.append(c)
    ax.plot(v,valores,label='{0}'.format(expresion))
    plt.legend(loc = 'upper left')
    canvas.draw()

#Creamos los botones con distintas propiedades
#Botones de la primera fila 
boton11 = tkinter.Button(ventana, text='x', bd=10, bg='darkgray', width=8, height=1, command=lambda:operaciones('x')).place(x=25, y=100)
boton12 = tkinter.Button(ventana, text='y', bd=10, bg='darkgray', width=8, height=1, command=lambda:operaciones('y')).place(x=117, y=100)
boton13 = tkinter.Button(ventana, text='x^', bd=10, bg='darkgray', width=8, height=1, command=lambda:operaciones('**')).place(x=210, y=100)
boton14 = tkinter.Button(ventana, text='sin', bd=10, bg='darkgray', width=8, height=1, command=lambda:operaciones('sin')).place(x=301, y=100)

#Botones de la segunda fila 
boton21 = tkinter.Button(ventana, text='π', bd=10, bg='darkgray', width=8, height=1, command=lambda:click('pi')).place(x=25, y=150)
boton22 = tkinter.Button(ventana, text='e', bd=10, bg='darkgray', width=8, height=1, command=lambda:operaciones('E')).place(x=117, y=150)
boton23 = tkinter.Button(ventana, text='√', bd=10, bg='darkgray', width=8, height=1, command=lambda:operaciones('sqrt')).place(x=209, y=150)
boton24 = tkinter.Button(ventana, text='cos', bd=10, bg='darkgray', width=8, height=1, command=lambda:operaciones('cos')).place(x=301, y=150)

#Botones de la tercera fila
boton31 = tkinter.Button(ventana, text=',', bd=10, bg='darkgray', width=8, height=1, command=lambda:click(',')).place(x=25, y=200)
boton32 = tkinter.Button(ventana, text='(', bd=10, bg='darkgray', width=8, height=1, command=lambda:operaciones('(')).place(x=117, y=200)
boton33 = tkinter.Button(ventana, text=')', bd=10, bg='darkgray', width=8, height=1, command=lambda:operaciones(')')).place(x=209, y=200)
boton34 = tkinter.Button(ventana, text='tan', bd=10, bg='darkgray', width=8, height=1, command=lambda:operaciones('tan')).place(x=301, y=200)

#Botones de la segunda cuadricula
#Botones de la cuarta fila
boton41 = tkinter.Button(ventana, text='7', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(7)).place(x=25, y=300)
boton42 = tkinter.Button(ventana, text='8', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(8)).place(x=97, y=300)
boton43 = tkinter.Button(ventana, text='9', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(9)).place(x=169, y=300)
boton44 = tkinter.Button(ventana, text='DEL', bd=10, bg='tomato', width=6, height=2, command=lambda:DEL()).place(x=241, y=300)
boton45 = tkinter.Button(ventana, text='AC', bd=10, bg='tomato', width=6, height=2, command=lambda:AC()).place(x=313, y=300)

#Botones de la quinta fila
boton51 = tkinter.Button(ventana, text='4', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(4)).place(x=25, y=370)
boton52 = tkinter.Button(ventana, text='5', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(5)).place(x=97, y=370)
boton53 = tkinter.Button(ventana, text='6', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(6)).place(x=169, y=370)
boton54 = tkinter.Button(ventana, text='x', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('*')).place(x=241, y=370)
boton55 = tkinter.Button(ventana, text='÷', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('/')).place(x=313, y=370)

#Botones de la sexta fila
boton61 = tkinter.Button(ventana, text='1', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(1)).place(x=25, y=440)
boton62 = tkinter.Button(ventana, text='2', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(2)).place(x=97, y=440)
boton63 = tkinter.Button(ventana, text='3', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(3)).place(x=169, y=440)
boton64 = tkinter.Button(ventana, text='+', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('+')).place(x=241, y=440)
boton65 = tkinter.Button(ventana, text='-', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('-')).place(x=313, y=440)

#Botones de la septima fila
boton71 = tkinter.Button(ventana, text='0', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(0)).place(x=25, y=510)
boton72 = tkinter.Button(ventana, text='.', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('.')).place(x=97, y=510)
boton73 = tkinter.Button(ventana, text='GRAF', bd=10, bg='darkgray', width=6, height=2, command=lambda:grafica()).place(x=169, y=510)
boton74 = tkinter.Button(ventana, text='APROX', bd=10, bg='darkgray', width=6, height=2, command=lambda:aprox()).place(x=241, y=510)
boton75 = tkinter.Button(ventana, text='=', bd=10, bg='darkgray', width=6, height=2, command=lambda:igual()).place(x=313, y=510)

#Botones de calculo
#Botones segunda columna
boton0 = tkinter.Button(ventana, text='3D', bd=10, bg='darkgray', width=5, height=3, command=lambda: grafica_3d()).place(x=410, y=510)

boton1 = tkinter.Button(ventana, text='f/(x)', bd=10, bg='darkgray',font=('arial',20), width=3, height=1, command=lambda:derivada()).place(x=475, y=510)

boton2 = tkinter.Button(ventana, text='∫', bd=10, bg='darkgray',font=('arial',20), width=2, height=1, command=lambda:integralindef()).place(x=555, y=510)

boton3 = tkinter.Button(ventana, text='∫ₐᵇ', bd=10, bg='darkgray',font=('arial',20), width=2, height=1, command=lambda:limites()).place(x=618, y=510)

boton4 = tkinter.Button(ventana, text='Funciones', bd=10, bg='darkgray', width=10, height=3, command=lambda:CDF()).place(x=680, y=510)
ventana.mainloop()
