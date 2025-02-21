months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
salary_data = {}
# Get valid salary input
while True:
    user_input = input("Please enter your salary for the month: $").strip()
    if not user_input:
        print("Invalid input: Salary cannot be empty. Please enter a value.")
        continue

    try:
        salary = float(user_input)
        if salary < 0:
            print("Invalid salary: Salary cannot be negative. Please enter a valid salary.")
            continue
        break  # Exit the loop if input is valid.
    except ValueError:
        print("Invalid input: Please enter a numeric value.")