# Importamos el módulo 'charts'.
# Este módulo debería contener la definición de la función 'generate_pie_chart'.
import lineas

# Definimos la función 'run' que ejecutará la función 'generate_pie_chart' del módulo 'charts'.
def run():
    lineas.generate_line_chart()

# Este bloque de código asegura que la función 'run' solo se ejecutará si este script se ejecuta como programa principal.
# Si este script se importa como un módulo en otro script, la función 'run' no se ejecutará automáticamente.
if __name__ == '__main__':
    run()

# Nota: Para que este script funcione correctamente, debes tener un módulo llamado 'charts'
# que contenga una función llamada 'generate_pie_chart'.
# Este módulo debería estar en el mismo directorio que este script, o en una ubicación que Python pueda encontrar.
