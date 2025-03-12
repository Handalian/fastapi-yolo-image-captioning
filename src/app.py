from dotenv import load_dotenv

# Cargar las variables desde .env
load_dotenv()

from fastapi import FastAPI, File, UploadFile, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from description import describe_image
from deep_translator import GoogleTranslator, exceptions
import logging
import uuid

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Servir archivos estáticos (imágenes, CSS, etc.)
STATIC_FOLDER = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_FOLDER), name="static")

# Carpeta donde se guardarán las imágenes subidas
UPLOAD_FOLDER = Path(__file__).parent / "static" / "uploads"
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

# Configurar Jinja2 Templates
BASE_DIR = Path(__file__).parent  # Obtiene la ruta de `src`
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Idiomas válidos para la traducción
VALID_LANGUAGES = {"es", "en", "fr", "de", "it", "pt"}

def translate_text(text: str, target_language: str = "es") -> str:
    """
    Traduce un texto a otro idioma usando Google Translator.
    """
    if target_language not in VALID_LANGUAGES:
        return f"Error: Idioma '{target_language}' no soportado."

    try:
        translator = GoogleTranslator(source="auto", target=target_language)
        translated_text = translator.translate(text)
        
        # Correcciones manuales en la traducción
        custom_translations = {"empate": "corbata"}  # Evitar que "tie" se traduzca como "empate"
        for incorrect, correct in custom_translations.items():
            translated_text = translated_text.replace(incorrect, correct)

        return translated_text

    except (exceptions.NotValidPayload, exceptions.NotValidLength) as e:
        logger.error(f"Error en la traducción: {e}")
        return f"Error en la traducción: {str(e)}"

    except Exception as e:
        logger.error(f"Error inesperado en la traducción: {e}")
        return f"Error inesperado en la traducción: {str(e)}"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Muestra la página principal del sitio.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload_image(request: Request, file: UploadFile = File(...), language: str = Form(...)):
    """
    Sube una imagen, la procesa y devuelve la descripción traducida.
    """
    try:
        # Validar idioma
        if language not in VALID_LANGUAGES:
            raise HTTPException(status_code=400, detail=f"Idioma '{language}' no soportado.")

        # Generar un nombre único para evitar sobrescribir archivos
        file_extension = file.filename.split(".")[-1]
        unique_filename = f"{uuid.uuid4().hex}.{file_extension}"
        file_location = UPLOAD_FOLDER / unique_filename

        # Guardar el archivo
        with file_location.open("wb") as buffer:
            buffer.write(await file.read())

        logger.info(f"Imagen guardada en {file_location}")

        # Procesar la imagen y traducir la descripción
        description = describe_image(str(file_location))
        description_translation = translate_text(description, target_language=language)

        return templates.TemplateResponse("result.html", {
            "request": request,
            "file_path": f"/static/uploads/{unique_filename}",
            "description": description_translation,
            "language": language
        })

    except HTTPException as he:
        logger.error(f"Error de cliente: {he.detail}")
        raise he

    except Exception as e:
        logger.error(f"Error en el servidor: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor.")
