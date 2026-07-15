import logging
import os

RUTA_LOGS = "logs/bot.log"


def configurar_logs():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        filename=RUTA_LOGS,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        encoding="utf-8"
    )


def registrar_info(mensaje):
    logging.info(mensaje)


def registrar_error(error, usuario="Desconocido", comando="Desconocido"):
    logging.error(
        f"Usuario: {usuario} | Comando: {comando} | Error: {error}"
    )
