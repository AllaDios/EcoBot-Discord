import discord
import random
import json
from discord.ext import commands

class Materials(commands.Cog):
    def _init_(self, bot):
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
        help="Muestra ideas de materiales o qué materiales están disponibles",
        aliases=["material"]
    )
    async def materials(self, ctx, *, material: str = None):
        if not self.materiales:
            await ctx.send("⚠️ No se encontraron materiales en la base de datos.")
            return

        if material:
            material = material.lower()
            if material in self.materiales:
                idea = random.choice(self.materiales[material])
                embed = discord.Embed(
                    title=f"💡 Idea con {material.capitalize()}",
                    description=idea,
                    color=discord.Color.green()
                )
            else:
                disponibles = ", ".join(f"{k}" for k in self.materiales.keys())
                embed = discord.Embed(
                    title="❌ Material no encontrado",
                    description=f"El material *{material}* no está en la base de datos.\n\n📦 *Materiales disponibles:*\n{disponibles}",
                    color=discord.Color.red()
                )
        else:
            disponibles = ", ".join(f"{k}" for k in self.materiales.keys())
            embed = discord.Embed(
                title="📦 Materiales disponibles",
                description=disponibles,
                color=discord.Color.blue()
            )
            embed.set_footer(text="Usa el comando !materiales <material> para ver una idea con ese material.")

        embed.set_footer(text="¡Convierte tus residuos en recursos! ♻️")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Materials(bot))