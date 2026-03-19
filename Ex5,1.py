import time
current_time=time.time()

total_seconds=int(current_time)

seconds_per_day=24*3600
days_since_epoch=total_seconds//seconds_per_day

remaining_seconds=total_seconds%seconds_per_day

hours=remaining_seconds//3600
remaining_seconds=remaining_seconds%3600

minutes=remaining_seconds//60
seconds=remaining_seconds%60

print("Days since epoch:", days_since_epoch)
print("Current time:", hours, "hours", minutes, "minutes", seconds, "seconds")