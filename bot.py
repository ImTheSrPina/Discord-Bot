
import discord, requests, openai, aiohttp, random


from discord.ext import commands
from aiohttp import ClientSession




## ===========================//  PREFIXES E INTENCIONES DEL BOT //============================ ##

def get_prefix(bot, message):
    prefixes = ['+ ',    '+']
    for prefix in prefixes:
        if message.content.startswith(prefix):
            return prefix 
    return "+"   ##DEFAULT PREFIX

bot = commands.Bot(command_prefix= get_prefix, intents = discord.Intents.all())

async def getWaifu(tag):
        async with ClientSession() as resp:
            async with resp.get(f"https://api.waifu.im/search/?included_tags={tag}") as response:
                data = await response.json()
        return data['images'][0]['url']


## ===========================//  CARGA DE API/TOKEN //============================ ##


openai.api_key=("YOUR-API-KEY")


## ===========================//  ENVENTOS DEL BOT  //============================ ##

@bot.event
async def on_ready():
    print(f"Soy {bot.user} y estoy en linea")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("https://waifly.com"))
    try:
        sync = await bot.tree.sync()
        print(f"Sincronizados {len(sync)} comandos slash")
    except Exception as e:
        print(e)
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Sólo puedes usar este comando un número limitado de veces, quedan {round(error.retry_after, 2)} segundos para que puedas usar de nuevo este comando")
    
    
## ===========================//  COMANDOS DE MODERACION  //============================ ##
    
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, usuario: discord.Member, *, razon="Sin motivo"):
    await ctx.guild.ban(usuario) 
    embMod=discord.Embed(title= "¡¡Expulsado!!", description="Un miembro ha sido expulsado", color=0xFF0000)
    embMod.add_field(name= "Nombre", value=f"{usuario.mention}")
    embMod.add_field(name= "Motivo", value=f"{razon}")
    await ctx.send(embed=embMod)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, usuario: discord.Member, *, razon="Sin motivo"):
    await ctx.guild.ban(usuario) 
    embMod=discord.Embed(title= "¡¡Baneado!!", description="¡¡Un miembro ha sido baneado!!", color=0xFF0000)
    embMod.add_field(name= "Nombre", value=f"{usuario.mention}")
    embMod.add_field(name= "Motivo", value=f"{razon}")
    await ctx.send(embed=embMod)
    
@bot.command()
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def unban(ctx, userID):
    user= discord.Object(id=userID)
    await ctx.guild.unban(user)
    emb = discord.Embed(color= 0xFF0000, title="¡¡Ban!!", description="")
    await ctx.send(embed=emb)
    
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, count: int):
    await ctx.channel.purge(limit=count)
    embMod=discord.Embed(title= "Mensajes eliminados", description="Se han eliminado los mensajes", color=0xFF0000)
    embMod.add_field(name= "Mensajes eliminados:", value=f"{count} mensajes")
    await ctx.send(embed=embMod)

    
## ===========================//  COMANDOS SLASH DEL BOT  //============================ ##


@bot.tree.command(name = "dog", description = "Muestra un perro :) ")
async def dog(interaction: discord.Interaction):
    dogAPI = requests.get("https://dog.ceo/api/breeds/image/random")
    dog = dogAPI.json()["message"]
    emb = discord.Embed(color= 0xa18262)
    emb.set_image(url=dog)
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "badwaifu", description = "Muestra una waifu")
async def badwaifu(interaction: discord.Interaction):
    animeAPI = requests.get("https://api.waifu.pics/nsfw/waifu")
    waifu = animeAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB)
    emb.set_image(url=waifu)
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "badneko", description = "Muestra una chica gato")
async def badneko(interaction: discord.Interaction):
    animeAPI = requests.get("https://api.waifu.pics/nsfw/neko")
    waifuNeko = animeAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "blowjob", description = "Muestra una mamada... Literalemte")
