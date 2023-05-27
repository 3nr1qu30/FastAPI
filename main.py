from fastapi import FastAPI
from pydantic import BaseModel
import os
import openai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Configurar los orígenes permitidos en CORS
origins = [
    "https://lyra-production.up.railway.app"
    # Agrega aquí los demás orígenes permitidos
]

# Agregar el middleware de CORS a la aplicación
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TranscriptionData(BaseModel):
    transcription: str

@app.post("/")
async def index(data: TranscriptionData):
    transcription = data.transcription
    print(transcription)

    openai.api_key = os.getenv("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")

    response =await openai.Completion.create(
    model="text-davinci-003",
    prompt=transcription + "\n\nTl;dr",
    temperature=0.7,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=1
    )
    print(response)
        # Aquí puedes hacer lo que necesites con la transcripción recibida
    return {"message": "Transcription received"}