from detection import detect_objects

def describe_image(image_path: str) -> str:
    """
    Genera una descripción en inglés basada en los objetos detectados en la imagen.
    """
    detected_objects = detect_objects(image_path)

    if not detected_objects:
        return "No objects were detected in the image."

    object_counts = {}
    for obj in detected_objects:
        object_counts[obj] = object_counts.get(obj, 0) + 1

    # Construcción de la descripción con todos los elementos detectados
    description_parts = [f"{count} {obj}(s)" for obj, count in object_counts.items()]
    
    return "The image contains " + ", ".join(description_parts) + "."
