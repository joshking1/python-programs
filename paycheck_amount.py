
#!/usr/bin/python3 

regular_rate = 20  # Regular hourly rate
overtime_rate = 30  # Overtime hourly rate
max_regular_hours = 40  # Maximum regular hours

# Input the number of hours worked
hours = float(input("Enter the number of hours worked: "))

if hours <= max_regular_hours:
    # Calculate regular paycheck amount
    regular_paycheck = hours * regular_rate
    total_paycheck = regular_paycheck
else:
    # Calculate regular paycheck amount
    regular_paycheck = max_regular_hours * regular_rate
    # Calculate overtime paycheck amount
    overtime_paycheck = (hours - max_regular_hours) * overtime_rate
    total_paycheck = regular_paycheck + overtime_paycheck

# Output the total paycheck amount
print("The total paycheck amount is:", total_paycheck)