async def blowjob(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/blowjob/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "hentai", description = "Muestra hentai :) ")
async def hentai(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("hentai"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "milf", description = "Muestra una milf")
async def milf(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("milf"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "ass", description = "Muestra un culo")
async def ass(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("ass"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "oral", description = "Muestra una mamada... pero desde otra API")
async def oral(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("oral"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "paizuri", description = "Sinceramente, no se que significa esto")
async def paizuri(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("paizuri"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "ecchi", description = "Muestra una imagen ecchi")
async def ecchi(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("ecchi"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "ero", description = "Muestra una imagen erotica")
async def ero(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("ero"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "neko", description = "Muestra un neko")
async def neko(interaction: discord.Interaction):
    animeAPI = requests.get("https://api.waifu.pics/sfw/neko")
    waifuNeko = animeAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB)
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "awoo", description = "Awooooo")
async def awoo(interaction: discord.Interaction):
    awooAPI = requests.get("https://api.waifu.pics/sfw/awoo")
    awoo = awooAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB)
    emb.set_image(url=awoo)
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "maid", description = "Muestra una maid")
async def maid(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("maid"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "waifu", description = "Muestra una waifu")
async def waifu(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("waifu"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "marin-kitagawa", description = "Muestra una imagen de Marin Kitagawa")
async def marin(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("marin-kitagawa"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "mori-calliope", description = "Muestra una imagen de Mori Calliope")
async def mori(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("mori-calliope"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "raiden-shogun", description = "Muestra una imagen de Raiden Shogun")
async def raiden(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("raiden-shogun"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "oppai", description = "Tu y yo sabemos que hace esto...")
async def oppai(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("oppai"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "selfies", description = "Selfie 📷 ")
async def selfies(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("selfies"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "uniform", description = "Colegialas")
async def uniform(interaction: discord.Interaction):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("uniform"))
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "megumin", description = "¡¡Explosion!! ")
async def megumin(interaction: discord.Interaction):
    explosionAPI = requests.get("https://api.waifu.pics/sfw/megumin")
    explosion = explosionAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB)
    emb.set_image(url=explosion)
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "shinobu", description = "¿?")
async def shinobu(interaction: discord.Interaction):
    explosionAPI = requests.get("https://api.waifu.pics/sfw/shinobu")
    explosion = explosionAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB)
    emb.set_image(url=explosion)
    await interaction.response.send_message(embed=emb)
    
@bot.tree.command(name = "trap", description = "¡¡Es una trampa!!")
async def trap(interaction: discord.Interaction):
    explosionAPI = requests.get("https://api.waifu.pics/sfw/trap")
    explosion = explosionAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB)
    emb.set_image(url=explosion)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "anal", description = "Muestra un anal")
async def anal(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/anal/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "cum", description = "Me corro haaaa")
async def cum(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/cum/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "fuck", description = "Joder, estan follando en la cocina")
async def fuck(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/fuck/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "pussylick", description = "Deja de decir mamadas, y mejor dalas")
async def pussylick(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/pussylick/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "solo", description = "Una waifu sola solita")
async def solo(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/solo/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "triofff", description = "Este comando muestra un trio que consiste en tres waifus")
async def triofff(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/threesome_fff/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "trioffm", description = "Este comando muestra un trio que consiste en dos waifus y un hombre")
async def trioffm(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/threesome_ffm/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "triommf", description = "Este comando muestra un trio que consiste en una waifu y dos hombres")
async def triommf(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/threesome_mmf/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "yuri", description = "Este comando muestra yuri, simplemente yuri")
async def yuri(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/yuri/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "yaoi", description = "No me gustan este tipo de cosas, pero estoy seguro que hay gente que si...")
async def yaoi(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/yaoi/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "fluff", description = "COLAS")
async def fluff(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/sfw/fluff/gif")
    fluf = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=fluf)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "holo", description = "Si te soy sincero, no se que hace este comando, solo lo añadí")
async def holo(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/sfw/holo/img")
    holo = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=holo)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "kitsune", description = "kitsune")
async def kitsune(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/sfw/kitsune/img")
    waifu = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifu)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "okami", description = "okami")
async def okami(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/sfw/okami/img")
    waifu = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifu)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "senko", description = "senko")
async def senko(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/sfw/senko/img")
    waifu = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifu)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "shiro", description = "shiro")
async def shiro(interaction: discord.Interaction):
    animeAPI = requests.get("https://purrbot.site/api/img/sfw/shiro/img")
    waifu = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifu)
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name = "trapo", description = "¡¡Es una trampa!!")
async def trapo(interaction: discord.Interaction):
    animeAPI = requests.get("https://api.waifu.pics/nsfw/trap")
    waifuNeko = animeAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await interaction.response.send_message(embed=emb)


