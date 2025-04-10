import discord
import requests
from discord.ext import commands
from datetime import datetime, timedelta

class NasaEonet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.base_url = "https://eonet.gsfc.nasa.gov/api/v3"
        self.tipos = {
            "sequias": "drought", 
            "tormentas": "severeStorms",
            "volcanes": "volcanoes", 
            "incendios": "wildfires",
            "inundaciones": "floods",
            "hielo": "seaLakeIce"
        }
        
    @commands.command(
        name="eventos",
        help="Muestra desastres naturales. Tipos: sequias, tormentas, volcanes, incendios, inundaciones, hielo",
        aliases=["nasa"]
    )
    async def eventos(self, ctx, tipo=None, dias=30):
        if dias > 60:
            dias = 60
            
        fecha = (datetime.now() - timedelta(days=dias)).strftime("%Y-%m-%d")
        url = f"{self.base_url}/events?status=open&start={fecha}"
        
        # Si pusieron un tipo específico, cambiamos la URL
        if tipo:
            tipo = tipo.lower()
            if tipo in self.tipos:
                tipo_en_ingles = self.tipos[tipo]
                url = f"{self.base_url}/categories/{tipo_en_ingles}?status=open&start={fecha}"
                titulo = f"🌍 Desastres de {tipo} en los últimos {dias} días"
            else:
                tipos_disponibles = ", ".join(self.tipos.keys())
                embed = discord.Embed(
                    title="❌ Error: Tipo no encontrado",
                    description=f"Los tipos que puedes usar son: `{tipos_disponibles}`",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed)
                return
        else:
            titulo = f"🌍 Desastres naturales de los últimos {dias} días"
        
        try:
            respuesta = requests.get(url)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                eventos = datos.get("events", [])
                if not eventos:
                    embed = discord.Embed(
                        title="🌍 No hay desastres",
                        description=f"¡Buenas noticias! No encontré desastres para ese período.",
                        color=discord.Color.blue()
                    )
                    await ctx.send(embed=embed)
                    return
                
                if len(eventos) > 10:
                    eventos = eventos[:10]
                
                embed = discord.Embed(
                    title=titulo,
                    description=f"Información de la NASA 🚀",
                    color=discord.Color.blue(),
                    url="https://eonet.gsfc.nasa.gov/"
                )
                
                for evento in eventos:
                    # Guardamos el nombre del evento
                    nombre = evento.get("title", "Evento sin nombre")
                    
                    # PARTE 1: SACAMOS LA FECHA DE MANERA SENCILLA
                    # Primero asumimos que no sabemos la fecha
                    fecha_mostrar = "Fecha desconocida"
                    
                    # Vemos si el evento tiene información de geometría
                    if "geometry" in evento and evento["geometry"]:
                        # Si tiene geometría, intentamos sacar la fecha del primer elemento
                        geometria = evento["geometry"][0]  # Tomamos el primer elemento
                        
                        # Vemos si tiene fecha
                        if "date" in geometria:
                            # Encontramos la fecha, ahora la convertimos a formato bonito
                            fecha_texto = geometria["date"]
                            
                            # La API de NASA usa "Z" al final, lo cambiamos a formato que Python entiende
                            fecha_texto = fecha_texto.replace("Z", "+00:00")
                            
                            # Convertimos el texto a una fecha real
                            try:
                                fecha_objeto = datetime.fromisoformat(fecha_texto)
                                
                                # Ahora la convertimos a formato día/mes/año
                                fecha_mostrar = fecha_objeto.strftime("%d/%m/%Y")
                            except:
                                # Si algo falla, seguimos con "Fecha desconocida"
                                fecha_mostrar = "Fecha desconocida"
                    
                    # PARTE 2: SACAMOS LAS COORDENADAS DE MANERA SENCILLA
                    # Primero asumimos que no hay coordenadas
                    coordenadas = ""
                    
                    # Vemos si el evento tiene información de geometría
                    if "geometry" in evento and evento["geometry"]:
                        # Si tiene geometría, intentamos sacar coordenadas del primer elemento
                        geometria = evento["geometry"][0]  # Tomamos el primer elemento
                        
                        # Vemos si tiene coordenadas
                        if "coordinates" in geometria:
                            # Encontramos coordenadas, vemos si tienen el formato esperado
                            coords = geometria["coordinates"]
                            
                            # Las coordenadas deben ser una lista con al menos dos números
                            if isinstance(coords, list) and len(coords) >= 2:
                                # El primer número es longitud, el segundo es latitud
                                longitud = coords[0]
                                latitud = coords[1]
                                
                                # Creamos el enlace a Google Maps
                                coordenadas = f"📍 [Ver en mapa](https://www.google.com/maps/search/?api=1&query={latitud},{longitud})"
                    
                    # Juntamos toda la información y la añadimos al mensaje
                    info = f"Fecha: {fecha_mostrar}"
                    
                    # Solo añadimos el enlace al mapa si encontramos coordenadas
                    if coordenadas:
                        info = info + f"\n{coordenadas}"
                        
                    # Añadimos la información al mensaje
                    embed.add_field(name=nombre, value=info, inline=False)
                
                # Añadimos un pie de página
                embed.set_footer(text="Datos de NASA | ♻️ EcoBot")
                
                # Añadimos un consejo de reciclaje según el tipo de desastre
                if tipo == "incendios":
                    embed.add_field(
                        name="♻️ Consejo de reciclaje",
                        value="Reciclar papel ayuda a prevenir incendios porque se talan menos árboles.",
                        inline=False
                    )
                elif tipo == "inundaciones":
                    embed.add_field(
                        name="♻️ Consejo de reciclaje",
                        value="Reciclar plásticos evita que tapen desagües y causen inundaciones.",
                        inline=False
                    )
                    
                # Enviamos el mensaje
                await ctx.send(embed=embed)
            else:
                # Si hubo un error con la API
                embed = discord.Embed(
                    title="❌ Error",
                    description=f"No pude conectar con la NASA. Error: {respuesta.status_code}",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed)
        except Exception as e:
            # Si ocurrió cualquier otro error
            embed = discord.Embed(
                title="❌ Error",
                description=f"Algo salió mal: {str(e)}",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

# Esta función es necesaria para que Discord cargue nuestro comando
async def setup(bot):
    await bot.add_cog(NasaEonet(bot)) 