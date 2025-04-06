import discord
import random
import json
from discord.ext import commands

class Materials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.materiales = self.cargar_materiales()

    def cargar_materiales(self):
        try:
            with open("data/materiales.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            print(f"⚠️ Error al cargar materiales.json: {e}")
            return {}

    @commands.command(
        name="materiales",
        help="Muestra un proyecto aleatorio o a partir de materiales específicos.\nCategorías disponibles: orgánicos, reciclables, reutilizables",
        aliases=["material"]
    )
    async def tips(self, ctx, categoria: str = None):
        if not self.materiales:
            await ctx.send("⚠️ No se encontraron materiales en la base de datos.")
            return

        if categoria:
            categoria = categoria.lower()
            if categoria in self.materiales:
                idea = random.choice(self.materiales[categoria])
                embed = discord.Embed(
                    title=f"💡 Idea con {categoria.capitalize()}",
                    description=idea,
                    color=discord.Color.green()
                )
            else:
                categorias_disponibles = ", ".join(self.materiales.keys())
                embed = discord.Embed(
                    title="🚫 Material no encontrado",
                    description=f"Los materiales disponibles son: `{categorias_disponibles}`",
                    color=discord.Color.red()
                )
        else:
            categoria_random = random.choice(list(self.materiales.keys()))
            idea = random.choice(self.materiales[categoria_random])
            embed = discord.Embed(
                title=f"💡 Idea con {categoria_random.capitalize()}",
                description=idea,
                color=discord.Color.green()
            )

        embed.set_footer(text="¡Convierte tus residuos en recursos! ♻️")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Materials(bot))