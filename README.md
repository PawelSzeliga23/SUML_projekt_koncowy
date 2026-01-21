# 🐕 PsiLook - Aplikacja do Rozpoznawania Ras Psów

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.52.2-red.svg)](https://streamlit.io)
[![YOLO](https://img.shields.io/badge/YOLO-v11n-green.svg)](https://github.com/ultralytics/ultralytics)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**PsiLook** to zaawansowana aplikacja webowa wykorzystująca głębokie uczenie maszynowe do **automatycznego rozpoznawania ras psów** w czasie rzeczywistym. Aplikacja wykorzystuje najnowszą wersję modelu **YOLOv11n** wytrenowanego na zbiorze **Stanford Dogs Dataset** i umożliwia identyfikację **120 różnych ras psów**.

![PsiLook Demo](assets/demo.gif)

---

## 🌟 Kluczowe Funkcjonalności

### 📸 Wykrywanie z Zdjęć
- Upload zdjęć (JPG, JPEG, PNG)
- Zdjęcia z kamery internetowej
- Detekcja wielu psów na jednym zdjęciu
- Top 3 najbardziej prawdopodobne rasy z poziomem pewności

### 🎥 Detekcja w Czasie Rzeczywistym
- Streamowanie obrazu z kamery internetowej
- Wykrywanie ras psów na żywo
- Automatyczne zapisywanie unikalnych wykryć
- Wsparcie dla wielu kamer (wybór ID)

### 📚 Biblioteka Ras
- Pełna lista 120 rozpoznawanych ras
- Przykładowe zdjęcia dla każdej rasy (via Dog CEO API)
- Polskie nazwy ras

### 🤖 Informacje o Modelu
- Szczegóły architektury YOLOv11n
- Informacje o danych treningowych
- Dokumentacja procesu uczenia

---

## 🏗️ Architektura Projektu

```
SUML_projekt_koncowy/
├── app.py                    # Punkt wejścia aplikacji
├── requirements.txt          # Zależności projektu
├── TODO.txt                  # Lista zadań do wykonania
│
├── models/                   # Warstwa modeli ML
│   ├── yolo_init.py          # Inicjalizacja i ładowanie modelu YOLO
│   ├── yolo_model.py         # Wrapper dla modelu YOLO
│   ├── dog_detection.py      # Klasa reprezentująca wykrycie
│   └── pretrained/           # Folder z wytrenowanym modelem
│       └── best.pt           # Model YOLOv11n
│
├── controllers/              # Logika biznesowa
│   ├── photo_controller.py   # Kontroler dla wykrywania ze zdjęć
│   ├── webcam_controller.py  # Kontroler dla kamery na żywo
│   └── dog_breed_library_controller.py  # Kontroler biblioteki ras
│
├── views/                    # Interfejs użytkownika
│   ├── navigation.py         # System nawigacji
│   ├── photo_detection.py    # Widok wykrywania ze zdjęć
│   ├── webcam_detection.py   # Widok kamery
│   ├── dog_breed_library.py  # Widok biblioteki ras
│   └── model.py              # Widok informacji o modelu
│
├── components/               # Komponenty UI wielokrotnego użytku
│   └── dog_card.py           # Karta wyświetlająca wyniki detekcji
│
├── utils/                    # Funkcje pomocnicze
│   ├── photo_utils.py        # Konwersje obrazów
│   ├── labels_utils.py       # Mapowanie etykiet (PL/API)
│   ├── dog_api.py            # Integracja z Dog CEO API
│   ├── colors.py             # Paleta kolorów aplikacji
│   └── navigation_utils.py   # Konfiguracja nawigacji
│
└── assets/                   # Zasoby statyczne
    └── no_image_available.jpg
```

### 🎯 Wzorzec Projektowy: MVC (Model-View-Controller)

- **Model**: Logika ML, YOLO, klasy danych (`models/`)
- **View**: Interfejs Streamlit, komponenty UI (`views/`, `components/`)
- **Controller**: Logika biznesowa, pipeline'y przetwarzania (`controllers/`)

---

## 🚀 Instalacja i Uruchomienie

### Wymagania
- Python 3.8 lub nowszy
- Kamera internetowa (opcjonalnie, dla funkcji live detection)
- ~500 MB miejsca na dysku (model + zależności)

### Krok 1: Klonowanie repozytorium
```bash
git clone https://github.com/PawelSzeliga23/SUML_projekt_koncowy.git
cd SUML_projekt_koncowy
```

### Krok 2: Instalacja zależności
```bash
pip install -r requirements.txt
```

### Krok 3: Pobranie modelu
Umieść wytrenowany model YOLO (`best.pt`) w folderze:
```
models/pretrained/best.pt
```

### Krok 4: Uruchomienie aplikacji
```bash
streamlit run app.py
```

Aplikacja będzie dostępna pod adresem: **http://localhost:8501**

---

## 🤖 O Modelu

### YOLOv11n (Nano)
Model jest oparty na najnowszej architekturze **YOLO (You Only Look Once)** w wersji **nano**, zoptymalizowanej pod kątem:
- **Szybkości** (1.5–3 ms na GPU)
- **Niskiego zużycia zasobów** (~2.6M parametrów)
- **Real-time detection** na urządzeniach edge

### Architektura
- **Backbone**: Lekkie bloki C3k2 do ekstrakcji cech
- **SPPF**: Spatial Pyramid Pooling Fast - detekcja multi-scale
- **C2PSA**: Cross-Stage Partial Spatial Attention
- **Neck**: Feature Pyramid Network (FPN) + PAN
- **Head**: Multi-scale prediction (klasy, bounding boxes, confidence)

### Dataset
- **Zbiór**: [Stanford Dogs Dataset](https://universe.roboflow.com/iliescu-mihail-doirn/stanford-dogs-dataset-dog-breed)
- **Wielkość**: 20,000+ obrazów
- **Klasy**: 120 ras psów
- **Źródło**: Roboflow Universe

### Wydajność
- **Dokładność**: Wysoka precyzja w czasie rzeczywistym
- **Confidence threshold**: 0.4 (zdjęcia) / 0.6 (live detection)
- **Input size**: 640x640 pikseli

---

## 📖 Instrukcja Użycia

### 1. Wykrywanie z Zdjęć
1. Wybierz zakładkę **"Zdjęcia"** w menu bocznym
2. Wybierz **"Wgraj zdjęcie"** lub **"Użyj kamery"**
3. Załaduj zdjęcie psa
4. Poczekaj na wyniki (top 3 rasy z poziomem pewności)

### 2. Detekcja na Żywo
1. Wybierz zakładkę **"Kamera"**
2. Wybierz ID kamery z listy rozwijanej
3. Kliknij **"Uruchom kamerę"**
4. Pokaż psa przed kamerą
5. Aplikacja automatycznie wykryje i wyświetli rasę
6. Kliknij **"Zatrzymaj kamerę"** aby zakończyć

### 3. Przeglądanie Biblioteki
1. Wybierz **"Biblioteka ras"** w menu
2. Przeglądaj wszystkie 120 dostępnych ras
3. Zobacz przykładowe zdjęcia każdej rasy

---

## 🛠️ Główne Technologie

| Technologia | Wersja | Zastosowanie |
|-------------|--------|--------------|
| **Python** | 3.8+ | Język programowania |
| **Streamlit** | 1.52.2 | Framework webowy |
| **Ultralytics** | 8.3.249 | Implementacja YOLO |
| **PyTorch** | 2.9.1 | Framework ML |
| **OpenCV** | 4.12.0 | Przetwarzanie obrazu |
| **Pillow** | 12.1.0 | Operacje na obrazach |
| **NumPy** | 2.2.6 | Operacje numeryczne |
| **Pandas** | 2.3.3 | Przetwarzanie danych |

Pełna lista zależności znajduje się w pliku [`requirements.txt`](requirements.txt).

---

## 🗺️ Roadmap

### ✅ Zrealizowane
- [x] Wykrywanie ras ze zdjęć
- [x] Detekcja w czasie rzeczywistym z kamery
- [x] Biblioteka 120 ras psów
- [x] Integracja z Dog CEO API
- [x] Polskie tłumaczenia nazw ras
- [x] Dokumentacja modelu

### 🚧 W toku (z TODO.txt)
- [ ] Obsługa filmów (wykrywanie ras w plikach wideo)
- [ ] Ulepszony feedback dla użytkownika
- [ ] Komunikaty o błędach w języku polskim
- [ ] Obsługa przypadków "nie znaleziono rasy"
- [ ] Rozszerzenie mappera polskich nazw

### 💡 Planowane
- [ ] Deploy do Streamlit Cloud
- [ ] Wsparcie dla większej liczby ras
- [ ] Historia wykryć użytkownika
- [ ] Eksport wyników do PDF
- [ ] Dark mode

---

## 🤝 Wkład w Projekt

Chętnie przyjmujemy pull requesty! Jeśli chcesz przyczynić się do rozwoju projektu:

1. **Fork** repozytorium
2. Stwórz branch z feature'em (`git checkout -b feature/AmazingFeature`)
3. Commit zmian (`git commit -m 'Add some AmazingFeature'`)
4. Push do brancha (`git push origin feature/AmazingFeature`)
5. Otwórz **Pull Request**

### Obszary do poprawy
- Testy jednostkowe i integracyjne
- Obsługa filmów (patrz TODO.txt)
- Optymalizacja wydajności
- Dokumentacja API
- Internationalization (i18n)

---

## 📝 Licencja

Projekt jest dostępny na licencji **MIT**. Zobacz plik [LICENSE](LICENSE) aby uzyskać więcej informacji.

---

## 👤 Autor

**Paweł Szeliga**
GitHub: [@PawelSzeliga23](https://github.com/PawelSzeliga23)

---

## 🙏 Podziękowania

- **Stanford University** - za udostępnienie Stanford Dogs Dataset
- **Ultralytics** - za framework YOLO
- **Dog CEO** - za darmowe API z obrazami psów
- **Roboflow** - za platformę do zarządzania danymi treningowymi
- **Streamlit** - za fantastyczny framework webowy

---

## 📞 Wsparcie

Jeśli napotkasz problemy lub masz pytania:
- Otwórz [Issue](https://github.com/PawelSzeliga23/SUML_projekt_koncowy/issues) na GitHubie
- Sprawdź sekcję **"O Modelu"** w aplikacji
- Przejrzyj dokumentację w kodzie

---

## 🐾 Ciekawostki

- Model potrafi rozpoznać 120 różnych ras psów
- Najszybsze wykrycie zajmuje ~1.5-3ms na GPU
- Aplikacja używa modelu o wadze tylko ~2.6M parametrów
- Zintegrowane API dostarcza >20,000 zdjęć psów

---

<p align="center">
  <strong>Zbudowano z ❤️ i AI</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="Made with Python">
  <img src="https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B.svg" alt="Made with Streamlit">
  <img src="https://img.shields.io/badge/Powered%20by-YOLO-00FFFF.svg" alt="Powered by YOLO">
</p>