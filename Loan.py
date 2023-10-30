import random
from datetime import date

def calculate_age(date_of_birth):
    birth_date = date.fromisoformat(date_of_birth)
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# User information
full_name = input("Enter your full name: ")
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
city_state = random.choice(["State1", "State2", "State3", "State4", "State5"])
employment_status = input("Enter your employment status: ")
employment_length = int(input("Enter the length of employment (in months): "))
annual_income = int(input("Enter your gross annual income: "))
bank_institution = input("Enter your bank institution: ")
house_ownership = input("Do you rent or own your home? ")
car_financing = input("Is your car financed, paid off, or leased? ")


# Loan amount and purpose
desired_loan_amount = float(input("Desired loan amount: "))
loan_purpose = input("Enter the purpose of the loan: ")

# Credit history
credit_score = int(input("Enter your credit score: "))

# Check if the user has ever had a loan
had_loan_before = input("Have you ever had a loan before? (yes/no): ")

# Reason for the loan
loan_reason = input("Why do you need a loan? How will it help you? (2 sentences): ")

# Loan approval criteria
age = 18  # Add code to calculate the age from date_of_birth

loan_limit = 5 if 18 <= age <= 24 else 10
income_threshold = 50000  # Annual income threshold
interest_rate = 0.05  # Default interest rate
banks_with_better_chances = ["JPMorgan Chase & Co.", "Bank of America", "Wells Fargo & Co.", "Citibank", "U.S. Bank", "PNC Financial Services Group"]
house_ownership_priority = {"rent": 0.8, "own": 1.0}
car_priority = {"financed": 1.2, "paid off": 1.0, "leased": 1.1}
loan_purpose_priority = {"home purchase": 0.9, "debt consolidation": 0.8, "car purchase": 0.85}

# Determine loan eligibility
eligible_for_loan = True

if annual_income < income_threshold:
    interest_rate += 0.02  # Higher interest rate for low income

if bank_institution in banks_with_better_chances:
    interest_rate -= 0.02  # Lower interest rate for preferred banks

if house_ownership in house_ownership_priority:
    interest_rate *= house_ownership_priority[house_ownership]

if car_financing in car_priority:
    interest_rate *= car_priority[car_financing]

if loan_purpose in loan_purpose_priority:
    interest_rate *= loan_purpose_priority[loan_purpose]

if had_loan_before.lower() == "no":
    loan_limit = 3  # Stricter loan limits for those without a loan history

if employment_length <= 5:
    eligible_for_loan = False  # Less than 6 months of employment reduces chances

# Check if the user is eligible for a loan
if eligible_for_loan:
    print("Congratulations! You are eligible for a loan.")
    
    # Generate loan options (simplified example)
    loan_options = [
        {"loan_amount": desired_loan_amount * 0.8, "interest_rate": interest_rate * 1.1},
        {"loan_amount": desired_loan_amount, "interest_rate": interest_rate},
        {"loan_amount": desired_loan_amount * 1.2, "interest_rate": interest_rate * 0.9}
    ]
    
    # Display loan options
    print("Loan Options:")
    for i, option in enumerate(loan_options, start=1):
        print(f"{i}. Loan Amount: ${option['loan_amount']:.2f}, Interest Rate: {option['interest_rate'] * 100:.2f}%")
    
    # Allow the user to choose from these options
    selected_option = int(input("Select a loan option (1, 2, 3): "))
    
    if 1 <= selected_option <= len(loan_options):
        selected_loan = loan_options[selected_option - 1]
        print(f"Congratulations! You've been approved for a loan of ${selected_loan['loan_amount']:.2f} at an interest rate of {selected_loan['interest_rate'] * 100:.2f}%.")
    else:
        print("Invalid selection. Please try again.")
else:
    print("Sorry, you are not eligible for a loan at this time. Please try again later.")