## ===========================//  COMANDOS DE INTERACCION CON EL BOT  //============================ ##

    
@bot.command()
async def avatar(ctx, miembro: discord.Member = None):
    if miembro is None:
        avatar = ctx.author
        avatarurl = avatar.avatar
        emb = discord.Embed (title=f"Avatar de {ctx.author.mention}",color= 0xFFC0CB)
        emb.set_image(url=avatarurl)
        await ctx.message.reply(embed=emb)
    else:
        emb = discord.Embed(title=f"Avatar de {miembro.mention}",color= 0xFFC0CB)
        emb.set_image(url=miembro.avatar.url)
        await ctx.message.reply(embed=emb)
        
@bot.command()
@commands.cooldown(5, 3600, commands.BucketType.user)
async def say(ctx, *, texto):
    await ctx.send(texto)
    await ctx.message.delete()


## ===========================//                COMANDOS DE IMAGENES ANIME                   //============================ ##

    
@bot.command()
async def neko(ctx):
    animeAPI = requests.get("https://api.waifu.pics/sfw/neko")
    waifuNeko = animeAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB)
    emb.set_image(url=waifuNeko)
    await ctx.send(embed=emb)
    
@bot.command()
async def awoo(ctx):
    awooAPI = requests.get("https://api.waifu.pics/sfw/awoo")
    awoo = awooAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB)
    emb.set_image(url=awoo)
    await ctx.send(embed=emb)
    
@bot.command()
async def megumin(ctx):
    explosionAPI = requests.get("https://api.waifu.pics/sfw/megumin")
    explosion = explosionAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB)
    emb.set_image(url=explosion)
    await ctx.send(embed=emb)
    
@bot.command()
async def maid(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("maid"))
    await ctx.send(embed=emb)
    
@bot.command()
async def waifu(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("waifu"))
    await ctx.send(embed=emb)
    
@bot.command()
async def marin(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("marin-kitagawa"))
    await ctx.send(embed=emb)
    
@bot.command()
async def mori(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("mori-calliope"))
    await ctx.send(embed=emb)
    
@bot.command()
async def raiden(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("raiden-shogun"))
    await ctx.send(embed=emb)
    
@bot.command()
async def oppai(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("oppai"))
    await ctx.send(embed=emb)
    
@bot.command()
async def selfie(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("selfies"))
    await ctx.send(embed=emb)
    
@bot.command()
async def uniform(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("uniform"))
    await ctx.send(embed=emb)

@bot.command()
async def shiro (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/sfw/shiro/img")
    waifu = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifu)
    await ctx.send(embed=emb)

@bot.command()
async def senko (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/sfw/senko/img")
    waifu = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifu)
    await ctx.send(embed=emb)

@bot.command()
async def okami (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/sfw/okami/img")
    waifu = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifu)
    await ctx.send(embed=emb)

@bot.command()
async def kitsune (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/sfw/kitsune/img")
    waifu = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifu)
    await ctx.send(embed=emb)

@bot.command()
async def icon (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/sfw/icon/img")
    icon = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=icon)
    await ctx.send(embed=emb)

@bot.command()
async def holo (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/sfw/holo/img")
    holo = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=holo)
    await ctx.send(embed=emb)

@bot.command()
async def fluff (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/sfw/fluff/gif")
    fluf = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=fluf)
    await ctx.send(embed=emb)
    
## ===========================//                     COMANDOS DE ACCION                     //============================ ##
    
@bot.command()
async def bully(ctx, miembro: discord.Member = None):
    violenciaAPI = requests.get("https://api.waifu.pics/sfw/bully")
    violencia = violenciaAPI.json()["url"]
    if miembro is None:
        emb = discord.Embed(title=f"{ctx.author.mention} esta en modo violento", color= 0xFFC0CB)
        emb.set_image(url=violencia)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} se volvió violento contra {miembro.mention}, ¡¡alguien detengalo!!", color= 0xFFC0CB)
        emb.set_image(url=violencia)
        await ctx.send(embed=emb)

@bot.command()
async def abrazar(ctx, miembro: discord.Member = None):
    abrazoAPI = requests.get("https://purrbot.site/api/img/sfw/hug/gif")
    abrazo = abrazoAPI.json()["link"]
    if miembro is None:
        emb = discord.Embed(title=f"{ctx.author.mention} necesita un abrazo :( ", color= 0xFFC0CB)
        emb.set_image(url=abrazo)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} le esta dando un abrazo a {miembro.mention}", color= 0xFFC0CB)
        emb.set_image(url=abrazo)
        await ctx.send(embed=emb)
    
