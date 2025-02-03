import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("movies.csv", encoding="latin1")

#Genero principal de las 20 peliculas más recientes

# Asegurar que releaseDate sea de tipo fecha
df["releaseDate"] = pd.to_datetime(df["releaseDate"], errors="coerce")

# Ordenar por fecha de lanzamiento (de más reciente a más antigua)
df_recent = df.sort_values(by="releaseDate", ascending=False).head(20)

# Extraer el primer género de cada película 
df_recent["main_genre"] = df_recent["genres"].str.split("|").str[0]

print("Género principal de las 20 películas más recientes:")
print(df_recent[["title", "main_genre"]])

#Genero principal que predomina en el conjunto de datos 
# Dividir la columna "genres" en listas y contar frecuencia de cada género
df_principal_genre = df["genres"].dropna().str.split("|").explode()  # Separa múltiples géneros y los cuenta individualmente
genre_counts = df_principal_genre.value_counts()

# Graficar
plt.figure(figsize=(12, 6))
genre_counts.plot(kind="bar", color="green")
plt.title("Género principal más frecuente en el conjunto de datos")
plt.xlabel("Género")
plt.ylabel("Cantidad de películas")
plt.xticks(rotation=45)
plt.show()

# Mostrar el género más común
common_genre = genre_counts.idxmax()
print(f"El género principal más común en el conjunto de datos es: {common_genre}")

#Genero al que pertenecen las peliculas más largas 
# Ordenar por duración y tomar las más largas
df_largo = df.sort_values(by="runtime", ascending=False)

# Extraer el primer género de cada película
df_largo["main_genre"] = df_largo["genres"].str.split("|").str[0]

print("Género principal de las películas más largas:")
print(df_largo[["title", "runtime", "main_genre"]])

#Directores que hicieron las 20 peliculas mejor calificadas 
df_director = df.sort_values(by="voteAvg", ascending=False).head(20)

# Verificar si hay valores nulos en "director" y eliminarlos si es necesario
df_director = df_director.dropna(subset=["director"])

print("Directores que hicieron las 20 peliculas mejor calificadas:")
print(df_director[["director", "title", "voteAvg"]])

# Género principal de películas que obtuvieron mayor ganancia
# Asegurar que 'genres' y 'revenue' no tengan valores nulos
df = df.dropna(subset=["genres"])
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce").fillna(0)

# Extraer el primer género de cada película en TODO df
df["main_genre"] = df["genres"].astype(str).str.split("|").str[0]

# Agrupar por género principal y sumar las ganancias
genre_revenue = df.groupby("main_genre")["revenue"].sum().sort_values(ascending=False)

# Verificar si hay datos suficientes
if genre_revenue.empty:
    print("No hay datos suficientes para calcular el género con mayores ganancias.")
else:
    top_genre = genre_revenue.idxmax()
    top_revenue = genre_revenue.max()
    print(f"El género principal con mayores ganancias es '{top_genre}' con un total de ${top_revenue:,.2f} en ingresos.")

#Asociación de los meses de lanzamiento con los ingresos 
# Asegurar que 'releaseDate' es de tipo fecha
df["releaseDate"] = pd.to_datetime(df["releaseDate"], errors="coerce")

# Crear una nueva columna con el mes de lanzamiento
df["releaseMonth"] = df["releaseDate"].dt.month

# Agrupar por mes y sumar los ingresos
mes_revenue = df.groupby("releaseMonth")["revenue"].sum()

# Ordenar los meses correctamente (de enero a diciembre)
mes_revenue = mes_revenue.reindex(range(1, 13), fill_value=0)

print("Ingresos totales por mes de lanzamiento:")
print(mes_revenue)

#Graficar los ingresos mensuales
plt.figure(figsize=(10, 5))
mes_revenue.plot(kind="bar", color="pink")

# Mejorar el formato del gráfico
plt.xticks(ticks=range(12), labels=["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"], rotation=45)
plt.xlabel("Mes de lanzamiento")
plt.ylabel("Ingresos Totales ($)")
plt.title("Ingresos por mes de lanzamiento")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Mostrar el gráfico
plt.show()


