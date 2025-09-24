from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI()

motd_folder = "motd/msg.json"

@app.get("/cheep")
def read_root():
    with open(motd_folder, 'r', encoding='utf-8') as datei:
      inhalt = json.load(datei)
    
    # Gebe den Inhalt als JSON-Antwort zurück
    return JSONResponse(content=inhalt)