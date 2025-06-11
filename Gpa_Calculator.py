# GPA Calculator with SGPA, CGPA, and Target CGPA Estimator
# ----------------------------------------------------------
# This script helps calculate SGPA, CGPA, and estimate the SGPA
# required in the next semester to achieve a target CGPA.
# Designed with edge case handling and clear structure for ease of use.

# Function to get valid integer input within an optional range
def get_int_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            val = int(input(prompt))
            if (min_value is not None and val < min_value) or (max_value is not None and val > max_value):
                print(f"[!] Please enter an integer between {min_value} and {max_value}.")
                continue
            return val
        except ValueError:
            print("[!] Invalid input. Please enter an integer.")

# Function to get valid float input within an optional range
def get_float_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            val = float(input(prompt))
            if (min_value is not None and val < min_value) or (max_value is not None and val > max_value):
                print(f"[!] Please enter a number between {min_value} and {max_value}.")
                continue
            return val
        except ValueError:
            print("[!] Invalid input. Please enter a number.")

# Function to calculate SGPA based on subject grades and credits
def calculate_sgpa():
    print("\n********* SGPA CALCULATOR *********")
    no_of_subjects = get_int_input("Enter the total number of subjects: ", min_value=1)

    credit_sum = 0
    total_credit = 0

    # Mapping of grades to grade points
    grade_to_point = {
        'EX': 10, 'S': 10, 'A+': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'P': 5, 'E': 4,
        'F': 0, 'FR': 0, 'U': None
    }

    for i in range(1, no_of_subjects + 1):
        print(f"\nSubject {i}:")
        grade_input = input("  → Enter Grade (EX, S, A, B, C, D, E, P, F, FR, U): ").strip().upper()
        credit_point = get_int_input("  → Enter Credit Points (1 or more): ", min_value=1)

        grade_point = grade_to_point.get(grade_input)

        # Handle U grade separately
        if grade_input == 'U':
            print("  [!] 'U' grade found. Skipping this subject.")
            continue
        elif grade_point is None:
            print("  [!] Invalid grade entered. Skipping this subject.")
            continue
        elif grade_point == 0:
            print("  [!] Fail grade detected. Grade point = 0 but credit is counted.")

        total_credit += grade_point * credit_point
        credit_sum += credit_point

    print("\n====================================")
    if credit_sum > 0:
        sgpa = total_credit / credit_sum
        print(f"Your SGPA is: {round(sgpa, 2)}")
    else:
        print("SGPA could not be calculated. Please check your input.")
    print("====================================\n")

# Function to calculate CGPA based on SGPAs and credits of previous semesters
def calculate_cgpa():
    print("\n********* CGPA CALCULATOR *********")
    num_semesters = get_int_input("Enter total number of semesters: ", min_value=1)

    weighted_total = 0
    total_credits = 0

    for i in range(1, num_semesters + 1):
        print(f"\nSemester {i}:")
        sgpa = get_float_input("  → Enter SGPA (0-10): ", min_value=0, max_value=10)
        semester_credits = get_int_input("  → Enter total credits for this semester: ", min_value=1)

        weighted_total += sgpa * semester_credits
        total_credits += semester_credits

    print("\n====================================")
    if total_credits > 0:
        cgpa = weighted_total / total_credits
        print(f"Your CGPA is: {round(cgpa, 2)}")
    else:
        print("CGPA could not be calculated. No valid credit entries found.")
    print("====================================\n")

# Function to calculate required SGPA to achieve a target CGPA
def calculate_required_sgpa():
    print("\n****** Required SGPA Calculator ******")

    current_cgpa = get_float_input("Enter your current CGPA (0-10): ", min_value=0, max_value=10)
    current_credits = get_int_input("Enter total credits completed so far: ", min_value=1)
    desired_cgpa = get_float_input("Enter your target CGPA (0-10): ", min_value=0, max_value=10)
    upcoming_credits = get_int_input("Enter credit points in next semester: ", min_value=1)

    required_total_points = desired_cgpa * (current_credits + upcoming_credits)
    current_total_points = current_cgpa * current_credits
    needed_points = required_total_points - current_total_points

    required_sgpa = needed_points / upcoming_credits

    print("\n====================================")
    if required_sgpa > 10:
        print(f"You need an SGPA of {round(required_sgpa, 2)}, which is more than 10. It's not possible.")
    elif required_sgpa < 0:
        print("Your current CGPA is already above the target CGPA!")
    else:
        print(f"To reach a CGPA of {desired_cgpa}, you need an SGPA of {round(required_sgpa, 2)} in your next semester.")
    print("====================================\n")

# Main menu to navigate between options
def main():
    while True:
        print("\n========= GPA CALCULATOR =========")
        print("1. Calculate SGPA")
        print("2. Calculate CGPA")
        print("3. Calculate Required SGPA for Target CGPA")
        print("4. Exit")
        choice = input("Select an option (1/2/3/4): ").strip()

        if choice == '1':
            calculate_sgpa()
        elif choice == '2':
            calculate_cgpa()
        elif choice == '3':
            calculate_required_sgpa()
        elif choice == '4':
            print("Thank you for using the GPA Calculator!")
            break
        else:
            print("[!] Invalid choice. Please select 1, 2, 3, or 4.")

# Start the program
main()