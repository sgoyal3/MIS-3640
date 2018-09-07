import time
FT = time.time()
days = FT / (60 * 60 * 24)
hour = days % int(days) * 24
min  = hour % int(hour) * 60
sec  = min % int(min) * 60
print(f"Days: {int(days)}\nTime: {int(hour)}:{int(min)}:{int(sec)}")
