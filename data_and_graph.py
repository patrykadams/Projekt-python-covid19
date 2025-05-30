
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Styl wykresów
sns.set(style="whitegrid")

# Wczytanie danych
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# kraje
countries = ["Poland", "Germany", "United States"]

# Filtrowanie danych
df_filtered = df[df["location"].isin(countries)].copy()
df_filtered["date"] = pd.to_datetime(df_filtered["date"])
df_filtered = df_filtered[["location", "date", "new_cases", "population"]].dropna()

df_filtered = df_filtered[df_filtered["date"] <= "2022-12-31"]

# Obliczanie nowych przypadków na 1000 mieszkańców
df_filtered["cases_per_1000"] = df_filtered["new_cases"] / (df_filtered["population"] / 1000)

# Wykres
plt.figure(figsize=(14, 6))
sns.lineplot(data=df_filtered, x="date", y="cases_per_1000", hue="location")
plt.title("Nowe przypadki COVID-19 na 1000 mieszkańców")
plt.xlabel("Data")
plt.ylabel("Nowe przypadki na 1000 osób")
plt.legend(title="Kraj")
plt.tight_layout()
plt.show()
