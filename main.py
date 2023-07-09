# Program Name: ExmaplePyFinal.py 
# Function:     Figure out Salaries within Range (+/- $5000)
# Input:        Float(integers)
# Output:       Salaries (rounded nearest 100)

# Lists
salaries = []

# Variables
default = 5000

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
    another_input = input("Is there another salary to enter? yes or no: \n" )
    if another_input == "yes":
        print(" ")
        continue
    else:
        print(" ")
        break

# Average of the salaries inputted
def avg_sal():
    average = sum(salaries) / len(salaries)
    return average

# Salaries within default range
minRange = avg_sal() - default
maxRange = avg_sal + default


# Print statements of results
print("Salary Analysis Results:")
print("Salaries: ", salaries)
print("Average of the employee's salaries: $" +str(avg_sal()))
# print("Salaries within +/-$5000: ")