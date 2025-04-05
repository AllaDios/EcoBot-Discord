# Guía de Instalación de EcoBot 🌱

Esta guía proporciona instrucciones detalladas para instalar y configurar EcoBot en tu servidor de Discord.

## Requisitos Previos

1. **Python 3.8+**: Verifica tu versión con `python --version` o `python3 --version`
2. **Git**: Para clonar el repositorio
3. **Discord Developer Account**: Para crear y configurar el bot

## Pasos de Instalación

### 1. Configuración del Bot en Discord

1. Ve a [Discord Developer Portal](https://discord.com/developers/applications)
2. Haz clic en "New Application" y dale un nombre (por ejemplo, "EcoBot")
3. Ve a la sección "Bot" y haz clic en "Add Bot"
4. Bajo la sección "TOKEN", haz clic en "Copy" para copiar tu token
5. Activa los siguientes "Privileged Gateway Intents":
   - Presence Intent
   - Server Members Intent
   - Message Content Intent
6. Ve a la sección "OAuth2" > "URL Generator"
   - Selecciona el scope "bot"
   - Selecciona los permisos: "Send Messages", "Read Messages/View Channels", "Embed Links"
   - Copia la URL generada y úsala para invitar al bot a tu servidor

### 2. Instalación del Código

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/EcoBot-Discord.git
cd EcoBot-Discord

# Instalar dependencias
pip install -r requirements.txt
```

### 3. Configuración del Entorno

1. Crea un archivo `.env` en la raíz del proyecto:
   ```
   DISCORD_TOKEN=tu_token_copiado_del_portal_de_desarrolladores
   PREFIX=!
   ```


### 4. Iniciar el Bot

```bash
# Asegúrate de que el entorno virtual está activado
python src/bot.py
```

Deberías ver un mensaje confirmando que el bot está conectado.

## Solución de Problemas

### Error al Cargar el Token
- Asegúrate de que el archivo `.env` está en la ubicación correcta
- Verifica que el token sea válido y esté correctamente copiado

### Error con los Comandos
- Asegúrate de que los permisos del bot en Discord sean adecuados

### Error con los Intents
- Verifica que hayas activado los intents necesarios en el portal de desarrolladores de Discord

## Soporte

Si encuentras algún problema durante la instalación, puedes:
- Abrir un issue en el repositorio de GitHub
- Revisar la documentación oficial de Discord.py en [discord.py](https://discordpy.readthedocs.io/) 