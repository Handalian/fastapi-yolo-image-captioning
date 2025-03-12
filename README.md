# **Computer Vision & NLP API**  

🚀 FastAPI para subir imágenes, describirlas y traducir la descripción a diferentes idiomas usando Google Translate.  

## **📌 Características**  
- 📷 **Subida de imágenes**  
- 📝 **Descripción automática** de imágenes  
- 🌍 **Traducción** de descripciones a varios idiomas  
- ⚡ **Desarrollado con FastAPI**  

---

## **🛠 Instalación y Configuración**  

### **1️⃣ Clona el repositorio**  
```sh
git clone https://github.com/Handalian/fastapi-yolo-image-captioning.git
cd fastapi-yolo-image-captioning

```

### **2️⃣ Crea un entorno virtual (opcional pero recomendado)**  
```sh
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### **3️⃣ Instala dependencias**  
```sh
pip install -r requirements.txt
```

### **4️⃣ Crea un archivo `.env`**  
```sh
echo "PYTHONPATH=src" > .env
```

### **5️⃣ Ejecuta la API**  
```sh
uvicorn app:app --reload
```
La API estará disponible en `http://127.0.0.1:8000`

---

## **📤 Uso de la API**  

### **Subir una imagen y obtener descripción traducida**  
**Método:** `POST /upload/`  
**Parámetros:**  
- `file`: Imagen a analizar (JPEG/PNG)  
- `language`: Idioma destino (ejemplo: `es`, `fr`, `de`)  

Puedes probarlo en Swagger UI:  
🔗 `http://127.0.0.1:8000/docs`

---

## **📂 Estructura del Proyecto**  
```
📁 TU_REPO/
 ├── 📂 src/            # Código fuente si está en un módulo separado
 ├──── 📂 static/         # Archivos estáticos (imágenes, CSS, etc.)
 ├──── 📂 templates/      # HTML para renderizar respuestas
 ├──── 📂 models/      # Modelos de IA (YOLO)
 ├──── 📜 app.py         # Código principal de la API
 ├──── 📜 description.py  # Lógica de análisis de imágenes
 ├──── 📜 detection.txt # Detección de imagen usando el modelo de IA
 ├──📜 requirements.txt # Dependencias del proyecto
 ├── 📜 .env           # Variables de entorno (NO subir a GitHub)
 ├── 📜 README.md      # Este archivo
```

---

## **🤖 Tecnologías Usadas**  
- **Python** 
- **FastAPI** (para la API web)
- **YOLOv8** (para la detección de objetos)
- **spacy** (para la descripción de la detección)
- **Jinja2** (para renderizar templates HTML)
- **Deep Translator** (para la traducción de los resultados)
- **Uvicorn** (para correr el servidor)

---

## **📜 Licencia**  
MIT License. ¡Puedes usarlo y modificarlo libremente!  

---