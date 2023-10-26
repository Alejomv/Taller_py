# Importamos la biblioteca matplotlib.pyplot con el alias plt.
# Esta biblioteca se utiliza para crear visualizaciones estáticas, animadas e interactivas en Python.
import matplotlib.pyplot as plt

def generate_scatter_plot():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]
    
    fig, ax = plt.subplots()
    ax.scatter(labels, values)
    
    plt.savefig('scatter_plot.png')
    plt.close()

