# PROYECTO DE CHATBOT DE DISCORD AI

------Semana 16-----

# 🤖 StudyBot AI

## Bot inteligente desarrollado en Python para Discord con integración de Gemini AI

---

## 📌 Descripción del proyecto

**StudyBot AI** es un bot desarrollado en Python para la plataforma Discord, diseñado como un asistente inteligente para apoyar actividades académicas.

El bot permite a los usuarios realizar consultas mediante inteligencia artificial utilizando la API de **Gemini**, gestionar tareas pendientes, almacenar historial de consultas y registrar eventos importantes del sistema.

El proyecto aplica conceptos fundamentales de programación como funciones, módulos, estructuras de datos, manejo de archivos y control de errores mediante un sistema de logs.

---

# 🎯 Objetivo del proyecto

Desarrollar un asistente inteligente integrado en Discord que permita automatizar consultas, organización de actividades y almacenamiento de información utilizando Python e inteligencia artificial.

---

# ⚙️ Funcionalidades principales

## 🧠 Inteligencia Artificial

- Responde consultas realizadas por los usuarios.
- Utiliza Gemini AI para generar respuestas.
- Permite interactuar mediante comandos personalizados.

---

## 📋 Gestión de tareas

- Registro de actividades pendientes.
- Consulta de tareas almacenadas.
- Persistencia de información mediante archivos JSON.

---

## 📚 Historial de consultas

- Guarda las interacciones realizadas con el bot.
- Permite conservar información importante del usuario.

---

## 📝 Sistema de Logs

El bot cuenta con un sistema de registro automático mediante archivos `.log`.

Permite almacenar:

- Inicio del bot.
- Ejecución de comandos.
- Errores encontrados durante la ejecución.
- Información del usuario y comando asociado al error.

Los registros son almacenados en:

logs/bot.log 

---

# 🛠️ Tecnologías utilizadas

## Python

Lenguaje principal utilizado para desarrollar la lógica del bot.

---

## Discord.py

Biblioteca utilizada para conectar Python con Discord y gestionar comandos.

---

## Gemini API

Servicio de inteligencia artificial utilizado para generar respuestas.

---

## JSON

Formato utilizado para almacenar información persistente:

- tareas
- historial de consultas

---

## Logging

Módulo utilizado para generar registros automáticos del sistema.

---

# 📂 Estructura del proyecto

STUDY_BOT

│
├── main.py
│
├── config.py
│
├── discord_bot
│ ├── discord.py
│ └── comandos.py
│
├── funciones
│ ├── gemini.py
│ ├── memoria.py
│ └── logs.py
│
├── data
│ ├── tareas.json
│ └── historial.json
│
└── logs
└── bot.log


---

# 🚀 Instalación y configuración

## 1. Clonar el proyecto

git clone URL_DEL_REPOSITORIO

---

## 2. Instalar dependencias

Ejecutar:


pip install -r requirements.txt


Dependencias principales:


discord.py
google-generativeai
python-dotenv


---

## 3. Configurar variables

Crear un archivo:

.env

Agregar:

DISCORD_TOKEN=tu_token_discord
GEMINI_API_KEY=tu_api_key


---

# ▶️ Ejecución del bot

Ejecutar:

python main.py

Si la conexión es correcta aparecerá:

🤖 StudyBot AI activo

Además se generará automáticamente:

logs/bot.log

---

# 💬 Comandos disponibles

## Consulta con inteligencia artificial

!ai pregunta

Ejemplo:

!ai explica qué es Python

---

## Registrar tarea


!tarea nombre_de_tarea

Ejemplo:

!tarea estudiar programación

---

## Ver historial

!historial

---

## Ver ayuda

!ayuda

---

# 🧪 Pruebas realizadas

Durante las pruebas del sistema se verificó:

✅ Conexión correcta con Discord.

✅ Respuesta mediante Gemini AI.

✅ Registro de tareas.

✅ Guardado de información en archivos JSON.

✅ Generación automática de archivos LOG.

✅ Control de errores durante la ejecución.

---

# 📌 Conclusiones

El desarrollo de StudyBot AI permitió aplicar conceptos fundamentales de programación utilizando Python, integrando servicios externos como Discord y Gemini AI.

Además, la implementación del sistema de logs permitió mejorar la administración del bot, facilitando la identificación de errores y el seguimiento de eventos durante su funcionamiento.

El proyecto demuestra cómo Python puede utilizarse para crear aplicaciones inteligentes, organizadas y escalables.

---
