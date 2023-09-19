import random

# Define possible levels and hourly rates for each level
levels = ["L1", "L2", "L3"]
hourly_rates = {
    "L1": 10,
    "L2": 12,
    "L3": 14,
}

# List of states for random selection
states = ["California", "New York", "Texas", "Florida", "Illinois"]

# Open a text file for writing the generated data
with open("test_data.txt", "w") as txt_file:
    
    # Generate random data for a specified number of employees
    num_employees = 50  # Adjust as needed
    txt_file.write("ID, Name, Level, State, MaritalStatus, NumChildren, RegWorkHours, OvertimeHours\n")
    for i in range(1, num_employees + 1):
        employee_id = f"{i:03}"  # Generates 3-digit ID like "001"
        employee_name = f"Employee{i}"
        level = random.choice(levels)
        state = random.choice(states)
        marital_status = random.choice(["Single", "Married"])
        num_children = random.randint(0, 3)  # Random number of children between 0 and 3
        reg_work_hours = random.randint(30, 50)  # Random regular work hours
        overtime_hours = random.randint(0, 20)   # Random overtime hours
        
        # Write the generated data to the text file
        txt_file.write(f"{employee_id}, {employee_name}, {level}, {state}, {marital_status}, {num_children}, {reg_work_hours}, {overtime_hours}\n")

print(f"Generated {num_employees} random employee records in 'test_data.txt'.")
