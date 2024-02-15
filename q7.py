def angle(time):
    x = time.find(':')
    hours = int(time[:x])
    minutes = int(time[x+ 1:])
    hour_angle = (hours % 12) * 30 + minutes * 0.5
    minute_angle = minutes * 6
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)


time = input("Enter the time in format hh:mm (24-hour notation): ")

print(f"The smaller angle between the hour and minute hands at {time} is {angle(time)} degrees.")
