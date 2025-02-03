import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("movies.csv", encoding="latin1")

# Mostrar las 10 peliculas con más presupuesto
df_sorted = df.sort_values(by="budget", ascending=False)
print("10 Peliculas con mayor presupuesto")
print(df_sorted[["title", "budget"]].head(10)) 

#Mostrar las 10 peliculas con más ingresos
highest_revenue = df.sort_values(by="revenue", ascending=False)
print("10 Peliculas con más ingresos")
print(highest_revenue[["title", "revenue"]].head(10)) 

#Pelicula con más votos 
df_votes = df.loc[df["voteCount"].idxmax()]
print("Pelicula con más votos")
print(df_votes[["title", "voteCount"]]) 

#Cantidad de peliculas cada año y en qué año se hicieron más peliculas 
# Asegurar que releaseDate es de tipo fecha
df["releaseDate"] = pd.to_datetime(df["releaseDate"], errors="coerce")
# Extraer el año
df["releaseYear"] = df["releaseDate"].dt.year 

df_date = df["releaseYear"].value_counts().sort_index()
print("Cantidad de peliculas cada año", df_date)

movies_year = df_date.idxmax()  
movies_count = df_date.max()  
print(f"año con más películas fue {movies_year} con {movies_count} películas.")

# Graficar un gráfico de barras
plt.figure(figsize=(10, 5))  # Ajustar tamaño
plt.bar(df_date.index, df_date.values, color='skyblue')

# Agregar título y etiquetas
plt.xlabel('Año')
plt.ylabel('Cantidad de películas')
plt.title('Cantidad de películas por año')

# Mejorar visualización
plt.xticks(rotation=45)  # Rotar etiquetas del eje X si hay muchos años

# Mostrar el gráfico
plt.show()


