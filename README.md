# 📊 Analiza danych COVID-19

Projekt analizuje dane dotyczące pandemii COVID-19 na przykładzie trzech krajów: **Polska**, **Niemcy** oraz **Stany Zjednoczone**.

---

## 🧠 Co robi projekt?

- Pobiera dane z [Our World in Data](https://covid.ourworldindata.org/data/owid-covid-data.csv)
- Filtrowanie danych do roku 2022
- Normalizacja: przelicza przypadki i zgony na 1000 mieszkańców
- Wylicza **średnią kroczącą (7 dni)** dla nowych przypadków i zgonów
- Analizuje dodatkowe wskaźniki zdrowotne:
  - Odsetek osób zaszczepionych
  - Liczba pacjentów w szpitalach na milion mieszkańców
  - Liczba pacjentów na OIOM na milion mieszkańców
  - Wygładzone zgony na milion mieszkańców
- Tworzy i zapisuje automatycznie wykresy 📈 jako pliki PNG

---

## 🗂 Zawartość katalogu

- `covid_health_metrics_auto_save.py` – główny skrypt analizy
- `covid_plots/` – folder, w którym zapisywane są wykresy PNG

---

## ▶️ Jak uruchomić?

1. Zainstaluj wymagane biblioteki (jeśli nie masz):
   ```bash
   pip install pandas matplotlib seaborn
