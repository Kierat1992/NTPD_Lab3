# FastAPI ML API + PostgreSQL (Docker Compose)

 Aplikacja API z prostym modelem ML uruchamiana w trybie produkcyjnym, zintegrowana z bazą danych PostgreSQL i skonfigurowana w Docker Compose.

---

## Funkcjonalności

- Endpoint `/` – powitalna wiadomość
- Endpoint `/predict` – predykcja na podstawie przesłanej liczby `x`
- Walidacja danych i obsługa błędów
- Endpointy informacyjne `/info`, `/health`
- Integracja z PostgreSQL (Docker)
- Gotowa konfiguracja Docker + Docker Compose

---

## Uruchamianie aplikacji

### Lokalnie (bez Dockera)

```bash
# 1. Utwórz i aktywuj środowisko
python -m venv venv
.\venv\Scripts\activate

# 2. Zainstaluj zależności
pip install -r requirements.txt

# 3. Uruchom API
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
```

---

### Przez Docker

```bash
# 1. Zbuduj obraz
docker build -t fastapi-ml-app .

# 2. Uruchom kontener
docker run -d -p 8000:8000 fastapi-ml-app
```

---

###  Przez Docker Compose (FastAPI + PostgreSQL)

```bash
docker-compose up --build
```

 Aplikacja dostępna pod:
- http://localhost:8000  
- http://localhost:8000/docs (Swagger)

---

## Parametry środowiskowe

Zmienne środowiskowe (ustawiane automatycznie przez Docker Compose):

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/mydatabase
```

---

## Wymagania systemowe

- Python 3.11
- Docker Desktop
- Porty:
  - 8000 – aplikacja FastAPI
  - 5432 – PostgreSQL

---

## Testowanie

```bash
curl.exe -X POST http://localhost:8000/predict -H "Content-Type: application/json" --data-raw "{\"x\": 7}"
```

---

## Pliki w repozytorium

- `app.py` – kod aplikacji FastAPI
- `requirements.txt` – zależności
- `Dockerfile` – budowa obrazu
- `docker-compose.yml` – konfiguracja usług
- `README.md` – dokumentacja

---
v

---

## Autor

Jędrzej  Rychter – Projekt wykonany w ramach przedmiotu NTPD Laboratorium numer 3 i 4