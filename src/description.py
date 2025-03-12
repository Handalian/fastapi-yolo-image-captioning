import spacy
from detection import detect_objects

nlp = spacy.load("en_core_web_sm")  # Cargar modelo de spaCy en inglés

def describe_image(image_path: str) -> str:
    """
    Genera una descripción en inglés basada en los objetos detectados en la imagen usando NLP.
    """
    detected_objects = detect_objects(image_path)

    if not detected_objects:
        return "No objects were detected in the image."

    object_counts = {}
    for obj in detected_objects:
        object_counts[obj] = object_counts.get(obj, 0) + 1

    # Generar una descripción fluida con NLP
    description = "This image appears to contain "
    for obj, count in object_counts.items():
        obj_noun = nlp(obj)[0]  # Obtener el objeto como un token NLP
        plural = obj_noun.text if count == 1 else obj_noun.text + "s"
        description += f"{count} {plural}, "

    return description.strip(", ") + "."
