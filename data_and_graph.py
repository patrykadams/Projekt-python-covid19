import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output directory for plots
output_dir = "covid_plots"
os.makedirs(output_dir, exist_ok=True)

# Set visual style
sns.set(style="whitegrid")

# Load data
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# Countries to analyze
countries = ["Poland", "Germany", "United States"]

# Filter by countries and date
df = df[df["location"].isin(countries)].copy()
df["date"] = pd.to_datetime(df["date"])
df = df[df["date"] <= "2022-12-31"]

# Define expected columns
expected_cols = [
    "location", "date", "new_cases", "new_deaths", "population",
    "people_vaccinated_per_hundred", "hospital_patients_per_million",
    "icu_patients_per_million", "new_deaths_smoothed_per_million"
]

# Keep only available columns
available_cols = [col for col in expected_cols if col in df.columns]
df = df[available_cols].dropna()

# Calculate derived metrics if possible
if "new_cases" in df.columns and "population" in df.columns:
    df["cases_per_1000"] = df["new_cases"] / (df["population"] / 1000)
if "new_deaths" in df.columns and "population" in df.columns:
    df["deaths_per_1000"] = df["new_deaths"] / (df["population"] / 1000)

# Add rolling averages if calculated
if "cases_per_1000" in df.columns:
    df["cases_rolling"] = df.groupby("location")["cases_per_1000"].transform(lambda x: x.rolling(7).mean())
if "deaths_per_1000" in df.columns:
    df["deaths_rolling"] = df.groupby("location")["deaths_per_1000"].transform(lambda x: x.rolling(7).mean())

# Plotting function with saving
def safe_lineplot(y, title, ylabel, filename):
    if y in df.columns:
        plt.figure(figsize=(14, 6))
        sns.lineplot(data=df, x="date", y=y, hue="location")
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel(ylabel)
        plt.legend(title="Country")
        plt.tight_layout()
        path = os.path.join(output_dir, filename)
        plt.savefig(path)
        plt.close()

# Generate and save plots
safe_lineplot("people_vaccinated_per_hundred", "Percentage of People Vaccinated (per 100)", "People Vaccinated per 100", "vaccinated.png")
safe_lineplot("hospital_patients_per_million", "Hospital Patients per Million Over Time", "Patients per Million", "hospital_patients.png")
safe_lineplot("icu_patients_per_million", "ICU Patients per Million Over Time", "ICU Patients per Million", "icu_patients.png")
safe_lineplot("new_deaths_smoothed_per_million", "Smoothed COVID-19 Deaths per Million Over Time", "Deaths per Million (Smoothed)", "deaths_smoothed.png")