from ultralytics import YOLO
import torch
import logging
from pathlib import Path

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Verificar si hay GPU disponible
device = "cuda" if torch.cuda.is_available() else "cpu"
logger.info(f"Usando dispositivo: {device}")

MODEL_PATH = Path(__file__).resolve().parent / "models" / "yolov8n.pt"

# Cargar el modelo YOLOv8
model = YOLO(str(MODEL_PATH)).to(device)
def detect_objects(image_path: str) -> list[str]:
    """
    Detecta objetos en una imagen usando YOLO y devuelve una lista con los nombres de los objetos detectados.
    """
    try:
        results = model(image_path, verbose=False)  # Obtener resultados
        detected_objects = []

        for result in results:
            if hasattr(result, "names") and hasattr(result, "boxes"):
                for box in result.boxes:
                    class_id = int(box.cls.item())  # Obtener ID de la clase
                    object_name = result.names.get(class_id, f"desconocido_{class_id}")  # Nombre del objeto
                    detected_objects.append(object_name)

        if not detected_objects:
            logger.info(f"No se detectaron objetos en {image_path}")
            return ["No se detectaron objetos"]

        return detected_objects

    except Exception as e:
        logger.error(f"Error al procesar la imagen {image_path}: {e}")
        return ["Error en la detección"]
