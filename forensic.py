
# Forensic case management model example using data types, operators, output, etc.

# Basic case information

# Unique identifier for each forensic case - string
case_id = "FRS-2024-03"

# Date on which the case was opened - string
case_opendate = "12-08-2024"

# Total number of cases
case_total = 246

# No.of currently active cases
case_active = 46

# Percentage of solved cases as decimal - 91% - float
case_solved_rate = 0.91

# Evidence and analysis statistics
# Total evidence items collected
item_total_evidence = 100

# Average Evidence per case
avg_evidence = item_total_evidence / case_total

# List (array) for daily activities - past 7 days
daily_evidence_collected = [5,7,6,8,9,2]
daily_cases_opened = [1,2,3,4,1,2]

# Dictionary for case type breakdown
case_types = {
"Theft": 85,
"Fraud": 55,
"Assault": 34,
"Cybercrime": 10
}

# Perform arithmetic operations
average_daily_cases_opened = sum(daily_cases_opened)/len(daily_cases_opened)
print("Average number of daily cases opened is: ", average_daily_cases_opened)
remaining_cases = case_total - case_active
print("The remaining cases amount to be: ", remaining_cases)

# Increment total cases by 5
case_total += 5

# Decrement total cases by 2

case_active -= 2

# Display forensic case summary
print("-----Forensic case summary------")
# print("Case ID: ", case_id)
print(f"Case ID: {case_id}")
print(f"Date on which the case was opened: {case_opendate}")
print(f"Total cases are: {case_total}")
print(f"The number of active cases: {case_active}")
print(f"The rate of solved cases: {case_solved_rate}")

# Logical and comparison operations

high_case_load = case_active > 40 and case_solved_rate < 0.9
print("------High case load and risk assesment--------")
if high_case_load:
	print("Warning high case load - requires additional resources")
else:
	print("Current case load is manageable.")



