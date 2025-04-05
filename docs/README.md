## 📋 Características

- **Consejos Ecológicos**: Ofrece consejos sobre reciclaje, ahorro de agua, energía y más.
- **Categorías Temáticas**: Incluye consejos específicos para baño, cocina, jardín, reciclaje y compostaje.
- **Interfaz Amigable**: Comandos intuitivos con respuestas visuales atractivas.

## 🔧 Requisitos

- Python 3.8 o superior
- Una cuenta de Discord y un token de bot
- Conexión a internet

## 🚀 Instalación

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/EcoBot-Discord.git
   cd EcoBot-Discord
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura las variables de entorno**:
   - Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
     ```
     DISCORD_TOKEN=tu_token_de_discord
     PREFIX=!
     ```

## 🎮 Uso

1. **Inicia el bot**:
   ```bash
   python src/bot.py
   ```

2. **Comandos disponibles**:
   - `!tips`: Muestra un consejo aleatorio
   - `!tips [categoría]`: Muestra un consejo de la categoría especificada (baño, cocina, jardín, reciclaje, compostaje)
