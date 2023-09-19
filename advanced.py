# Define hourly rates and tax rates based on levels
HourlyRate1LevelX = 12  # Replace with the actual hourly rate for regular work for Level X
HourlyRate2LevelX = 18  # Replace with the actual hourly rate for overtime work for Level X

# Define rates for family support and tax rates by state
MarriageStatusRate = 50  # Replace with the actual marriage status rate
ChildRate = 20  # Replace with the actual rate per child
StateIncomeTaxRates = {
    "California": 0.1,  # Replace with the actual state tax rate for California
    # Add more states and their tax rates as needed
}
FederalTaxRate = 0.15  # Replace with the actual federal tax rate

# Open the input file for reading
with open("advance_report.txt", "r") as input_file:
    # Open the output file for writing
    with open("advance_salary.txt", "w") as output_file:
        # Write header to the output file
        output_file.write("ID, Name, Level, State, Single/Married, #ofChildren, #ofRegularWorkHours, #ofOvertimeHours, GrossIncome, StateTax, FederalTax, NetIncome\n")

        # Iterate over each line in the input file
        for line in input_file:
            # Split the line into fields using a comma as the separator
            fields = line.strip().split(",")
            
            # Extract employee information
            employee_id, employee_name, level, state, marital_status, num_children, reg_work_hour, overtime_hour = fields
            
            # Convert work hour values to integers
            reg_work_hour = int(reg_work_hour)
            overtime_hour = int(overtime_hour)
            num_children = int(num_children)
            
            # Calculate GrossIncome
            gross_income = (reg_work_hour * HourlyRate1LevelX) + (overtime_hour * HourlyRate2LevelX)
            
            # Calculate FamilySupport
            family_support = (MarriageStatusRate * (1 if marital_status == "Married" else 0)) + (ChildRate * num_children)
            
            # Calculate StateTax
            state_tax_rate = StateIncomeTaxRates.get(state, 0)  # Get state tax rate or default to 0
            state_tax = gross_income * state_tax_rate
            
            # Calculate FederalTax
            federal_tax = gross_income * FederalTaxRate
            
            # Calculate NetIncome
            net_income = gross_income - (state_tax + federal_tax)
            
            # Format the output line
            output_line = f"{employee_id}, {employee_name}, {level}, {state}, {marital_status}, {num_children}, {reg_work_hour}, {overtime_hour}, {gross_income}, {state_tax}, {federal_tax}, {net_income}\n"
            
            # Write the output line to the output file
            output_file.write(output_line)

print("Salary calculation and writing to advance_salary.txt is complete.")
