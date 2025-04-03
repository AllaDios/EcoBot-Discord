import discord
import random
import json
from discord.ext import commands

class Tips(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.consejos = self.cargar_consejos()

    def cargar_consejos(self):
        """Carga los consejos desde el archivo JSON al iniciar el cog."""
        try:
            with open("data/consejos.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            print(f"⚠️ Error al cargar consejos.json: {e}")
            return {}

    @commands.command(name="tips", help="Muestra un consejo aleatorio o de una categoría específica.")
    async def tips(self, ctx, categoria: str = None):
        """Envia un consejo aleatorio o de una categoría específica."""
        if not self.consejos:
            await ctx.send("⚠️ No se encontraron consejos en la base de datos.")
            return

        if categoria:
            categoria = categoria.lower()
            if categoria in self.consejos:
                consejo = random.choice(self.consejos[categoria])
                embed = discord.Embed(
                    title=f"🌱 Consejo sobre {categoria.capitalize()}",
                    description=consejo,
                    color=discord.Color.green()
                )
            else:
                categorias_disponibles = ", ".join(self.consejos.keys())
                embed = discord.Embed(
                    title="🚫 Categoría no encontrada",
                    description=f"Las categorías disponibles son: `{categorias_disponibles}`",
                    color=discord.Color.red()
                )
        else:
            categoria_random = random.choice(list(self.consejos.keys()))
            consejo = random.choice(self.consejos[categoria_random])
            embed = discord.Embed(
                title=f"🌱 Consejo de {categoria_random.capitalize()}",
                description=consejo,
                color=discord.Color.green()
            )

        embed.set_footer(text="¡Pequeñas acciones generan grandes cambios! ♻️")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Tips(bot))
