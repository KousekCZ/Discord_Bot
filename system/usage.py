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


def get_pagefile_usage():
    pagefile_usage = psutil.swap_memory().percent
    pagefile_used_gb = round(psutil.swap_memory().used / (1024 ** 3),
                             2)  # převést byty na GB s dvěma desetinnými místy
    pagefile_total_gb = round(psutil.swap_memory().total / (1024 ** 3),
                              2)  # převést byty na GB s dvěma desetinnými místy
    return pagefile_usage, pagefile_used_gb, pagefile_total_gb


def format_system_info(cpu_percent, total_cpu_percent, ram_percent, ram_used_gb, ram_total_gb, disk_percent,
                       disk_used_gb, disk_total_gb, pagefile_usage, pagefile_used_gb, pagefile_total_gb):
    cpu_info = "\n".join([f"CPU {i}: {value}%" for i, value in enumerate(cpu_percent)])
    return f"## Správce úloh\n### CPU\nCelkové využití CPU: {total_cpu_percent}%\n{cpu_info}\n### RAM:\n{ram_percent}% ({ram_used_gb}GB / {ram_total_gb}GB)\n### Disk:\n{disk_percent}% ({disk_used_gb}GB / {disk_total_gb}GB)\n### Pagefile:\n {pagefile_usage}% ({pagefile_used_gb}GB / {pagefile_total_gb}GB)"


async def update_usage(client, channel_id):
    channel = client.get_channel(channel_id)
    message = await channel.send("Načítání...")

    while True:
        cpu_percent, total_cpu_percent = get_cpu_usage()
        ram_percent, ram_used_gb, ram_total_gb = get_ram_usage()
        disk_percent, disk_used_gb, disk_total_gb = get_disk_usage()
        pagefile_usage, pagefile_used_gb, pagefile_total_gb = get_pagefile_usage()
        info_text = format_system_info(cpu_percent, total_cpu_percent, ram_percent, ram_used_gb, ram_total_gb,
                                       disk_percent, disk_used_gb,
                                       disk_total_gb, pagefile_usage, pagefile_used_gb, pagefile_total_gb)
        await message.edit(content=info_text)
        time.sleep(0.5)  # Aktualizace každých 0.5 sekundy
