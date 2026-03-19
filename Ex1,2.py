time_minute = 60
time_second= 42
total_time= time_minute*42+time_second
print ("Question 1.")
print ("Answer:", total_time)

distance_mile = 1.61
distance_kilometer = 10
distance = distance_kilometer / distance_mile
print ("Question 2.")
print ("Answer:", distance)

pace_seconds= total_time/distance
pace_min=int(pace_seconds//60)
pace_sec=int(pace_seconds%60)
time_hours=total_time/3600
speed_mph = distance / time_hours

print ("Question 3.")
print ("Average pace per mile:", pace_min, "minutes", pace_sec, "seconds.")
print ("Average speed:", speed_mph, "miles per hour.")

