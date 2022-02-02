import psutil
import shutil 
import os
from pathlib import Path

@client.command()
async def info(ctx):
    tFile = open('/sys/class/thermal/thermal_zone0/temp') #cpu temp
    temp = float(tFile.read())
    tempC = temp/1000

    cFile = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq') #cpu clock
    clock =float(cFile.read())
    clockC = clock/1000

    cpu = psutil.cpu_percent(interval=1) #cpu usage
    ram = psutil.virtual_memory()[2] #RAM usage

    root_directory = Path('/home/pi/MusicBot/audio_cache') #AudioCache Usage
    disk = size(sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file()))

    path = "." 
    (free) = shutil.disk_usage(path)

    embed=discord.Embed(title="Sys Info", description="Raspbian GNU/Linux 10 (buster)", color=0x2ea4ff)
    embed.add_field(name="CPU TEMP", value=f"{tempC}℃", inline=True)
    embed.add_field(name="CPU Clock", value=f"{clockC}MHz", inline=True)
    embed.add_field(name="CPU Usage", value=f"{cpu}%", inline=True)
    embed.add_field(name="RAM Usage", value=f"{ram}%", inline=True)
    embed.add_field(name="AudioCache Usage", value=disk, inline=True)
    embed.add_field(name="Available Capacity", value=size(float(free)), inline=True)
    await ctx.send(embed=embed)
