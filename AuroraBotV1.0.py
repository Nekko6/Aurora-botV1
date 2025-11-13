import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

##### EVENTOS #####

@bot.event
async def on_ready():
    sincs = await bot.tree.sync()
    print(f"{len(sincs)} comandos sincronizados.")
    print(f'Bom dia Aurora {bot.user.name} - {bot.user.id}')

@bot.event
async def on_member_join(member: discord.Member):
    canal = bot.get_channel(1280444833600897096)
    await canal.send(f"🔔 Tring tring! 🔔\n{member.mention} é o nosso novo cliente🧋")

    join_embed = discord.Embed()
    join_embed.title = "Bem-vindo ao Servidor!"
    join_embed.description = "Estamos felizes em ter você aqui. Aproveite sua estadia!"
    join_embed.set_image(
        url="https://i.pinimg.com/originals/bf/88/a9/bf88a9cad16364149a4e307d66659870.gif"
    )

    await canal.send(embed=join_embed)


##### TREE COMANDOS #####

@bot.tree.command()
async def ola(interaction: discord.Interaction):
    await interaction.response.send_message(
        f'Olá🩵, {interaction.user.mention}! Como posso ajudar você hoje?'
    )


@bot.tree.command()
async def ajuda(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Os meus comandos são esses:\n"
        "/ola → Eu digo oi 👋\n"
        "/ajuda → Mostra os comandos\n"
    )


@bot.tree.command()
async def safada(interaction: discord.Interaction):
    await interaction.response.send_message(f'{interaction.user.mention}, sua safada!')


##### COMANDOS COMUNS #####

@bot.command()
async def join_embed(ctx: commands.Context):
    join_embed = discord.Embed()
    join_embed.title = "Bem-vindo ao Servidor!"
    join_embed.description = "Estamos felizes em ter você aqui. Aproveite sua estadia!"
    await ctx.reply(embed=join_embed)

bot.run("seu token
")
