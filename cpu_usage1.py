import psutil

def cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    return usage>percent

if cpu_usage(75):
    print("Overloaded")

else:
    print('Safe')