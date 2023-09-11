import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    virtual_memory = psutil.virtual_memory()
    return {
        'total': virtual_memory.total,
        'available': virtual_memory.available,
        'used': virtual_memory.used,
        'percentage': virtual_memory.percent
    }

if __name__ == "__main__":
    while True:
        cpu_usage = get_cpu_usage()
        ram_usage = get_ram_usage()
        
        print(f'CPU Usage: {cpu_usage}%')
        print(f'RAM Usage - Total: {ram_usage["total"]}, Available: {ram_usage["available"]}, Used: {ram_usage["used"]}, Percentage: {ram_usage["percentage"]}%')
