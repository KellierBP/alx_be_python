# daily_reminder.py

# Prompt for inputs
task = input("Enter your task: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Match Case to react based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an unspecified priority."

# If task is time-bound, modify the reminder
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Final customized reminder
print(reminder)
