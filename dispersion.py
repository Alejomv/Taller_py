# Importamos la biblioteca matplotlib.pyplot con el alias plt.
# Esta biblioteca se utiliza para crear visualizaciones estáticas, animadas e interactivas en Python.
import matplotlib.pyplot as plt

# Definimos la función generate_scatter_plot para generar un gráfico de dispersión (scatter plot).
def generate_scatter_plot():
    # Definimos las etiquetas para los puntos en el eje X del gráfico.
    labels = ['A', 'B', 'C']
    
    # Definimos los valores correspondientes a cada etiqueta en el eje X.
    values = [200, 34, 120]
    
    # Creamos una figura y un eje para nuestro gráfico utilizando plt.subplots().
    # 'fig' se refiere a la figura completa, y 'ax' se refiere al eje en el que se dibuja el gráfico.
    fig, ax = plt.subplots()
    
    # Utilizamos el método scatter para generar un gráfico de dispersión.
    # 'labels' se utiliza para el eje X, 'values' para el eje Y.
    ax.scatter(labels, values)
    
    # Guardamos la figura en un archivo llamado 'scatter_plot.png'.
    # Esta función guarda la imagen en el disco duro.
    plt.savefig('scatter_plot.png')
    
    # Cerramos la figura para liberar la memoria.
    plt.close()

# Nota: La función ha sido definida pero no ha sido llamada en este fragmento de código.
# Para ejecutar la función y generar el gráfico, deberías añadir 'generate_scatter_plot()' al final del script.
