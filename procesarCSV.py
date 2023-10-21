# pip install pandas
#pip install openpyxl
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("resultados.csv", sep=',')

# Dividir la columna 'URL FROM,Enlace con .HTML,Texto del enlace' en tres columnas
#df[['URL FROM', 'Enlace con .HTML', 'Texto del enlace']] = df['URL FROM,Enlace con .HTML,Texto del enlace'].str.split(',', 2, expand=True)

# Guardar el resultado en un nuevo archivo CSV
df.to_csv("resultados_separados.csv", index=False)

print("Resultados exportados a resultados_separados.csv")
print(df)


