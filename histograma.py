import matplotlib.pyplot as plt
import numpy as np

def generate_histogram():
    values = np.repeat(['A', 'B', 'C'], [200, 34, 120])
    
    fig, ax = plt.subplots()
    ax.hist(values, bins=[0, 1, 2, 3], align='left', rwidth=0.8)
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(['A', 'B', 'C'])
    
    plt.savefig('histogram.png')
    plt.close()
