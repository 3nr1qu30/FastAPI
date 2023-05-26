from fastapi import FastAPI, UploadFile
from starlette.responses import FileResponse

app = FastAPI()

@app.post("/")
async def index(file: UploadFile = File(...)):
    contents = await file.read()

    with open("audio.wav", "wb") as audio_file:
        audio_file.write(contents)

    return FileResponse("audio.wav", filename="audio.wav")