@bot.command()
async def llorar(ctx):
    lloraAPI = requests.get("https://purrbot.site/api/img/sfw/cry/gif")
    llora = lloraAPI.json()["link"]
    emb = discord.Embed(title=f"{ctx.author.mention} comenzó a llorar :( ", color= 0xFFC0CB)
    emb.set_image(url=llora)
    await ctx.send(embed=emb)
    
@bot.command()
async def beso(ctx, miembro: discord.Member = None):
    kissAPI = requests.get("https://purrbot.site/api/img/sfw/kiss/gif")
    kiss = kissAPI.json()["link"]
    if miembro is None:
        emb = discord.Embed(title=f"{bot.user} besó a {ctx.author.mention} >w<", color= 0xFFC0CB)
        emb.set_image(url=kiss)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} besó a {miembro.mention} >_<", color= 0xFFC0CB)
        emb.set_image(url=kiss)
        await ctx.send(embed=emb)
    
@bot.command()
async def lamer(ctx, miembro: discord.Member = None):
    lamerAPI = requests.get("https://purrbot.site/api/img/sfw/lick/gif")
    lamer = lamerAPI.json()["link"]
    if miembro is None:
        emb = discord.Embed(title=f"{bot.user} lamió a {ctx.author.mention} :O ", color= 0xFFC0CB)
        emb.set_image(url=lamer)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} lamió a {miembro.mention}", color= 0xFFC0CB)
        emb.set_image(url=lamer)
        await ctx.send(embed=emb)
    
@bot.command() 
async def acariciar(ctx, miembro: discord.Member = None):
    acariciarAPI = requests.get("https://purrbot.site/api/img/sfw/pat/gif")
    acariciar = acariciarAPI.json()["link"]
    if miembro is None:
        emb = discord.Embed(title=f"{bot.user} acarició a {ctx.author.mention}", color= 0xFFC0CB)
        emb.set_image(url=acariciar)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} acarició a {miembro.mention}", color= 0xFFC0CB)
        emb.set_image(url=acariciar)
        await ctx.send(embed=emb)
        
@bot.command()
async def bonk(ctx, miembro: discord.Member = None):
    bonkAPI = requests.get("https://api.waifu.pics/sfw/bonk")
    bonk = bonkAPI.json()["url"]
    if miembro is None:
        emb = discord.Embed(title=f"{ctx.author.mention} trata de golpear a alguien aleatoriamente sin ningún exito", color= 0xFFC0CB)
        emb.set_image(url=bonk)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} golpeó a {miembro.mention}", color= 0xFFC0CB)
        emb.set_image(url=bonk)
        await ctx.send(embed=emb)
        
@bot.command()
async def arrojar(ctx, miembro: discord.Member = None):
    arrojarAPI = requests.get("https://api.waifu.pics/sfw/yeet")
    arrojar = arrojarAPI.json()["url"]
    if miembro is None:
        emb = discord.Embed(title=f"{ctx.author.mention} trata de arrojar a alguien aleatoriamente sin ningún exito", color= 0xFFC0CB)
        emb.set_image(url=arrojar)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} arrojó a {miembro.mention}", color= 0xFFC0CB)
        emb.set_image(url=arrojar)
        await ctx.send(embed=emb)
        
@bot.command()
async def verguenza(ctx):
    verguenzaAPI = requests.get("https://purrbot.site/api/img/sfw/blush/gif")
    verguenza = verguenzaAPI.json()["link"]
    emb = discord.Embed(title=f"{ctx.author.mention} siente vergüenza", color= 0xFFC0CB)
    emb.set_image(url=verguenza)
    await ctx.send(embed=emb)
        
@bot.command()
async def sonrisa(ctx, miembro: discord.Member = None):
    sonrrisaAPI = requests.get("https://purrbot.site/api/img/sfw/smile/gif")
    sonrrisa = sonrrisaAPI.json()["link"]
    if miembro is None:
        emb = discord.Embed(title=f"{ctx.author.mention} esta sonrriendo", color= 0xFFC0CB)
        emb.set_image(url=sonrrisa)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} le sonrrió a {miembro.mention} >w<", color= 0xFFC0CB)
        emb.set_image(url=sonrrisa)
        await ctx.send(embed=emb)
    
@bot.command()
async def hi(ctx, miembro: discord.Member = None):
    hiAPI = requests.get("https://api.waifu.pics/sfw/wave")
    hi = hiAPI.json()["url"]
    if miembro is None:
        emb = discord.Embed(title=f"{ctx.author.mention} esta saludando a todos", color= 0xFFC0CB)
        emb.set_image(url=hi)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} saluda a {miembro.mention}", color= 0xFFC0CB)
        emb.set_image(url=hi)
        await ctx.send(embed=emb)
    
