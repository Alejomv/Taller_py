
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Simulación de datos de temperaturas (en la vida real, obtendrías estos datos de una API o una base de datos)
data = {
    "fecha": ["2023-01-01", "2023-01-02", "2023-01-03"],
    "temperatura": [22, 24, 23]
}

# Convertir los datos a un DataFrame de Pandas
df = pd.DataFrame(data)

# Hacer un gráfico de las temperaturas históricas
plt.plot(df['fecha'], df['temperatura'])
plt.title('Temperaturas históricas')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.show()
