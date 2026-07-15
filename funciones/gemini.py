from google import genai
from config import GEMINI_API_KEY
from datetime import datetime

client = genai.Client(api_key=GEMINI_API_KEY)

async def preguntar_ia(pregunta):

    fecha_actual = datetime.now().strftime("%A, %d de %B de %Y")

    contexto = f"""
La fecha actual del sistema es: {fecha_actual}

Si el usuario pregunta por la fecha, día de hoy, hora o información temporal,
usa esta fecha. No inventes fechas.
"""

    respuesta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
{contexto}

Pregunta del usuario:
{pregunta}
"""
    )

    return respuesta.text