@bot.command()
async def five(ctx, miembro: discord.Member = None):
    chocalaAPI = requests.get("https://api.waifu.pics/sfw/highfive")
    chocala = chocalaAPI.json()["url"]
    if miembro is None:
        await ctx.send("Es necesario que menciones a alguien para darle los cinco")
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} le da cinco a {miembro.mention}", color= 0xFFC0CB)
        emb.set_image(url=chocala)
        await ctx.send(embed=emb)
    
@bot.command()
async def tomar(ctx, miembro: discord.Member = None):
    tomarAPI = requests.get("https://api.waifu.pics/sfw/handhold")
    tomar = tomarAPI.json()["url"]
    if miembro is None:
        await ctx.send("?")
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} le tomo la mano a {miembro.mention}", color= 0xFFC0CB)
        emb.set_image(url=tomar)
        await ctx.send(embed=emb)
    
@bot.command()
async def comer(ctx):
    comerAPI = requests.get("https://api.waifu.pics/sfw/nom")
    comer = comerAPI.json()["url"]
    emb = discord.Embed(title=f"{ctx.author.mention} está comiendo", color= 0xFFC0CB)
    emb.set_image(url=comer)
    await ctx.send(embed=emb)
    
@bot.command()
async def morder(ctx, miembro: discord.Member = None):
    morderAPI = requests.get("https://purrbot.site/api/img/sfw/bite/gif")
    morder = morderAPI.json()["link"]
    if miembro is None:
        await ctx.send("Es necesario que menciones que quieres morder, ¿O planeas morder otra cosa?")
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} mordió a {miembro.mention}, ¡¡ouch!!", color= 0xFFC0CB)
        emb.set_image(url=morder)
        await ctx.send(embed=emb)
    
@bot.command()
async def abofetear(ctx, miembro: discord.Member = None):
    bofetearAPI = requests.get("https://purrbot.site/api/img/sfw/slap/gif")
    bofetear = bofetearAPI.json()["link"]
    if miembro is None:
        await ctx.send("?")
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} abofeteó a {miembro.mention}, ¡¡ouch!!", color= 0xFFC0CB)
        emb.set_image(url=bofetear)
        await ctx.send(embed=emb)
    
@bot.command()
async def cosquillas (ctx, miembro: discord.Member = None):
    cosquillasAPI = requests.get("https://purrbot.site/api/img/sfw/tickle/gif")
    cosquilla = cosquillasAPI.json()["link"]
    if miembro is None:
        await ctx.send("Debes mencionar a algien")
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} le hace cosquillas a {miembro.mention}", color= 0xFFC0CB)
        emb.set_image(url=cosquilla)
        await ctx.send(embed=emb)
    
@bot.command()
async def patear(ctx, miembro: discord.Member = None):
    patearAPI = requests.get("https://api.waifu.pics/sfw/kick")
    patear = patearAPI.json()["url"]
    if miembro is None:
        await ctx.send("Es necesario que menciones a quien quieres patear")
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} pateó a {miembro.mention}, ¡¡ouch!!", color= 0xFFC0CB)
        emb.set_image(url=patear)
        await ctx.send(embed=emb)
    
@bot.command()
async def happy(ctx):
    happyAPI = requests.get("https://api.waifu.pics/sfw/happy")
    happy = happyAPI.json()["url"]
    emb = discord.Embed(title=f"{ctx.author.mention} esta feliz :) ", color= 0xFFC0CB)
    emb.set_image(url=happy)
    await ctx.send(embed=emb)
    
@bot.command()
async def confia(ctx, miembro: discord.Member = None):
    ginoAPI = requests.get("https://api.waifu.pics/sfw/wink")
    gino = ginoAPI.json()["url"]
    if miembro is None:
        emb = discord.Embed(title=f"Confíen en {ctx.author.mention}", color= 0xFFC0CB)
        emb.set_image(url=gino)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title=f"{miembro.mention}, trata de confíar en {ctx.author.mention} ;) ", color= 0xFFC0CB)
        emb.set_image(url=gino)
        await ctx.send(embed=emb)
    
@bot.command()
async def tocar(ctx):
    tocarAPI = requests.get("https://purrbot.site/api/img/sfw/poke/gif")
    tocar = tocarAPI.json()["link"]
    emb = discord.Embed(title="Tocar Tocar Tocar Tocar", color= 0xFFC0CB)
    emb.set_image(url=tocar)
    await ctx.send(embed=emb)
    
