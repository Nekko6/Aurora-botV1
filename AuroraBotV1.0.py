import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

##### coversa #####
conversas = {
    "boa noite": "Boa noite🌙! Tenha uma ótima noite de sono!",
    "bom dia": "Bom dia☀️! Que seu dia seja incrível!",
    "boa tarde": "Boa tarde🌤️! Espero que esteja tendo um ótimo dia!",
    "oi": "Olá🩵! Como posso ajudar você hoje?",
}

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "boa noite" in message.content.lower():
        await message.channel.send(f'Boa noite🌙, {message.author.mention}!Tenha uma ótima noite de sono!')

    if "bom dia" in message.content.lower():
        await message.channel.send(f'Bom dia☀️, {message.author.mention}! Que seu dia seja incrível!')

    if "boa tarde" in message.content.lower():
        await message.channel.send(f'Boa tarde🌤️, {message.author.mention}! Espero que esteja tendo um ótimo dia!')

    if "oi" in message.content.lower():
        await message.channel.send(f'Olá🩵, {message.author.mention}! Como posso ajudar você hoje?')

    await bot.process_commands(message)

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

'''@bot.event
async def on_ready():
 canal = bot.get_channel(1280230866811093004)
 await canal.send(" Bom dia")'''

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

@bot.tree.command()
async def youtube(interaction: discord.Interaction):
    await interaction.response.send_message(f'{interaction.user.mention}, confira o canal do meu criador\n'f'https://www.youtube.com/@NeKko_San64')

##### VOICE CLIENTS COMANDOS #####

    


##### COMANDOS COMUNS #####

@bot.command()
async def join_embed(ctx: commands.Context):
    join_embed = discord.Embed()
    join_embed.title = "Bem-vindo ao Servidor!"
    join_embed.description = "Estamos felizes em ter você aqui. Aproveite sua estadia!"
    await ctx.reply(embed=join


bot.run("SEU TOKEN")


