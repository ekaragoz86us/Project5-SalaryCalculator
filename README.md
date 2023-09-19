# Project5 - Salary Calculator

## Part 1: Basic Salary Calculator

**Goal.** Given a file `basic_report.txt`, compute the salary of each employee.

**Input.** The file contains the following information: 
- Employee ID
- Employee Name
- \# of Regular Work Hour
- \# of Overtime hours
for each employee per line in the file:
`ID, Name,#RegWorkHour,#OvertimeHour`
Each column is separated by comma. An example is 
`001, Kirby Luna, 40, 10`

**Output.** The salary is computed as follows:
```
  GrossIncome = (# of Regular Work Hour x HourlyRate1) +  (\# of Overtime hours x HourlyRate2)
  Tax = GrossIncome x 15%
  NetIncome = GrossIncome - Tax
```
Then include the information in the following format `ID, Name,#RegWorkHour,#OvertimeHour, GrossIncome, Tax, NetIncome` for each employee per line in a new file `basic_salary.txt`.

## Part 2: Advanced Salary Calculator

**Goal.** Given a file “advance_report.txt” by the employer, compute the salary of each 
employee. 

**Input.** The input file `advance_report.txt` contains the following information: 
`ID, Name, Level, State, Single/Married, \#ofChildren, \#ofRegularWorkHours, \#ofOvertime Hours`
for each employee per line separated by comma. For example, 
`001, Kirby Luna, L1, California, Married, 2, 40, 10`

**Output.** The salary is computed as follows:
```
  GrossIncome = (# of Regular Work Hour x HourlyRate1forLevelX) + (# of Overtime hours x HourlyRate2LevelX) + (FamilySupport = MarriageStatusRate x Married/Single + Rate x #ofChildren)
  StateTax = GrossIncome x StateIncomeTaxRate (%0 - %10 depending on the state)
  FederalTax = GrossIncome x FederalTaxaRate (%15)
  NetIncome = GrossIncome - (StateTax + FederalTax)
```
for each employee per line in a new file `advance_salary.txt`.

## Bonus- Generate your own data
- Generate random IDs and fake names
- Assign random levels (from a list of possible levels)
- Randomly choose the marriage status (single/married) and number of 
children
- Randomly choose # of Hours (regular and overtime)
