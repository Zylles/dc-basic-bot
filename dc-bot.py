import os
import discord
from discord.ext import commands
import info
import kurcm
import kur
import time
import utils
from env import *
from model import *
import function
from function import *
from datetime import datetime
import duyurular

intents = discord.Intents.all()


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix='!', intents=intents, *args, **kwargs)


bot = MyBot()
game = Game()


@bot.event
async def on_ready():
    print(f"{bot.user} BOT AKTİF!!")
    await bot.change_presence(activity=discord.Game(name="!yardim"))

# ------------------------------------------------------------BİLGİ--------------------------------------
@bot.command(name="admin")
async def admin(ctx):
    await ctx.send(info.admink)


@bot.command(name="yardim")
async def yardim(ctx):
    await ctx.send(info.bilgi)


@bot.command(name="oyunlar")
async def oyunlar(ctx):
    await ctx.send(info.oyunlar)


@bot.command(name="normal")
async def normal(ctx):
    await ctx.send(info.normalb)

# -----------------------------------------------DAVET----------------------------------------
@bot.command(name="davet")
async def davet(ctx):
    await ctx.send(
        "BOTUN DAVET LİNKİ\n\nhttps://discord.com/api/oauth2/authorize?client_id=1207017285181513789&permissions=8&scope=bot")


# --------------------------------------------------KUR----------------------------------
@bot.command(name="kur")
async def kur(ctx):
    await ctx.send(kurcm.kur_dl + kurcm.kur_eu)

# ---------------------------------------------------oyun---------------------------
@bot.command(name="oyun")
async def zar_game(ctx, *args):
    if "zar" in args:
        await ctx.send("ZAR")
        await ctx.send(game.roll_dice())
    else:
        await ctx.send("YANLIŞ KOMUT!!")


# -------------------------------------------------mesaj sil-----------------------------------------
@bot.command(name="sil")
@commands.has_role("Admin")
async def sil(ctx, amount=50):
    await ctx.channel.purge(limit=amount)


# ---------------------------------------------KULLANCI ATMA-------------------------------------------
@bot.command(name="at")
@commands.has_role("Admin")
async def at(ctx, member: discord.Member, *args, reason="YOK"):
    await member.kick(reason=reason)
    
@bot.command(name="kick")
@commands.has_role("Admin")
async def kick(ctx, member: discord.Member, *args, reason="YOK"):
    await member.kick(reason=reason)


# ---------------------------------------------------ban------------------------------------
@bot.command(name="ban")
@commands.has_role("Admin")
async def ban(ctx, member: discord.Member, *args, reason="YOK"):
    await member.ban(reason=reason)


# -------------------------------------------------unban-------------------------------------
@bot.command(name="unban")
@commands.has_role("Admin")
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for bans in banned_users:
        user = bans.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} KULLANICISININ  BANI KALKTI')
            return


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


# -------------------------------------------------------ping-----------------------------
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pingim : `{bot.latency * 1000}`ms')


# -------------------------------------------------VERİ TABANI-------------------------------
@bot.command(name="workkkaka")
async def work(ctx):
    discord_id = ctx.message.author.id
    user = get_user_or_false(discord_id)
    now = datetime.now()
    if user:
        if is_more_than_one_hour(user.work):
            user.money = user.money + 1000
            user.work = now.strftime(TİME_STAMP_PATTERN)
            user.update()
            await ctx.send(f"HOŞ GELDİN ÇALIŞAN! {user.money}$ VAR")
        else:
            await ctx.send("1 SAAT BEKLEMEN GEREKİYOR")
    else:
        person = Person(discord_id, 1000, now.strftime(TİME_STAMP_PATTERN)._, 0).save()
        await ctx.send(f"HOŞ GELDİN ÇALIŞAN! {person.money}$ VAR")

    db.commit()


# ---------------------------------------------------Otomatik ROL VERME VE HOŞGELDİN MESAJI--------------------------------
@bot.event
async def on_member_join(member):
    kayıt_role = member.guild.get_role(1208406371142344734)
    await member.add_roles(kayıt_role)
    await member.guild.get_channel(1208420167025954908).send(
        f"{member.mention} HOŞ GELDİN. {kayıt_role.mention} Rolünüz verildi")

#-------------------------------------------------------GÜLE GÜLE MESAJI-------------------
@bot.event 
async def on_member_remove(member):
     channel=bot.get_channel(1208420167025954908)
     emb=discord.Embed(title=f"GÜLE GÜLE {member.name}")
     await channel.send(embed=emb)
# --------------------------------------------------------KAYIT BİLGİ------------------------
@bot.command()
async def destek(ctx):
    await ctx.send("AKD BOT RESMİ DİSCORD SUNUCUSU\n\nhttps://discord.gg/m9SwQvQ8xh")

channel = bot.get_channel(1209168715732746320)
async def dd(ctx):
    await channel.send('hello word')
# -------------------------------------------------------TOKRN----------------------------------------
bot.run(TOKEN)
