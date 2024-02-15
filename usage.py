import psutil
import time


def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(percpu=True)
    total_cpu_percent = psutil.cpu_percent()  # Celková spotřeba CPU
    return cpu_percent, total_cpu_percent


def get_ram_usage():
    mem = psutil.virtual_memory()
    ram_percent = mem.percent
    ram_used_gb = round(mem.used / (1024 ** 3), 2)  # převést byty na GB s dvěma desetinnými místy
    ram_total_gb = round(mem.total / (1024 ** 3), 2)  # převést byty na GB s dvěma desetinnými místy
    return ram_percent, ram_used_gb, ram_total_gb


def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent
    disk_used_gb = round(disk_usage.used / (1024 ** 3), 2)  # převést byty na GB s dvěma desetinnými místy
    disk_total_gb = round(disk_usage.total / (1024 ** 3), 2)  # převést byty na GB s dvěma desetinnými místy
    return disk_percent, disk_used_gb, disk_total_gb


def format_system_info(cpu_percent, total_cpu_percent, ram_percent, ram_used_gb, ram_total_gb, disk_percent,
                       disk_used_gb, disk_total_gb):
    cpu_info = "\n".join([f"CPU {i}: {value}%" for i, value in enumerate(cpu_percent)])
    return f"## Správce úloh\n\r### CPU\n\rCelkové využití CPU: {total_cpu_percent}%\n\r{cpu_info}\n\r### RAM:\n\r{ram_percent}% ({ram_used_gb}GB / {ram_total_gb}GB)\n\r### Disk:\n\r{disk_percent}% ({disk_used_gb}GB / {disk_total_gb}GB)"


async def update_usage(bot, channel_id):
    channel = bot.get_channel(channel_id)
    message = await channel.send("Načítání...")

    while True:
        cpu_percent, total_cpu_percent = get_cpu_usage()
        ram_percent, ram_used_gb, ram_total_gb = get_ram_usage()
        disk_percent, disk_used_gb, disk_total_gb = get_disk_usage()
        info_text = format_system_info(cpu_percent, total_cpu_percent, ram_percent, ram_used_gb, ram_total_gb,
                                       disk_percent, disk_used_gb, disk_total_gb)
        await message.edit(content=info_text)
        time.sleep(1)
