# Importamos la biblioteca matplotlib.pyplot con el alias plt.
# Esta biblioteca se utiliza para crear visualizaciones estáticas, animadas e interactivas en Python.
import matplotlib.pyplot as plt

# Definimos la función generate_pie_chart para generar un gráfico de pastel (tarta).
def generate_pie_chart():
    # Especificamos las etiquetas para cada segmento del gráfico de pastel.
    labels = ['A', 'B', 'C']
    
    # Asignamos los valores numéricos que corresponden a cada etiqueta.
    # En este caso, 'A' corresponde a 200, 'B' a 34 y 'C' a 120.
    values = [200, 34, 120]

    # Creamos una figura y un eje utilizando subplots. 
    # Esta es una manera de preparar el espacio para el gráfico.
    fig, ax = plt.subplots()
    
    # Generamos el gráfico de pastel utilizando el método pie.
    # Le pasamos los valores y las etiquetas definidos anteriormente.
    ax.pie(values, labels=labels)
    
    # Guardamos la figura en un archivo con formato PNG llamado 'pie.png'.
    plt.savefig('torta.png')
    
    # Cerramos la figura para liberar memoria.
    plt.close()

# Nota: Este script define la función generate_pie_chart, pero no la ejecuta.
# Para visualizar el gráfico, debes llamar a la función después de definirla:
# generate_pie_chart()
