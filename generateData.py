import random

# Choose the data generation mode: basic or advanced
dataMode = 'basic'
#dataMode = 'advanced'

num_employees = 50  # Adjust as needed

# List of random first names
first_names = [
    "Emma", "Liam", "Olivia", "Noah", "Ava", "Isabella", "Sophia", "Mia",
    "Charlotte", "Amelia", "Harper", "Evelyn", "Abigail", "Emily", "Elizabeth",
    "Sofia", "Avery", "Ella", "Scarlett", "Grace", "Chloe", "Lily", "Zoey",
    "Penelope", "Victoria", "Aria", "Riley", "Madison", "Layla", "Eleanor",
    "Hannah", "Addison", "Aubrey", "Stella", "Zoe", "Aurora", "Savannah",
    "Violet", "Hazel", "Brooklyn", "Lillian", "Samantha", "Natalie", "Emilia",
    "Leah", "Maya", "Allison", "Lucy", "Eva", "Taylor"
]

# List of random last names
last_names = [
    "Johnson", "Smith", "Brown", "Davis", "Wilson", "Jones", "Miller",
    "Martinez", "Anderson", "Taylor", "Thomas", "Jackson", "White", "Harris",
    "Clark", "Lewis", "Hall", "Walker", "Turner", "Baker", "Green", "Allen",
    "King", "Wright", "Hill", "Adams", "Scott", "Murphy", "Carter", "Mitchell",
    "Young", "Parker", "Evans", "Gray", "Collins", "Nelson", "Hayes", "Reed",
    "Wood", "Ross", "Campbell", "Rivera", "Cooper", "Bennett", "Flores",
    "Reed", "Ward", "Foster", "Morgan", "Rogers"
]

# List of possible levels
levels = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8"]

# List of states for random selection
states = [
    "California", "Texas", "Florida", "New York", "Pennsylvania", "Illinois",
    "Ohio", "Georgia", "North Carolina", "Michigan"
]


# Data Generation - Basic mode
def generateDataBasic(num_employees):
  # Open a text file for writing the generated data
  with open('basic_report.txt', "w") as txt_file:
    # Generate random data for a specified number of employees
    txt_file.write("ID, Name, #RegWorkHours,#OvertimeHours\n")
    for i in range(1, num_employees + 1):
      employee_id = f"{i:03}"  # Generates 3-digit ID like "001"
      employee_name = f"{random.choice(first_names)} {random.choice(last_names)}"
      reg_work_hours = random.randint(30, 40)  # Random regular work hours
      overtime_hours = random.randint(0, 20)  # Random overtime hours

      # Write the generated data to the text file
      txt_file.write(
          f"{employee_id}, {employee_name}, {reg_work_hours}, {overtime_hours}\n"
      )
  txt_file.close()
  print(
      f"Generated {num_employees} random employee records in 'basic_report.txt'."
  )


# Data Generation - Advanced mode
def generateDataAdvanced(num_employees):
  # Open a text file for writing the generated data
  with open('advanced_report.txt', "w") as txt_file:
    # Generate random data for a specified number of employees
    txt_file.write(
        "ID, Name, Level, State, MaritalStatus, NumChildren, RegWorkHours, OvertimeHours\n"
    )
    for i in range(1, num_employees + 1):
      employee_id = f"{i:03}"  # Generates 3-digit ID like "001"
      employee_name = f"{random.choice(first_names)} {random.choice(last_names)}"
      level = random.choice(levels)
      state = random.choice(states)
      marital_status = random.choice(["Single", "Married"])
      num_children = random.randint(
          0, 3)  # Random number of children between 0 and 3
      reg_work_hours = random.randint(30, 50)  # Random regular work hours
      overtime_hours = random.randint(0, 20)  # Random overtime hours

      # Write the generated data to the text file
      txt_file.write(
          f"{employee_id}, {employee_name}, {level}, {state}, {marital_status}, {num_children}, {reg_work_hours}, {overtime_hours}\n"
      )
  txt_file.close()
  print(
      f"Generated {num_employees} random employee records in 'advanced_report.txt'."
  )


# Main Part
if dataMode == 'basic':
  generateDataBasic(num_employees)
elif dataMode == 'advanced':
  generateDataAdvanced(num_employees)
else:
  print("Not defined data generation mode!")
