# explore_datetime.py
# Demonstrates how to use the datetime module for handling dates and times in Python

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(days_to_add):
    # Get the current date
    current_date = datetime.now()
    # Add the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    # Format as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date after {days_to_add} days:", formatted_future_date)
    return future_date

# Main program execution
if __name__ == "__main__":
    # Display current date and time
    display_current_datetime()

    # Prompt user for number of days
    try:
        days = int(input("Enter number of days to add: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer for days.")
