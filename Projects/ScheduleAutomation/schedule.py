# Sample employee data.
employees = [
# -------> add minimum hours required
    {"name": "Anne", "availability": [1, 2, 3, 4, 5], "max_hours": 8},
    {"name": "Belle", "availability": [2, 3, 4, 5, 6], "max_hours": 12},
    {"name": "Carrie", "availability": [1, 2, 3, 4, 5, 6], "max_hours": 8},

# ----->  Add more employees
]

# Sample shift data
shifts = [
    {"day": 1, "day_name": "Monday", "shift_type": "Morning", "required_employees": 1, "hours": 4},
    {"day": 1, "day_name": "Monday", "shift_type": "Afternoon", "required_employees": 1, "hours": 4},
    {"day": 2, "day_name": "Tuesday", "shift_type": "Morning", "required_employees": 1, "hours": 4},
    {"day": 2, "day_name": "Tuesday", "shift_type": "Afternoon", "required_employees": 1, "hours": 4},
    {"day": 3, "day_name": "Wednesday","shift_type": "Morning", "required_employees": 1, "hours": 4},
    {"day": 3, "day_name": "Wednesday", "shift_type": "Afternoon", "required_employees": 2, "hours": 4},
# ------> Add whole week shifts
]

# Initialize a schedule
schedule = []

# Sort shifts by priority (e.g., by day and required employees)
shifts.sort(key=lambda x: (x["day"], -x["required_employees"]))

# Assign employees to shifts
for shift in shifts:
    assigned_employees = []

    for employee in employees:
# ------> check all employees before asssigning shifts 

        # Check if the employee is available on the shift day
        if shift["day"] in employee["availability"]:
            
            # Check if the employee hasn't exceeded their max hours
# -------> add minnimum hours requirement check 
            if sum([s.get("hours", 0) for s in assigned_employees]) + shift["hours"] <= employee["max_hours"]:
                assigned_employees.append(employee)
                shift["hours"] = shift.get("hours", 0) + 4  # Assuming a 4-hour shift
            
            overtime = shift['hours'] - employee['max_hours']
            if overtime > 0: 
                    print(f"Attention! {employee['name']} is working over their allowed hours by {overtime} hours.")
# -----> repair placing, doesnt react... maybe change to preffered?


# ----> DO NOT allow possibility of more than max hours

        # Check if we've met the required number of employees for the shift
        if len(assigned_employees) == shift["required_employees"]:
            break
        else: 
            print(f"Attention! There are not enough employees to cover the required {shift['shift_type']} shift on {shift['day_name']}.")
# ----> edit so the message is not repeated multiple times? total the missing employees? empty shift
# ----> why is it printing if the shift was covered?

    # Add the assigned employees to the schedule
    schedule.append({"shift": shift, "assigned_employees": assigned_employees})

# Print the final schedule
for entry in schedule:
    shift = entry["shift"]
    employees = ", ".join([e["name"] for e in entry["assigned_employees"]])
    print(f"{shift['day']} - {shift['shift_type']} - Employees: {employees}")

    """
    Next steps:
    - repair above comments  
    -  lenghten the shifts
    - allow variety in shifts length
    
    """
