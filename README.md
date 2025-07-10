# 🔮 Tarotista Virtual - API Backend

Una API desarrollada con FastAPI que alimenta una aplicación móvil de tarot virtual. Esta API procesa consultas de los usuarios y las envía a modelos de IA especializados a través de OpenRouter, devolviendo lecturas de tarot personalizadas y místicas.

## ✨ Características

- 🚀 **API RESTful** construida con FastAPI
- 🤖 **Integración con múltiples modelos de IA** via OpenRouter
- 🎯 **Respuestas especializadas** con prompt de sistema personalizado
- ⚡ **Rendimiento optimizado** con medición de tiempos de respuesta
- 🌐 **CORS configurado** para integración con aplicaciones móviles
- 📱 **Diseñada para Flutter** como cliente principal

## 🛠️ Tecnologías Utilizadas

- **FastAPI** - Framework web moderno y rápido
- **OpenAI SDK** - Cliente para comunicación con APIs de IA
- **OpenRouter** - Plataforma de acceso a múltiples modelos de IA
- **Pydantic** - Validación de datos y serialización
- **Python-dotenv** - Gestión de variables de entorno

## 📋 Modelos de IA Disponibles

| Modelo | Identificador | Descripción |
|--------|---------------|-------------|
| **DeepSeek V3** | `deepseek/deepseek-chat-v3-0324:free` | Modelo gratuito de alta calidad |
| **Llama 3.3** | `meta-llama/llama-3.3-70b-instruct:free` | Modelo Meta gratuito |
| **WizardLM** | `microsoft/wizardlm-2-8x22b` | Modelo Microsoft (por defecto) |
| **Dolphin/Mistral** | `cognitivecomputations/dolphin3.0-r1-mistral-24b:free` | Modelo especializado gratuito |

## 🚀 Instalación y Configuración

### Prerequisitos

- Python 3.8+
- pip (gestor de paquetes de Python)
- Cuenta en OpenRouter con API key

### 1. Clonar el repositorio

```bash
git clone https://github.com/Secallona/MorganaAPI.git
cd MorganaAPI
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install fastapi uvicorn openai python-dotenv pydantic
```

### 4. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
OPENAI_API_KEY=tu_openrouter_api_key_aqui
```

### 5. Crear archivo de prompt del sistema

Crear un archivo `system_prompt.txt` con las instrucciones para la IA:

```txt
Eres una tarotista virtual experta con décadas de experiencia en la lectura de cartas del tarot.
Respondes con sabiduría mística, utilizando un lenguaje poético y evocador.
Siempre ofreces interpretaciones positivas y constructivas, ayudando a las personas a reflexionar sobre su vida.
[Agregar más instrucciones específicas según sea necesario]
```

## 🎯 Uso de la API

### Ejecutar el servidor

```bash
uvicorn main:app --reload
```

El servidor estará disponible en `http://localhost:8000`

### Documentación automática

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Endpoint principal

**POST** `/generate`

Genera una respuesta de tarot basada en el prompt del usuario.

#### Parámetros de consulta

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `prompt` | string | ✅ | La consulta o pregunta del usuario |

#### Ejemplo de uso

```bash
curl -X POST "http://localhost:8000/generate?prompt=¿Qué me depara el futuro en el amor?" \
  -H "Content-Type: application/json"
```

#### Respuesta exitosa

```json
{
  "response": "Las cartas revelan que en tu camino amoroso se aproximan cambios transformadores..."
}
```

#### Respuesta con error

```json
{
  "error": "Descripción del error"
}
```

## 📁 Estructura del Proyecto

```
tarotista-virtual-api/
├── app/
│   ├── api/
│   │   └── routes.py          # Rutas de la API
│   ├── core/
│   │   ├── config.py          # Configuración y settings
│   │   └── system_prompt.py   # Gestión del prompt del sistema
│   ├── models/
│   │   └── prompt_request.py  # Modelos de datos Pydantic
│   └── services/
│       └── ai_service.py      # Lógica de comunicación con IA
├── main.py                    # Aplicación principal FastAPI
├── system_prompt.txt          # Instrucciones para la IA
├── .env                       # Variables de entorno
└── README.md                  # Este archivo
```

## 🔧 Configuración Avanzada

### Cambiar modelo de IA

Modifica el archivo `app/core/config.py` para cambiar el modelo por defecto:

```python
# En ai_service.py, línea de model
model=settings.MODELS['DeepSeekV3'],  # Cambiar por el modelo deseado
```

### Personalizar CORS

Modifica `ALLOWED_ORIGINS` en `config.py`:

```python
ALLOWED_ORIGINS = ["http://localhost:3000", "https://miapp.com"]
```

## 📱 Integración con Flutter

La API está diseñada para funcionar perfectamente con aplicaciones Flutter. Ejemplo de integración:

```dart
final response = await http.post(
  Uri.parse('http://your-api-url/generate?prompt=${userPrompt}'),
  headers: {'Content-Type': 'application/json'},
);
```

## 🐛 Resolución de Problemas

### Error: "API Key not found"
- Verifica que el archivo `.env` existe y contiene `OPENAI_API_KEY`
- Asegúrate de que la API key de OpenRouter es válida

### Error: "Module not found"
- Verifica que todas las dependencias están instaladas
- Asegúrate de que el entorno virtual está activado

### Error de CORS
- Verifica la configuración de `ALLOWED_ORIGINS` en `config.py`
- Asegúrate de incluir el dominio desde donde se hacen las peticiones

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🔗 Enlaces Útiles

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenRouter API](https://openrouter.ai/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

---

*Desarrollado con ❤️ para conectar la sabiduría ancestral del tarot con la tecnología moderna*
