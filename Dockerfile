# Używamy obrazu z Pythonem
FROM python:3.8-slim

# Tworzymy katalog dla aplikacji
WORKDIR /app

# Kopiujemy pliki aplikacji do katalogu /app w kontenerze
COPY . /app

# Instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt

# Ustawiamy port, na którym będzie działać aplikacja
EXPOSE 7777

# Uruchamiamy aplikację po starcie kontenera
CMD ["python", "app.py"]
