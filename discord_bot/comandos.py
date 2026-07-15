from discord_bot.discord import bot
from funciones.gemini import preguntar_ia
from funciones.memoria import tareas, usuarios_activos, conocimiento_base, historial_ia, guardar_datos, RUTA_TAREAS, RUTA_HISTORIAL
from datetime import datetime

def buscar_en_base(texto):
    texto = texto.lower()
    for clave in conocimiento_base:
        if clave in texto:
            return conocimiento_base[clave]
    return None

@bot.command()
async def ai(ctx, *, pregunta):
    usuarios_activos.add(ctx.author.name)

    respuesta = buscar_en_base(pregunta)

    if respuesta is None:
        async with ctx.typing():
            respuesta = await preguntar_ia(pregunta)

    texto = str(respuesta)

    for i in range(0, len(texto), 1900):
        await ctx.send(f"🤖 {texto[i:i+1900]}")

    historial_ia.append({
        "pregunta": pregunta,
        "respuesta": respuesta,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    guardar_datos(RUTA_HISTORIAL, historial_ia)

@bot.command()
async def hola(ctx):
    await ctx.send(f"Hola {ctx.author.mention}!")

@bot.command()
async def tarea(ctx, *, texto=None):

    if texto is None:
        await ctx.send("⚠️ Escribe una tarea. Ejemplo: !tarea estudiar Python")
        return

    tareas.append({
        "usuario": ctx.author.name,
        "texto": texto,
        "estado": "pendiente"
    })

    guardar_datos(RUTA_TAREAS, tareas)

    await ctx.send("📌 Tarea guardada correctamente")

@bot.command(name="tareas")
async def tareas_list(ctx):

    if len(tareas) == 0:
        await ctx.send("📚 No tienes tareas registradas.")
        return

    mensaje = "📚 **TAREAS REGISTRADAS**\n\n"

    for i, tarea in enumerate(tareas, start=1):
        mensaje += f"{i}. {tarea['texto']} - {tarea['estado']}\n"

    await ctx.send(mensaje)


@bot.command()
async def stats(ctx):
    await ctx.send(f"Tareas: {len(tareas)} | Usuarios: {len(usuarios_activos)} | IA: {len(historial_ia)}")
    
@bot.command()
async def historial(ctx):

    if len(historial_ia) == 0:
        await ctx.send("🧠 No existe historial de preguntas todavía.")
        return

    mensaje = "🧠 **ÚLTIMAS PREGUNTAS A LA IA**\n\n"

    for i, h in enumerate(historial_ia[-5:], start=1):

        pregunta = h["pregunta"]
        fecha = h["fecha"]

        mensaje += f"**{i}.** {pregunta}\n"
        mensaje += f"📅 {fecha}\n\n"


    await ctx.send(mensaje)    



@bot.command()
async def fecha(ctx):

    hoy = datetime.now()

    await ctx.send(
        f"📅 Hoy es {hoy.strftime('%A, %d/%m/%Y')}"
    )

@bot.command()
async def ayuda(ctx):
    mensaje = """
🤖 **StudyBot AI - Comandos disponibles**

📚 **Comandos de IA**
!ai [pregunta]
→ Realiza una pregunta a la inteligencia artificial

📝 **Gestión de tareas**
!tarea [texto]
→ Guarda una nueva tarea

!tareas
→ Muestra tus tareas registradas

🧠 **Historial**
!historial
→ Muestra preguntas anteriores a la IA

📊 **Información**
!stats
→ Muestra estadísticas del bot

📅 **Fecha**
!fecha
→ Muestra la fecha actual del sistema

👋 **General**
!hola
→ Saludo del bot
"""

    await ctx.send(mensaje)
