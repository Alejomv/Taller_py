# Importamos la biblioteca matplotlib.pyplot con el alias plt.
# Esta biblioteca se utiliza para crear visualizaciones estáticas, animadas e interactivas en Python.
import matplotlib.pyplot as plt

# Definimos la función generate_pie_chart para generar un gráfico de pastel (tarta).
def generate_bar_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]
    
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    
    plt.savefig('bar_chart.png')
    plt.close()