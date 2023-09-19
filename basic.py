# Define hourly rates and tax rate
HourlyRate1 = 10  # Replace with the actual hourly rate for regular work
HourlyRate2 = 15  # Replace with the actual hourly rate for overtime work
TaxRate = 0.15

# Open the input file for reading
with open("basic_report.txt", "r") as input_file:
  # Open the output file for writing
  with open("basic_salary.txt", "w") as output_file:
    # Write header to the output file
    output_file.write(
        "ID, Name, #RegWorkHour, #OvertimeHour, GrossIncome, Tax, NetIncome\n")

    # Skip the first line by simply reading it
    input_file.readline()
    
    # Iterate over each line in the input file
    for line in input_file:
      # Split the line into fields using a comma as the separator
      fields = line.strip().split(",")

      # Extract the employee information
      employee_id, employee_name, reg_work_hour, overtime_hour = fields

      # Convert work hour values to integers
      reg_work_hour = int(reg_work_hour)
      overtime_hour = int(overtime_hour)

      # Calculate GrossIncome
      gross_income = (reg_work_hour * HourlyRate1) + (overtime_hour *
                                                      HourlyRate2)

      # Calculate Tax
      tax = gross_income * TaxRate

      # Calculate NetIncome
      net_income = gross_income - tax

      # Format the output line
      output_line = f"{employee_id}, {employee_name}, {reg_work_hour}, {overtime_hour}, {gross_income}, {tax}, {net_income}\n"

      # Write the output line to the output file
      output_file.write(output_line)

print("Salary calculation and writing to basic_salary.txt is complete.")
