# Importamos la biblioteca matplotlib.pyplot con el alias plt.
# Esta biblioteca se utiliza para crear visualizaciones estáticas, animadas e interactivas en Python.
import matplotlib.pyplot as plt

# Definimos la función generate_pie_chart para generar un gráfico de pastel (tarta).
def generate_box_plot():
    values = [[200] * 200 + [34] * 34 + [120] * 120]
    
    fig, ax = plt.subplots()
    ax.boxplot(values)
    
    plt.savefig('box_plot.png')
    plt.close()
