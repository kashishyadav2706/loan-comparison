# Loan Comparison System 💰📊

A Python-based **Loan Comparison System** that helps users calculate EMI, generate amortization schedules, store loan details in MySQL, and compare multiple loans based on total interest and total payment.

---

## 📌 Features

* Calculate **EMI (Equated Monthly Installment)**
* Generate **loan amortization schedule**
* Store loan details in **MySQL database**
* Compare **2 or 3 loans** easily
* Console-based interactive program
* Accurate financial calculations

---

## 🛠️ Technologies Used

* **Python 3**
* **MySQL**
* `mysql-connector-python` library

---

## 📂 Project Structure

```
Loan-Comparison/
│
├── loan_comparison.py   # Main Python script
├── README.md            # Project documentation
```

---

## ⚙️ Database Setup

Create a MySQL database and table before running the project.

### 1️⃣ Create Database

```sql
CREATE DATABASE loan_project;
USE loan_project;
```

### 2️⃣ Create Table

```sql
CREATE TABLE loans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    loan_name VARCHAR(100),
    principal FLOAT,
    interest_rate FLOAT,
    tenure_years INT,
    emi FLOAT,
    total_interest FLOAT,
    total_payment FLOAT
);
```

---

## 🔧 Configuration

Update your MySQL credentials in the code if needed:

```python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="loan_project"
)
```

---

## ▶️ How to Run

1. Install required library:

```bash
pip install mysql-connector-python
```

2. Run the program:

```bash
python loan_comparison.py
```

3. Enter loan details when prompted:

   * Loan Name
   * Principal Amount
   * Interest Rate (%)
   * Tenure (years)

4. Choose whether to display the amortization schedule.

---

## 📊 Sample Output

```
--- Loan Summary ---
Loan Name: Home Loan
EMI: 23500.45
Total Interest: 1850023.40
Total Payment: 4850023.40
```

### Loan Comparison Output

```
🔍 LOAN COMPARISON

Loan: Home Loan
EMI: 23500.45
Total Interest: 1850023.40
Total Payment: 4850023.40
```

---

## 🚀 Future Improvements

* Add **GUI (Tkinter / Web App)**
* Export results to **CSV or PDF**
* Graphical comparison charts
* User authentication
* Error handling & validation

---

## 👨‍💻 Author

**Your Name**
GitHub: [https://github.com/kashishyadav2706](https://github.com/kashishyadav2706)

---

## 📄 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute.

---

⭐ If you like this project, don’t forget to give it a star!
