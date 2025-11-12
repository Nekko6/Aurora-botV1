import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

# isso permite ligar a aurora
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

# esse evento permite que a aurora de boas vindas para novos membros
@bot.event
async def on_member_join(member:discord.Member):
    canal = bot.get_channel(1280444833600897096)
    await canal.send(f"🔔 Tring tring! 🔔\n{member.mention} é o nosso novo cliente🧋")
    join_embed = discord.Embed()
    join_embed.title = "Bem-vindo ao Servidor!"
    join_embed.description = "Estamos felizes em ter você aqui. Aproveite sua estadia!"
    join_embed.set_image(url="https://i.pinimg.com/originals/bf/88/a9/bf88a9cad16364149a4e307d66659870.gif ")
    await canal.send(embed=join_embed)

# dando esse comando a aurora responde com uma saudação
@bot.command()
async def ola(ctx:commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"Olá:blue_heart: , {nome} Eu sou o AuroraBot, como posso ajudar você hoje?")

#aqui a aurora da uma lista dos comandos
@bot.command()
async def ajuda(ctx:commands.Context):
    ajuda_mensagem = (
        "Aqui estão alguns comandos que você pode usar\n"
        ".ola - O bot responde com uma saudação.\n"
        ".ajuda - Mostra esta mensagem de ajuda.\n"
        "Mais comandos serão adicionados em breve!"
    )
    await ctx.reply(ajuda_mensagem)

#aqui eu testo a embed
@bot.command()
async def join_embed(ctx:commands.Context):
   join_embed = discord.Embed()
   join_embed.title = "Bem-vindo ao Servidor!"
   join_embed.description = "Estamos felizes em ter você aqui. Aproveite sua estadia!"
  
#isso permite rodar a aurora
bot.run("")

