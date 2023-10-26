# Importamos la biblioteca matplotlib.pyplot con el alias plt.
# matplotlib.pyplot es una colección de funciones de estilo de comando que hacen que matplotlib funcione como MATLAB.
# Cada función pyplot realiza algún cambio en una figura: crea una figura, crea un área de trazado en una figura,
# dibuja algunas líneas en un área de trazado, decora la trama con etiquetas, etc.
import matplotlib.pyplot as plt

# Importamos la biblioteca numpy con el alias np.
# numpy es una biblioteca para el lenguaje de programación Python, que añade soporte para vectores y matrices,
# constituyendo una biblioteca de funciones matemáticas de alto nivel para operar con estos datos.
import numpy as np

# Definimos la función generate_histogram que no toma ningún argumento.
def generate_histogram():
    # Creando una lista de 354 elementos donde 'A' se repite 200 veces, 'B' se repite 34 veces y 'C' se repite 120 veces.
    values = np.repeat(['A', 'B', 'C'], [200, 34, 120])
    
    # Creando una figura y un conjunto de subgráficos.
    # 'fig' se refiere a la figura completa, y 'ax' se refiere al eje en el que se dibuja el gráfico.
    fig, ax = plt.subplots()
    
    # Dibujamos un histograma. 
    # Los valores son los datos a representar, bins son los bordes de los bins o las divisiones que queremos, 
    # align es la alineación de los bins y rwidth es la anchura relativa de los bins.
    # En este caso estamos dividiendo los datos en 3 bins representando las letras 'A', 'B' y 'C'.
    ax.hist(values, bins=[0, 1, 2, 3], align='left', rwidth=0.8)
    
    # Establecemos las posiciones de las marcas en el eje X.
    ax.set_xticks([0.5, 1.5, 2.5])
    
    # Establecemos las etiquetas para las marcas en el eje X.
    ax.set_xticklabels(['A', 'B', 'C'])
    
    # Guardamos la figura en un archivo llamado 'histogram.png'.
    # Esta función guarda la imagen en el disco duro.
    plt.savefig('histogram.png')
    
    # Cerramos la figura para liberar la memoria.
    plt.close()

# Nota: Al igual que en el ejemplo anterior, la función ha sido definida pero no ha sido llamada en este fragmento de código.
# Para ejecutar la función y generar el histograma, deberías añadir 'generate_histogram()' al final del script.
