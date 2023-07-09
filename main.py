# Program Name: ExmaplePyFinal.py 
# Function:     Figure out Salaries within Range (+/- $5000)
# Input:        Float(integers)
# Output:       Salaries (rounded nearest 100)

# List
salaries = []
avg_range = []

# Introduction
print("Welcome the to final project")
print("Please enter the employee's salaries: ")

# User input
while(True):
    salary = float(input("Employee Salary: $"))
    if salary == 0:
        print("Salary cannot be $0, please try again.")
        continue
    else:
        salaries.append(salary)
    another_input = input("Is there another salary to enter? yes or no: \n")
    if another_input == "yes":
        print(" ")
        continue
    else:
        print(" ")
        break

# Round salaries to the nearest 100
round_sal = [round(salary, 2) for salary in salaries]

# Average of the salaries inputted
def avg_sal():
    global average
    average = sum(round_sal) / len(round_sal)
    return round(average, 2)

# Set Range
minRange = avg_sal() - 50
maxRange = avg_sal() + 50

# Salaries within range
for average in round_sal:
    if average >= minRange and average <= maxRange:
        avg_range.append(average)

# Print statements of results
print("Salary Analysis Results:")
print("Salaries: ", salaries)
print ("Rounded salaries: ", round_sal)
print("Average of the employee's salaries: $" + str(avg_sal()))

# If list is empty
if len(avg_range) == 0:
    print("No employee salaries are within the salary range.")
else:
    print("Employees within salary range of +/- $5000: $" + str(avg_range))
# Minimum Range is below 0
if minRange < 0:
    print("Please restart the program. Minimum range is below $0.")