# DataCamp-Project-Cleaning-Bank-Marketing-Campaign-Data
Projekt obejmuje utworzenie i zarządzanie bazą danych w PostgreSQL na podstawie danych zgromadzonych w ramach kampanii marketingowej banku dotyczącej ofert kredytów osobistnych. Poniżej przedstawiam opis poszczególnych kroków oraz elementów projektu:

1. **Importowanie bibliotek:**

Wykorzystanie Pandas i NumPy do manipulacji i analizy danych.

2. **Wczytanie danych:**

Pobranie danych z pliku CSV o nazwie 'bank_marketing.csv'.

3. **Podział danych na trzy tabele:**

client: Dane dotyczące klientów i ich cechy demograficzne.

campaign: Informacje dotyczące kampanii marketingowej, kontaktów i wyników.

economics: Dane ekonomiczne klientów.


4. **Przetworzenie danych:**

Zmiana nazw kolumn i dostosowanie formatu danych.
Zastąpienie niektórych wartości i korekta formatów.

5. **Zapisanie danych do osobnych plików CSV:**

Zapis danych z poszczególnych tabel do plików 'client.csv', 'campaign.csv' i 'economics.csv'.

6. **Tworzenie tabel w bazie danych:**

Dla każdej tabeli (client, campaign, economics) utworzenie odpowiednich struktur.

7. **Wprowadzenie danych do tabel za pomocą SQL:**

Utworzenie wieloliniowych ciągów znaków SQL, które zawierają kody do utworzenia tabel oraz zaimportowania danych z plików CSV.

8. **Opis tabel:**

Dla każdej tabeli zawarto opis kolumn, ich typów danych, a także informacje o kluczach głównych i obcych.

9. **Dodatkowe uwagi:**

Projekt obejmuje również pewne modyfikacje danych, takie jak zmiana formatu daty, korekty w nazwach kolumn, oraz dostosowanie wartości tak, aby lepiej odpowiadały wymaganiom bazy danych.
