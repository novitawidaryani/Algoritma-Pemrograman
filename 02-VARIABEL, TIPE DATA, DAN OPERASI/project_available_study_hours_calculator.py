

# ask the user for sleeping hours, working hours, weekday relaxing hours, weekend relaxing hours
sleeping_hours = float(input("How many hours do you sleep per day? "))
working_hours = float(input("How many hours do you work per day? "))
weekday_relaxing_hours = float(input("How many hours do you relax on weekdays? "))
weekend_relaxing_hours = float(input("How many hours do you relax on weekends? "))

# calculate weekday available hours = 24 - (sleeping hours + working hours + weekday relaxing hours + 3)
weekday_available_hours = 24 - (sleeping_hours + working_hours + weekday_relaxing_hours + 3)


# calculate weekend available hours = 24 - (sleeping hours + weekend relaxing hours + 3)
weekend_available_hours = 24 - (sleeping_hours + weekend_relaxing_hours + 3)


# calculate total available hours = (weekday available hours * 5) + (weekend available hours * 2)
total_available_hours = (weekday_available_hours * 5) + (weekend_available_hours * 2)


# print the total available hours
print("You have a " + str(weekday_available_hours) + " hours to study on weekdays")
print("You have a " + str(weekend_available_hours) + " hours to study on weekends")
print("You have a " + str(total_available_hours) + " hours to study in a week")