@bot.command()
async def bailar(ctx, miembro: discord.Member = None):
    bailarAPI = requests.get("https://purrbot.site/api/img/sfw/dance/gif")
    bailar = bailarAPI.json()["link"]
    if miembro is None:
        emb = discord.Embed(title=f"{ctx.author.mention} comenzó a bailar", color= 0xFFC0CB)
        emb.set_image(url=bailar)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title=f"{ctx.author.mention} comenzó a bailar con {miembro.mention}", color= 0xFFC0CB)
        emb.set_image(url=bailar)
        await ctx.send(embed=emb)
    
@bot.command()
async def cringe(ctx):
    cringeAPI = requests.get("https://api.waifu.pics/sfw/cringe")
    cringe = cringeAPI.json()["url"]
    emb = discord.Embed(title=f"Vergüenza ajena", color= 0xFFC0CB)
    emb.set_image(url=cringe)
    await ctx.send(embed=emb)

    

## ===========================//                 COMANDOS DE NSFW                   //============================ ##


@bot.command()
@commands.is_nsfw()
async def badwaifu(ctx):
    animeAPI = requests.get("https://api.waifu.pics/nsfw/waifu")
    waifu = animeAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB)
    emb.set_image(url=waifu)
    await ctx.send(embed=emb)
    
@badwaifu.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def blowjob(ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/blowjob/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await ctx.send(embed=emb)
    
@blowjob.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')

@bot.command()
@commands.is_nsfw()
async def badneko(ctx):
    animeAPI = requests.get("https://api.waifu.pics/nsfw/neko")
    waifuNeko = animeAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await ctx.send(embed=emb)
    
@badneko.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def hentai(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("hentai"))
    await ctx.send(embed=emb)
    
@hentai.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def milf(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("milf"))
    await ctx.send(embed=emb)

@milf.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def ass(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("ass"))
    await ctx.send(embed=emb)

@ass.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def oral(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("oral"))
    await ctx.send(embed=emb)

@oral.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def paizuri(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("paizuri"))
    await ctx.send(embed=emb)
    
@paizuri.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def ecchi(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("ecchi"))
    await ctx.send(embed=emb)
    
@ecchi.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
       
@bot.command()
@commands.is_nsfw()
async def ero(ctx):
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=await getWaifu("ero"))
    await ctx.send(embed=emb)
    
