# Importamos la biblioteca matplotlib.pyplot con el alias plt.
# Esta biblioteca se utiliza para crear visualizaciones estáticas, animadas e interactivas en Python.
import matplotlib.pyplot as plt

# Definimos la función generate_pie_chart para generar un gráfico de pastel (tarta).
def generate_line_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]
    
    fig, ax = plt.subplots()
    ax.plot(labels, values, marker='o')
    
    plt.savefig('line_chart.png')
    plt.close()
