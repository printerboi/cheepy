import logging
import secrets
from types import SimpleNamespace
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from fastapi.security import HTTPBasic, HTTPBasicCredentials

from server.cheepy.Config import Config
from server.cheepy.DBConnector import DBConnector
from server.cheepy.Models import MessageModel

logger = logging.getLogger("uvicorn.info")  # Use uvicorn's logger for consistency

motd_folder = "motd/msg.json"
security = HTTPBasic()
config = Config()

def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, config.user)
    correct_password = secrets.compare_digest(credentials.password, config.password)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

def get_db():
    db = DBConnector()
    try:
        yield db
    finally:
        db.close()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    logger.info("Application is starting...")
    # Example: Initialize database, load ML model, etc.
    # app.state.db = await connect_to_db()
    app.state = SimpleNamespace(my_resource="cheepy")
    logger.info("DB Connection established!")

    db = get_db()

    yield  # This allows FastAPI to start serving requests
    del app.state
    # Code to run on shutdown
    print("Application is shutting down...")
    # Example: Close database connection
    # await app.state.db.close()

app = FastAPI(lifespan=lifespan)

@app.get("/cheep")
def read_root(username: str = Depends(verify_credentials), db: DBConnector = Depends(get_db)):
    print(f"Request received: {username}")

    msg = db.get_last_message()

    # Gebe den Inhalt als JSON-Antwort zurück
    return JSONResponse(content=msg, status_code=status.HTTP_200_OK)

@app.post("/cheep")
async def create_message(message: MessageModel, username: str = Depends(verify_credentials), db: DBConnector = Depends(get_db)):
    db.create_message(message)

    return {"status": "success", "message": message}