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

2. **Crea un entorno virtual**:
   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```

4. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configura las variables de entorno**:
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

## 📁 Estructura del Proyecto

```
EcoBot-Discord/
├── data/
│   └── consejos.json      # Base de datos de consejos ecológicos
├── docs/
│   └── README.md          # Documentación
├── src/
│   ├── command/
│   │   └── tips.py        # Comando para mostrar consejos
│   └── bot.py             # Archivo principal del bot
├── .env                   # Variables de entorno
└── requirements.txt       # Dependencias
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:
1. Haz un fork del proyecto
2. Crea una rama para tu característica
3. Haz commit de tus cambios
4. Envía un pull request

## 📜 Licencia

Este proyecto está bajo la licencia MIT.
