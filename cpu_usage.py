import psutil

def cpu_usage(percent):
    usage = psutil.cpu_percent()
    return usage>percent

if cpu_usage(65) & cpu_usage(95) & cpu_usage(60):
    print("Overloaded")

else:
    print('Safe')