
import pandas as pd

# Extract : lire un CSV
df = pd.read_csv("ventes.csv")

# Transform : nettoyer + ajouter une colonne
df["date"] = pd.to_datetime(df["date"])
df["chiffre_total"] = df["prix_unitaire"] * df["quantite"]

# Load : exporter vers Excel
df.to_excel("ventes_transformées.xlsx", index=False)

import pandas as pd

df = pd.DataFrame({
    "produit": ["A", "A", "B", "B", "C"],
    "quantite": [2, 3, 5, 1, 4],
    "prix": [10, 10, 20, 20, 15]
})

# Calcul du CA par produit
df["CA"] = df["quantite"] * df["prix"]
ca_par_produit = df.groupby("produit")["CA"].sum()

print(ca_par_produit)


import pandas as pd

# 1. Extract + Transform directement depuis l'URL
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
df = pd.read_csv(url)  # pandas peut lire directement depuis une URL

f["Passengers"] = df["Passengers"].astype(int)  # assure que les passagers sont des entiers
df["Year"] = df["Year"].astype(int)             # assure que l'année est un entier
df["Month"] = df["Month"].astype(str)     

df = df.dropna(subset=["Passengers"])

#Ou ajouter une colonne calculée, par exemple le pourcentage de passagers par rapport à l’année :

df["Passenger_pct"] = df.groupby("Year")["Passengers"].apply(lambda x: x / x.sum() * 100)

# 2. Load : sauvegarder en Parquet
df.to_parquet("data_clean.parquet", index=False)

print("Pipeline ETL terminé")


from multiprocessing import Pool

def carre(x):
    return x * x

if __name__ == "__main__":
    with Pool(4) as p:  # 4 processus en parallèle
        resultats = p.map(carre, range(10))
    print(resultats)
    
    
