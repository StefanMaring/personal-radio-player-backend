from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import random

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],               
    allow_headers=["*"],       
    expose_headers=["Content-Disposition"],   
)

AUDIO_FOLDER = os.path.join(os.path.dirname(__file__), "audio")
audio_queue = [];

@app.get("/getSong")
def getSong():
    mp3_files = [file for file in os.listdir(AUDIO_FOLDER) if file.endswith(".mp3")]
    if not mp3_files:
        raise HTTPException(status_code=404, detail="No mp3 files found")
    
    random_mp3 = random.choice(mp3_files)
    while checkIfFileIsInQueue(random_mp3):
        random_mp3 = random.choice(mp3_files)

    file_path = os.path.join(AUDIO_FOLDER, random_mp3)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    if(len(audio_queue) >= 3):
        dequeue()

    enqueue(random_mp3)

    return FileResponse(file_path, media_type="audio/mpeg", filename=random_mp3)

def enqueue(file_name):
    if file_name not in audio_queue:
        audio_queue.insert(0, file_name)
    else:
        raise HTTPException(status_code=400, detail="File already in queue")
    
def dequeue():
    if audio_queue:
        return audio_queue.pop(2)
    else:
        raise HTTPException(status_code=404, detail="Queue is empty")
    
def checkIfFileIsInQueue(file_name):
    if file_name in audio_queue:
        return True
    else:
        return False