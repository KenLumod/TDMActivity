def compute_sss_contribution():
    return 1200

def compute_philhealth_contribution(gross_salary):
    return (gross_salary * 0.05) / 2

def compute_pagibig_contribution():
    return 100

def compute_income_tax():
    return 1875  # Assuming fixed value for simplicity

def compute_total_deductions(gross_salary):
    sss = compute_sss_contribution()
    philhealth = compute_philhealth_contribution(gross_salary)
    pagibig = compute_pagibig_contribution()
    tax = compute_income_tax()
    
    total = sss + philhealth + pagibig + tax
    return total, sss, philhealth, pagibig, tax

def display_salary_breakdown(gross_salary, sss, philhealth, pagibig, tax, total_deductions, net_salary):
    print("\nSalary Breakdown")
    print("=================")
    print(f"Gross Salary: {gross_salary:.2f}")
    print(f"SSS Deduction: {sss:.2f}")
    print(f"PhilHealth Deduction: {philhealth:.2f}")
    print(f"Pag-IBIG Deduction: {pagibig:.2f}")
    print(f"Tax Deduction: {tax:.2f}")
    print(f"Total Deductions: {total_deductions:.2f}")
    print(f"Net Salary: {net_salary:.2f}")

def main():
    salary = float(input("Enter your monthly salary: "))
    total_deductions, sss, philhealth, pagibig, tax = compute_total_deductions(salary)
    net_salary = salary - total_deductions
    display_salary_breakdown(salary, sss, philhealth, pagibig, tax, total_deductions, net_salary)

if __name__ == "__main__":
    main()