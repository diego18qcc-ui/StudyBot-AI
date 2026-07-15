from discord_bot.discord import bot
from config import DISCORD_TOKEN
import discord_bot.comandos

from funciones.logs import configurar_logs, registrar_info

configurar_logs()


@bot.event
async def on_ready():
    print(f"🤖 StudyBot AI activo como {bot.user}")
    registrar_info(f"Bot iniciado correctamente como {bot.user}")


bot.run(DISCORD_TOKEN)
