import discord
from discord.ext import commands
from funciones.logs import registrar_error


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_command_error(ctx, error):

    registrar_error(
        error,
        ctx.author.name,
        ctx.message.content
    )

    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Ese comando no existe. Usa !ayuda")

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("⚠️ Faltan datos para ejecutar ese comando.")

    else:
        await ctx.send("⚠️ Ocurrió un error y fue registrado.")
