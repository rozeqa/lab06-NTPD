# lab06-NTPD - Róża Domańska 122328

## Zadanie 1

Utworzyłam repozytorium na GitHubie z kodem aplikacji API z laboratorium 5. Dodałam plik `model.py` zawierający funkcje `train_and_predict()` oraz `get_accuracy()` operujące na zbiorze danych Iris (klasyfikacja za pomocą regresji logistycznej).

Napisałam cztery testy jednostkowe w pliku `test_model.py`:
<img width="508" height="337" alt="Zrzut ekranu 2026-05-7 o 11 16 59" src="https://github.com/user-attachments/assets/b06f52de-9d0a-4412-8a2b-7ffa16e4f3c5" />

## Zadanie 2

W katalogu `.github/workflows/` utworzyłam plik `ci.yml` definiujący pipeline CI. Workflow uruchamia się automatycznie przy każdym pushu i pull requeście do gałęzi `main`.

<img width="993" height="360" alt="Zrzut ekranu 2026-05-7 o 11 18 43" src="https://github.com/user-attachments/assets/5b151f8f-8e63-4a81-8a85-9e636f1a2835" />
<img width="680" height="360" alt="Zrzut ekranu 2026-05-7 o 11 20 49" src="https://github.com/user-attachments/assets/5f680202-3404-4fff-a466-dbc7c07d8034" />

## Wnioski

Pipeline CI działa poprawnie – testy są uruchamiane automatycznie po każdym pushu do gałęzi `main`. Wszystkie 4 testy jednostkowe przechodzą pomyślnie, a model osiąga dokładność powyżej 70% na zbiorze testowym Iris.
