import psutil

def cpu_usage(percent):
    usage = psutil.cpu_percent()
    return usage>percent

if cpu_usage(65):
    print("Overloaded")

else:
    print('Safe')