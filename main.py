import mysql.connector

# -----------------------------
# MySQL CONNECTION
# -----------------------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="loan_project"
    )

# -----------------------------
# EMI CALCULATION
# -----------------------------
def calculate_emi(P, R, N):
    R = R / (12 * 100)
    N = N * 12

    emi = (P * R * (1 + R)**N) / ((1 + R)**N - 1)
    return emi

# -----------------------------
# AMORTIZATION SCHEDULE
# -----------------------------
def amortization_schedule(P, R, N, emi):
    R = R / (12 * 100)
    N = N * 12

    schedule = []
    outstanding = P

    for month in range(1, N + 1):
        interest = outstanding * R
        principal = emi - interest
        outstanding -= principal

        schedule.append({
            "Month": month,
            "Principal Paid": round(principal, 2),
            "Interest Paid": round(interest, 2),
            "Remaining Amount": round(outstanding, 2)
        })

        if outstanding <= 0:
            break

    return schedule

# -----------------------------
# SAVE LOAN RESULT TO MYSQL
# -----------------------------
def save_to_mysql(name, P, R, T, emi, total_interest, total_payment):
    db = connect_db()
    cursor = db.cursor()

    query = """
    INSERT INTO loans (loan_name, principal, interest_rate, tenure_years, emi, total_interest, total_payment)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (name, P, R, T, emi, total_interest, total_payment)
    cursor.execute(query, values)
    db.commit()
    db.close()

# -----------------------------
# MAIN LOAN INPUT FUNCTION
# -----------------------------
def process_loan():
    name = input("\nEnter loan name: ")
    P = float(input("Enter Principal Amount: "))
    R = float(input("Enter Interest Rate (yearly %): "))
    T = int(input("Enter Tenure (years): "))

    emi = calculate_emi(P, R, T)
    N = T * 12
    total_payment = emi * N
    total_interest = total_payment - P

    print("\n--- Loan Summary ---")
    print(f"Loan Name: {name}")
    print(f"EMI: {emi:.2f}")
    print(f"Total Interest: {total_interest:.2f}")
    print(f"Total Payment: {total_payment:.2f}")

    save_to_mysql(name, P, R, T, emi, total_interest, total_payment)

    show_schedule = input("Show amortization schedule? (yes/no): ").lower()
    if show_schedule == "yes":
        schedule = amortization_schedule(P, R, T, emi)
        for row in schedule:
            print(row)

    print("\nLoan saved to MySQL successfully!")
    return {
        "name": name,
        "emi": emi,
        "total_interest": total_interest,
        "total_payment": total_payment
    }

# -----------------------------
# COMPARE MULTIPLE LOANS
# -----------------------------
def compare_loans():
    count = int(input("How many loans do you want to compare? (2 or 3): "))
    loans = []

    for i in range(count):
        print(f"\nEnter details for Loan {i+1}")
        loan = process_loan()
        loans.append(loan)

    print("\n======================")
    print(" 🔍 LOAN COMPARISON ")
    print("======================")

    for l in loans:
        print(f"\nLoan: {l['name']}")
        print(f"EMI: {l['emi']:.2f}")
        print(f"Total Interest: {l['total_interest']:.2f}")
        print(f"Total Payment: {l['total_payment']:.2f}")

# Run the project
compare_loans()
