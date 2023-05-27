from fastapi import FastAPI
from pydantic import BaseModel
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

    # Aquí puedes hacer lo que necesites con la transcripción recibida

    return {"message": "Transcription received"}