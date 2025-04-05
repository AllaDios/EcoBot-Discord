import discord
import json
from discord.ext import commands

class Project(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.proyectos_data = self.cargar_proyectos()

    def cargar_proyectos(self):
        try:
            with open("data/proyectos.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            print(f"⚠️ Error al cargar proyectos.json: {e}")
            return {"projects": [], "materials": [], "project_materials": []}

    def buscar_proyectos(self, materiales_usuario):
        if not self.proyectos_data:
            return []

        materiales_ids = []
        for material_usuario in materiales_usuario:
            for material in self.proyectos_data.get("materials", []):
                if material_usuario.lower() in material["nombre"].lower():
                    materiales_ids.append(material["id"])
                    break

        if not materiales_ids:
            return []

        proyectos_posibles = {}
        
        for relacion in self.proyectos_data.get("project_materials", []):
            project_id = relacion["project_id"]
            material_id = relacion["material_id"]
            
            if material_id in materiales_ids:
                if project_id not in proyectos_posibles:
                    proyectos_posibles[project_id] = 1
                else:
                    proyectos_posibles[project_id] += 1

        proyectos_ordenados = sorted(proyectos_posibles.items())
        
        resultados = []
        for project_id, _ in proyectos_ordenados:
            for proyecto in self.proyectos_data.get("projects", []):
                if proyecto["id"] == project_id:
                    resultados.append(proyecto)
                    break
        
        return resultados

    @commands.command(
        name="project",
        help="Busca proyectos de reciclaje según los materiales que tengas.\nEjemplo: !project botella cartón",
        aliases=["proyecto"]
    )
    async def project(self, ctx, *materiales):
        if not materiales:
            await ctx.send("⚠️ Debes indicar al menos un material. Ejemplo: `!project botella cartón`")
            return

        proyectos = self.buscar_proyectos(materiales)
        
        if not proyectos:
            materiales_texto = ", ".join(materiales)
            embed = discord.Embed(
                title="🔍 No se encontraron proyectos",
                description=f"No encontré proyectos que puedas hacer con: `{materiales_texto}`\n\nPrueba con otros materiales o revisa que estén bien escritos.",
                color=discord.Color.orange()
            )
            
            materiales_disp = [m["nombre"] for m in self.proyectos_data.get("materials", [])[:10]]
            if materiales_disp:
                embed.add_field(
                    name="Algunos materiales disponibles:",
                    value=", ".join(materiales_disp),
                    inline=False
                )
        else:
            materiales_texto = ", ".join(materiales)
            embed = discord.Embed(
                title=f"♻️ Proyectos para reciclar con {materiales_texto}",
                description=f"He encontrado {len(proyectos)} proyectos que puedes hacer:",
                color=discord.Color.green()
            )
            
            for proyecto in proyectos:
                embed.add_field(
                    name=f"🌱 {proyecto['nombre']}",
                    value=f"**Descripción:** {proyecto['descripcion']}\n**Instrucciones:** {proyecto['instrucciones']}",
                    inline=False
                )
        
        embed.set_footer(text="¡Convierte tus residuos en recursos! ♻️")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Project(bot)) 