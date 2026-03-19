import math

r = 5
volume = 4/3*math.pi*pow(r,3)

print ("Question 1.")
print ("Volume of the sphere is:", volume)

cover_price=24.95
discount=0.40

discount_price = cover_price * (1 - discount)

copies = 60

book_cost = discount_price * copies

shipping = 3 + (copies - 1) * 0.75

total_cost = book_cost + shipping

print("Total wholesale cost:", total_cost)

start_hour = 6
start_min = 52

start_seconds = start_hour*3600 + start_min*60

easy_pace = 8*60 + 15
tempo_pace = 7*60 + 12

total_run = easy_pace + 3*tempo_pace + easy_pace

finish_seconds = start_seconds + total_run

hour = finish_seconds // 3600
minute = (finish_seconds % 3600) // 60
second = finish_seconds % 60

print("Arrive home at:", hour, ":", minute, ":", second)
