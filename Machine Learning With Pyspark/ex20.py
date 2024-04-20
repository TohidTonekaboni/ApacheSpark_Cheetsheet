# Find the average speed in km per hour. This will be different to the value that you got earlier because your model is now more sophisticated.
# What's the average time on the ground at OGG?
# What's the average time on the ground at JFK?
# What's the average time on the ground at LGA?


# Average speed in km per hour
avg_speed_hour = 60 / regression.coefficients[0]
print(avg_speed_hour)

# Average minutes on ground at OGG
inter = regression.intercept
print(inter)

# Average minutes on ground at JFK
avg_ground_jfk = inter + regression.coefficients[3]
print(avg_ground_jfk)

# Average minutes on ground at LGA
avg_ground_lga = inter + regression.coefficients[4]
print(avg_ground_lga)