import random

# [ Task 1 ]

moods = ["Happy","Sad","Angry","Energetic","Calm","Confused"]

# Loop through each day of the week
for day in range(7):
    # Randomly select a mood from the list
    mood = random.choice(moods)

    print(f"Day {day + 1}: {mood}")