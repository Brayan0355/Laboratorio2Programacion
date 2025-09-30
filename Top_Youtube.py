import pandas as pd
import numpy as np

# 1. Cargar el dataset
df = pd.read_csv("youtube-top-100-songs-2025.csv")

# 2. Resumen estadístico
print("=== Resumen estadístico (describe) ===")
print(df.describe(include="all"))

# 3. Tipos de datos
print("\n=== Tipos de datos ===")
print(df.dtypes)

# 4. Primeros y últimos registros
print("\n=== Primeros registros (head) ===")
print(df.head())

print("\n=== Últimos registros (tail) ===")
print(df.tail())

# 5. Ordenar resultados por una columna (ejemplo: vistas o likes)
#  Ajusta el nombre de la columna según como venga en tu CSV
if "views" in df.columns:
    print("\n=== Canciones ordenadas por vistas (descendente) ===")
    print(df.sort_values("views", ascending=False).head(10))

if "likes" in df.columns:
    print("\n=== Canciones ordenadas por likes (descendente) ===")
    print(df.sort_values("likes", ascending=False).head(10))

# 6. Medidas estadísticas sobre una columna numérica
#  Cambia "views" por cualquier columna numérica de tu dataset
if "views" in df.columns:
    views = df["views"].dropna()
    print("\n=== Medidas estadísticas sobre 'views' ===")
    print("Media:", np.mean(views))
    print("Mediana:", np.median(views))
    print("Desviación estándar:", np.std(views))

