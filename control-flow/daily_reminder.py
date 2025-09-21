# daily_reminder.py

# Step 1: Ask the user for task details
task = input("Enter your task for today: ")
priority = input("Enter the priority level (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Step 2: Use a loop to keep reminding (just once here for demo, can be extended)
for i in range(1):
    # Step 3: Match Case based on priority
    match priority:
        case "high":
            reminder = f"Reminder: Your task '{task}' is HIGH priority."
        case "medium":
            reminder = f"Reminder: Your task '{task}' is MEDIUM priority."
        case "low":
            reminder = f"Reminder: Your task '{task}' is LOW priority."
        case _:
            reminder = f"Reminder: Your task '{task}' has an UNKNOWN priority."

    # Step 4: Adjust reminder if time-sensitive
    if time_bound == "yes":
        reminder += " It requires immediate attention today!"

    # Step 5: Print final reminder
    print(reminder)
