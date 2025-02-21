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
        
# Enter data for multiple months
while True:
    while True:
        month = input("\nEnter the month (e.g., January, February, etc.): ").lower()
        if month in months and month not in salary_data:
            break
        elif month in salary_data:
            print(f"Data for {month.capitalize()} already entered. Please choose another month.")
        else:
            print("Invalid month. Please enter a valid month name.")

    while True:
        try:
            saving = float(input("Enter the savings percentage: "))
            rent = float(input("Enter the rent percentage: "))
            electricity = float(input("Enter the electricity percentage: "))
            
            if saving < 0 or rent < 0 or electricity < 0:
                print("Percentages cannot be negative. Please enter valid values.")
                continue
            if saving + rent + electricity > 100:
                print("Total percentage cannot exceed 100%. Please enter valid values.")
                continue
            break
        except ValueError:
            print("Invalid input: Please enter numeric values.")