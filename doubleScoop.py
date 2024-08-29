import random

# [ Task 1 ]

# List of moods
moods = ["Happy", "Sad", "Angry", "Energetic", "Calm", "Confused", "Tired"]

# List of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# List of times of the day
times_of_day = ["morning", "afternoon", "evening", "night"]

# Nested loops to iterate over days and times
for day in days_of_week:
    for time in times_of_day:
        mood = random.choice(moods)
        print(f"On {day} {time} you were {mood}.")
