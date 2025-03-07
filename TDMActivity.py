def compute_deductions(monthly_salary):
    sss_contribution = 1200
    philhealth_contribution = (monthly_salary * 0.05) / 2
    pagibig_contribution = 100
    income_tax = 1875

    total_deductions = sss_contribution + philhealth_contribution + pagibig_contribution + income_tax
    net_monthly_salary = monthly_salary - total_deductions

    print("Gross Monthly Salary: {:.2f}".format(monthly_salary))
    print("SSS Contribution: {:.2f}".format(sss_contribution))
    print("PhilHealth Contribution: {:.2f}".format(philhealth_contribution))
    print("Pag-IBIG Contribution: {:.2f}".format(pagibig_contribution))
    print("Income Tax: {:.2f}".format(income_tax))
    print("Total Deductions: {:.2f}".format(total_deductions))
    print("Net Monthly Salary: {:.2f}".format(net_monthly_salary))

monthly_salary = float(input("Enter your monthly salary: "))
compute_deductions(monthly_salary)
