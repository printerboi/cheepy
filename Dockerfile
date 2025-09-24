# Verwende ein offizielles Python-Image
FROM python:3.9

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Kopiere die Anforderungen und installiere sie
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Code in das Container-Image
COPY . .

# Exponiere den Port, auf dem die App läuft
EXPOSE 8000

# Befehl zum Starten der FastAPI-Anwendung
CMD ["fastapi", "dev", "cheepy/cheepy.py"]