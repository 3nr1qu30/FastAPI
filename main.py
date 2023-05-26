from fastapi import FastAPI, UploadFile, File
from starlette.responses import FileResponse
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


@app.post("/")
async def index(fileee: UploadFile = File(...)):
    contents = await fileee.read()

    with open("audio.wav", "wb") as audio_file:
        audio_file.write(contents)
    print(contents)
    return FileResponse("audio.wav", filename="audio.wav")

