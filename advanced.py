# Define hourly rates and tax rates based on levels
#levels = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8"]
regular_hourly_rates = {
    " L1": 10,
    " L2": 15,
    " L3": 20,
    " L4": 30,
    " L5": 40,
    " L6": 60,
    " L7": 80,
    " L8": 100
}
overtime_hourly_rates = {
    " L1": 15,
    " L2": 22,
    " L3": 30,
    " L4": 45,
    " L5": 60,
    " L6": 90,
    " L7": 120,
    " L8": 150
}

# Define rates for family support
MarriageStatusRate = {
    " Single": 50,
    " Married": 150
}  # Support by marriage status
ChildRate = 20  # Support rate per child

# Define tax rates
FederalTaxRate = 0.15  # Federal tax rate
#states = ["California", "Texas", "Florida", "New York", "Pennsylvania", "Illinois", "Ohio", "Georgia", "North Carolina", "Michigan"]
StateIncomeTaxRates = {
    " California": 0.10,
    " Texas": 0.12,
    " Florida": 0.07,
    " New York": 0.15,
    " Pennsylvania": 0.08,
    " Illinois": 0.09,
    " Ohio": 0.03,
    " Georgia": 0.06,
    " North Carolina": 0.09,
    " Michigan": 0.00
}

# Open the input file for reading
with open("advanced_report.txt", "r") as input_file:
  # Open the output file for writing
  with open("advanced_salary.txt", "w") as output_file:
    # Write header to the output file
    output_file.write(
        "ID, Name, Level, State, Single/Married, #ofChildren, #ofRegularWorkHours, #ofOvertimeHours, GrossIncome, StateTax, FederalTax, NetIncome\n"
    )

    # Skip the first line by simply reading it
    input_file.readline()

    # Iterate over each line in the input file
    for line in input_file:
      # Split the line into fields using a comma as the separator
      fields = line.strip().split(",")
      print(fields)

      # Extract employee information
      employee_id, employee_name, level, state, marital_status, num_children, reg_work_hour, overtime_hour = fields

      # Convert work hour values to integers
      reg_work_hour = int(reg_work_hour)
      overtime_hour = int(overtime_hour)
      num_children = int(num_children)

      # Calculate GrossIncome
      gross_income = (reg_work_hour * regular_hourly_rates[level]) + (
          overtime_hour * overtime_hourly_rates[level])

      # Calculate FamilySupport
      family_support = MarriageStatusRate[marital_status] + (ChildRate *
                                                             num_children)

      # Calculate Tax
      federal_tax = gross_income * FederalTaxRate
      state_tax = gross_income * StateIncomeTaxRates[state]

      # Calculate NetIncome
      net_income = gross_income - (state_tax + federal_tax)

      # Format the output line
      output_line = f"{employee_id}, {employee_name}, {level}, {state}, {marital_status}, {num_children}, {reg_work_hour}, {overtime_hour}, {gross_income}, {state_tax}, {federal_tax}, {net_income}\n"

      # Write the output line to the output file
      output_file.write(output_line)

print("Salary calculation and writing to advance_salary.txt is complete.")
