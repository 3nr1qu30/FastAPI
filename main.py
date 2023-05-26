from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from pydantic import BaseModel
import base64
import wave
from starlette.responses import FileResponse
from starlette import status

app= FastAPI()

# Configurar los orígenes permitidos en CORS
origins = [
    "http://localhost:8080",
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

class AudioData(BaseModel):
    audioBase64: str

@app.post("/")
async def index(audio_data: AudioData):
    audio_base64 = audio_data.audioBase64
    print(audio_base64)

    # Decodificar la cadena base64
    audio_decoded = base64.b64decode(audio_base64)
    print(audio_decoded)

    # Guardar el audio decodificado en un archivo WAV
    with wave.open("audio.wav", "w") as wav_file:
        wav_file.setnchannels(1)  # Configurar el número de canales (mono)
        wav_file.setsampwidth(2)  # Configurar el ancho de muestra en bytes (2 bytes para 16 bits)
        wav_file.setframerate(44100)  # Configurar la frecuencia de muestreo (44.1 kHz)
        wav_file.writeframes(audio_decoded)

    # Devolver la respuesta con el archivo de audio descargable
    return FileResponse("audio.wav", filename="audio.wav", media_type="audio/wav", status_code=status.HTTP_200_OK)
