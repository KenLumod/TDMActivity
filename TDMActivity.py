class SalaryCalculator:
    def __init__(self, gross_salary):
        self.gross_salary = gross_salary
        self.sss = self.compute_sss_contribution()
        self.philhealth = self.compute_philhealth_contribution()
        self.pagibig = self.compute_pagibig_contribution()
        self.tax = self.compute_income_tax()
        self.total_deductions = self.compute_total_deductions()
        self.net_salary = self.gross_salary - self.total_deductions

    def compute_sss_contribution(self):
        return 1200

    def compute_philhealth_contribution(self):
        return (self.gross_salary * 0.05) / 2

    def compute_pagibig_contribution(self):
        return 100

    def compute_income_tax(self):
        return 1875  # Assuming fixed value for simplicity

    def compute_total_deductions(self):
        return self.sss + self.philhealth + self.pagibig + self.tax

    def display_salary_breakdown(self):
        print("\nSalary Breakdown")
        print("=================")
        print(f"Gross Salary: {self.gross_salary:.2f}")
        print(f"SSS Deduction: {self.sss:.2f}")
        print(f"PhilHealth Deduction: {self.philhealth:.2f}")
        print(f"Pag-IBIG Deduction: {self.pagibig:.2f}")
        print(f"Tax Deduction: {self.tax:.2f}")
        print(f"Total Deductions: {self.total_deductions:.2f}")
        print(f"Net Salary: {self.net_salary:.2f}")

def main():
    salary = float(input("Enter your monthly salary: "))
    calculator = SalaryCalculator(salary)
    calculator.display_salary_breakdown()

if _name_ == "_main_":
    main()