@ero.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def anal (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/anal/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await ctx.send(embed=emb)

@anal.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def cum (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/cum/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await ctx.send(embed=emb)

@cum.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')

@bot.command()
@commands.is_nsfw()
async def fuck (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/fuck/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await ctx.send(embed=emb)

@fuck.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def pussylick (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/pussylick/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await ctx.send(embed=emb)

@pussylick.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def solo (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/solo/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await ctx.send(embed=emb)

@solo.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def triofff (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/threesome_fff/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await ctx.send(embed=emb)

@triofff.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def trioffm (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/threesome_ffm/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await ctx.send(embed=emb)

@trioffm.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def triommf (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/threesome_mmf/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await ctx.send(embed=emb)

@triommf.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def yuri (ctx):
    animeAPI = requests.get("https://purrbot.site/api/img/nsfw/yuri/gif")
    waifuNeko = animeAPI.json()["link"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await ctx.send(embed=emb)

@yuri.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    
@bot.command()
@commands.is_nsfw()
async def trap (ctx):
    animeAPI = requests.get("https://api.waifu.pics/nsfw/trap")
    waifuNeko = animeAPI.json()["url"]
    emb = discord.Embed(color= 0xFFC0CB) 
    emb.set_image(url=waifuNeko)
    await ctx.send(embed=emb)

@trap.error
async def nsfw_command_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Este comando solo puede usarse en canales NSFW, pídele a tu administrador que creé un canal NSFW para hacer uso de este comando.')
    

## ===========================//  COMANDOS DE CONSULTA A CHATGPT //============================ ##
    
    
@bot.command()
@commands.cooldown(5, 300, commands.BucketType.user)
async def gpt(ctx, *pregunta):
    response = openai.Completion.create(
        engine="text-davinci-002",      ## Modelo de lenguaje GPT
        prompt=f"Las respuestas deben ser respondiendo a este usuario y en español: {ctx.author.mention}, debe ser tratado con cariño, tambien, debes responder de forma femenina, por ejemplo: en vez de no estoy seguro, debe ser no estoy segura; Aqui va mi mensaje solo responde a lo que va a continuacion entre parentesis: ( {pregunta} )",     ## Mensaje que se envia a GPT
        max_tokens=1000,     ## Longitud de respuesta 
        n=1,                 ## Numero de respuestas 
        temperature=1,     ## Aleatoriedad de los mensajes
    )
    respuesta = response.choices[0].text
    emb = discord.Embed(description=respuesta , color = 0x008f39)
    emb.set_author(name="Respuesta de ChatGPT")
    ##await ctx.channel.trigger_typing()
    await ctx.message.reply(embed=emb)



## ===========================//  COMANDOS PARA OBTENER UN PERRO //============================ ##


@bot.command()
async def dog(ctx):
    
    dogAPI = requests.get("https://dog.ceo/api/breeds/image/random")
    dog = dogAPI.json()["message"]
    emb = discord.Embed(color= 0xa18262)
    emb.set_image(url=dog)
    await ctx.send(embed=emb)
        
    
## ===========================//  COMANDOS PARA OBTENER AYUDA  //============================ ##


@bot.command()
async def ayuda(ctx):
    
    await ctx.send("Ayuda")
    ##Introduccion a la ayuda
    embMess=discord.Embed( title="Comando de ayuda recibido", description="Observamos que pediste ayuda y hemos venido corriendo a dartela, a continuacion te daremos una breve guia sobre como usar el bot.", color=0x008f39)
    ##Ayuda de moderacion 
    embMod=discord.Embed(title= "Comandos de moderación", description="Tenemos disponibles distintos comandos de moderación que pueden serte de ayuda al querer mantener un orden en tu servidor. A continuacion se listan estos comandos:", color=0x008f39)
    embMod.add_field(name= "kick", value="Este comando te permite expulsar a un miembro del servidor, solo debes mencionar a quien desees expulsar; Tambien puedes añadir un motivo escribiendolo despues de mencionar al miembro a expulsar")
    embMod.add_field(name="ban", value="Este comando permite banear a un miembro, solo debes mencionar a la persona que desees expulsar, tambien puedes añadir un motivo")
    embMod.add_field(name="clear" , value="Este comando te permite eliminar mensajes, solo escribe el comando, y seguido escribe el numero de mensajes para eliminar.")
    ##Ayuda de acciones
    embAction=discord.Embed( title="Comandos de acciones", description="Los comandos de acciones permiten tener una mayor interaccion entre los miembros de tu servidor, puedes expresar acciones y emociones, esta vez preferiremos que tu mismo experimentes con estos comandos, asi que nosotros solo te dejaremos que comandos puedes usar, intenta escribiendo solo el comando o mencionando a alguien junto con estos.", color=0x008f39)
    embAction.add_field(name="bully", value="")
    embAction.add_field(name="abrazar", value="")
    embAction.add_field(name="llorar", value="")
    embAction.add_field(name="beso", value="")
    embAction.add_field(name="lamer", value="")
    embAction.add_field(name="acariciar", value="")
    embAction.add_field(name="bonk",value="")
    embAction.add_field(name="arrojar",value="")
    embAction.add_field(name="sonrisa",value="")
    embAction.add_field(name="hi",value="")
    embAction.add_field(name="five",value="")
    embAction.add_field(name="tomar",value="")
    embAction.add_field(name="comer",value="")
    embAction.add_field(name="morder",value="")
    embAction.add_field(name="abofetear",value="")
    embAction.add_field(name="cosquillas",value="")
    embAction.add_field(name="patear",value="")
    embAction.add_field(name="happy",value="")
    embAction.add_field(name="five",value="")
    embAction.add_field(name="confia",value="")
    embAction.add_field(name="tocar",value="")
    embAction.add_field(name="bailar",value="")
    embAction.add_field(name="cringe",value="")
    ##Ayuda imagenes API
    embImg=discord.Embed(title= "Comandos de imagenes de waifus", description="Las waifus se han convertido en la principal atracción para los usuarios, asi que nos vimos en la necesidad de añadir estos comandos:", color=0x008f39)
    embImg.add_field(name="waifu",value="")
    embImg.add_field(name="neko",value="")
    embImg.add_field(name="awoo",value="")
    embImg.add_field(name="megumin",value="")
    embImg.add_field(name="maid",value="")
    embImg.add_field(name="shiro",value="")
    embImg.add_field(name="senko",value="")
    embImg.add_field(name="okami",value="")
    embImg.add_field(name="kitsune",value="")
    embImg.add_field(name="holo",value="")
    embImg.add_field(name="fluff",value="")
    embImg.add_field(name="marin",value="")
    embImg.add_field(name="mori",value="")
    embImg.add_field(name="raiden",value="")
    embImg.add_field(name="oppai",value="")
    embImg.add_field(name="selfie",value="")
    embImg.add_field(name="uniform",value="")
    ##CHAT GPT
    embGPT=discord.Embed(title= "CHAT GPT", description="Estuvimos horas tratando de hacer esta implementación, incluso usamos al mismisimo GhatGPT para que nos enseñara como añadirlo a nuestro bot, pero logramos hacer que nuestro bot tenga conciencia misma.", color=0x008f39)
    embGPT.add_field(name="Como usar ChatGPT",value="Para usar esta caracteristica, es necesario que uses el comando .gpt, seguido, puedes ecribir lo que quieras; una pregunta, un poema o una declaración de amor, deja que el bot responda a tu mensaje.")
    ##DOG
    embDOG=discord.Embed(title= "DOGS API", description="Estamos orgullosos de presentar al que fue nuestro introductor al mundo de las API; Estamos hablando de dog API, planeamos extender esta caracteristica, asi que te dejamos una lista de los comandos que puedes usar para ver imagenes de perritos 😀", color=0x008f39)
    embDOG.add_field(name="dog",value="imagenes de perros")
    ##NSFW
    embNSFW=discord.Embed(title= "NSFW", description="Tu y yo sabemos que es esta categoria, limitate a usar los comandos y no preguntes...", color=0x008f39)
    embNSFW.add_field(name="badwaifu",value="")
    embNSFW.add_field(name="blowjob",value="")
    embNSFW.add_field(name="badneko",value="")
    embNSFW.add_field(name="hentai",value="")
    embNSFW.add_field(name="milf",value="")
    embNSFW.add_field(name="ass",value="")
    embNSFW.add_field(name="oral",value="")
    embNSFW.add_field(name="paizuri",value="")
    embNSFW.add_field(name="ecchi",value="")
    embNSFW.add_field(name="ero",value="")
    embNSFW.add_field(name="anal",value="")
    embNSFW.add_field(name="cum",value="")
    embNSFW.add_field(name="fuck",value="")
    embNSFW.add_field(name="pussylick",value="")
    embNSFW.add_field(name="solo",value="")
    embNSFW.add_field(name="triofff",value="")
    embNSFW.add_field(name="trioffm",value="")
    embNSFW.add_field(name="triommf",value="")
    embNSFW.add_field(name="yuri",value="")
    
    await ctx.send(embed=embMess)
    await ctx.send(embed=embMod)
    await ctx.send(embed=embAction)
    await ctx.send(embed=embImg)
    await ctx.send(embed=embGPT)
    await ctx.send(embed=embDOG)
    await ctx.send(embed=embNSFW)
    

@bot.command()
async def info(ctx):
    
    emb=discord.Embed( title="Informacion", description=f"Este bot esta hecho a partir de un dia de aburrimiento en casa, hemos recibido ayuda de diversas fuentes en internet, por lo que estamos bastante agradecidos con ellos, a continuacion agradecemos a distintos desarrolladores que lograron hacer realidad este sueño; Con mucho cariño el staff de {bot.user}")
    emb.add_field(name="https://waifu.pics/",value="API de imagenes animé.")
    emb.add_field(name="https://www.waifu.im/",value="API de imagenes animé.")
    emb.add_field(name="https://docs.purrbot.site/",value="Otra API de imagenes animé, realmente nos gustan las imagenes animé.")
    emb.add_field(name="https://dog.ceo/dog-api/",value="Nuestro introductor al mundo de las API.")
    emb.add_field(name="CHAT GPT",value="Por dejarnos usar su API de forma gratuita, prometemos no pedir nada a cambio por el uso de esta caracteristica.")
    emb.add_field(name="https://wiki.waifly.com/",value="Agradecimientos especiales a waifly.com por permitirnos hostear nuestro bot de forma gratuita.")
    emb.add_field(name="https://discord.gg/UHrZeXnMSy",value="Agradecemos a los miembros de nuestro servidor, que soportaron todos nuestro errores y nos ayudaron a probar todos los comandos; Chicos, los quiero mucho.")
    await ctx.send(embed=emb)
        

## ===========================//  TOKEN DE BOT //============================ ##

    
bot.run("YOUR TOKEN")

