# ⚖️ Kalkulator BMI (GUI Tkinter)

Aplikacja z interfejsem graficznym napisana w **Pythonie**, służąca do obliczania wskaźnika masy ciała (BMI). Program nie tylko podaje wynik liczbowy, ale również interpretuje go zgodnie ze standardowymi kategoriami medycznymi.

---

## ✨ Funkcje
* **Interfejs Graficzny:** Intuicyjne okno zbudowane przy użyciu biblioteki `tkinter`.
* **Obliczenia w czasie rzeczywistym:** Przeliczanie wzrostu (cm na m) i wagę na wskaźnik BMI.
* **Interpretacja wyniku:** Wyświetlanie informacji o stanie zdrowia (np. niedowaga, nadwaga, otyłość).
* **Obsługa błędów:** * Zabezpieczenie przed pozostawieniem pustych pól.
    * Zabezpieczenie przed dzieleniem przez zero (w przypadku wpisania wzrostu 0).
* **Estetyka:** Kolorowy layout z czytelnymi czcionkami.

## 🛠️ Technologie
* **Język:** Python 3.x
* **Biblioteka:** `tkinter` (standardowa biblioteka GUI w Pythonie)

## 📖 Instrukcja obsługi
1. Wpisz swoją **wagę** w kilogramach (np. 75).
2. Wpisz swój **wzrost** w centymetrach (np. 180).
3. (Opcjonalnie) Wpisz swój **wiek**.
4. Kliknij żółty przycisk **"Oblicz"**.
5. Wynik oraz opis Twojego wskaźnika BMI pojawi się pod polami wprowadzania.

## ⚠️ Uwagi techniczne (Do zrobienia)
W kodzie znajdują się zakomentowane sekcje dotyczące logiki wieku. W przyszłości planowane jest:
- [ ] Uwzględnienie przedziałów wiekowych przy interpretacji BMI.
- [ ] Poprawa pobierania danych wieku (naprawa błędu `get_wiek` bez nawiasów).

---
*Projekt ma charakter edukacyjny i służy do nauki tworzenia interfejsów graficznych oraz obsługi wyjątków w Pythonie.*
