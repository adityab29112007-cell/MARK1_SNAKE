from fastapi import FastAPI, UploadFile, File
from backend.gemini_service import identify_snake_image
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Indian Snake Identifier API is running"}

@app.post("/identify-snake")
async def identify_snake(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    result = identify_snake_image(file_path)

    return {
        "result": result
    }