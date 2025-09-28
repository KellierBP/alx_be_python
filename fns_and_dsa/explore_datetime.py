# explore_datetime.py

from datetime import datetime, timedelta


def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format it in a readable format YYYY-MM-DD HH:MM:SS
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date


def calculate_future_date(current_date, days_to_add):
    # Add the specified number of days to the current date
    future_date = current_date + timedelta(days=days_to_add)
    # Print the result in YYYY-MM-DD format
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date


def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Prompt for user input and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
