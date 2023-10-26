# Importamos la biblioteca matplotlib.pyplot con el alias plt.
# Esta biblioteca se utiliza para crear visualizaciones estáticas, animadas e interactivas en Python.
import matplotlib.pyplot as plt

# Definimos la función generate_bar_chart para generar un gráfico de barras.
def generate_bar_chart():
    # Definimos las etiquetas para las barras en el gráfico.
    labels = ['A', 'B', 'C']
    
    # Definimos los valores correspondientes a cada barra en el gráfico.
    values = [200, 34, 120]
    
    # Creamos una figura y un eje para nuestro gráfico utilizando plt.subplots().
    # 'fig' se refiere a la figura completa, y 'ax' se refiere al eje en el que se dibuja el gráfico.
    fig, ax = plt.subplots()
    
    # Utilizamos el método bar para generar un gráfico de barras.
    # 'labels' se utiliza para el eje X (las categorías), 'values' para el eje Y (las alturas de las barras).
    ax.bar(labels, values)
    
    # Guardamos la figura en un archivo llamado 'bar_chart.png'.
    # Esta función guarda la imagen en el disco duro.
    plt.savefig('bar_chart.png')
    
    # Cerramos la figura para liberar la memoria.
    plt.close()

# Nota: La función ha sido definida pero no ha sido llamada en este fragmento de código.
# Para ejecutar la función y generar el gráfico, deberías añadir 'generate_bar_chart()' al final del script.
