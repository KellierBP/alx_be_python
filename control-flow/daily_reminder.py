# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process based on priority
match priority.lower():
    case "high":
        reminder = f"Your task '{task}' is HIGH priority."
    case "medium":
        reminder = f"Your task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"Your task '{task}' is LOW priority."
    case _:
        reminder = f"Your task '{task}' has an unknown priority."

# Modify if time-bound
if time_bound.lower() == "yes":
    reminder += " This requires immediate attention today!"

# Provide customized reminder
print(reminder)
