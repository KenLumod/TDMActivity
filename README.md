# Salary Calculator

## Overview
The Salary Calculator is a Python program designed to compute the net salary after deductions, including SSS, PhilHealth, Pag-IBIG, and income tax. Users input their monthly salary, and the program calculates and displays a detailed salary breakdown.

---

## Refactored Changes

### Enhancements & Fixes

#### **Input Validation & Error Handling:**
- Ensured that the salary input is a positive numeric value.
- Added exception handling to handle invalid inputs (e.g., non-numeric values).
- Prevented zero or negative salary inputs by continuously prompting users until a valid salary is entered.

#### **Code Readability & Maintainability:**
- Improved variable naming for better clarity (e.g., `gross_salary` instead of `salary`).
- Standardized the formatting in the salary breakdown output for readability.
- Fixed syntax errors, including the main execution check (`if __name__ == "__main__":`).

#### **Technical Debt Identified:**
- The income tax calculation is a fixed value and not dynamic or based on actual tax brackets.
- The SSS contribution is hardcoded, rather than being computed based on official tables.
- No unit tests have been implemented to verify the correctness of calculations.

### Refactoring Improvements Made:
- **Implemented robust error handling for salary input:**  
  Users are prompted to input a valid salary using a while loop with exception handling for non-numeric values.
  
- **Enhanced user experience by ensuring input validation:**  
  Non-positive and invalid salary inputs are caught, and users are re-prompted until they provide a valid salary.

- **Increased code maintainability by fixing syntax issues and improving clarity:**  
  Clearer variable names and standardized formatting make the code easier to read and maintain.

---

## Code Explanation

### **Class-Based Structure:**
The code has been refactored to use a `SalaryCalculator` class for better organization, modularity, and maintainability.

- **Class:**  
  The `SalaryCalculator` class groups all salary-related methods. It encapsulates the salary data and computation of deductions like SSS, PhilHealth, Pag-IBIG, and income tax, making the program more organized and easier to extend.

- **Constructor (`__init__` method):**  
  The constructor initializes the object with the `gross_salary` input and calculates the necessary deductions (SSS, PhilHealth, Pag-IBIG, and tax).

- **Methods:**  
  Each deduction calculation is handled by a separate method, making the code more modular and maintainable. These methods include:
  - `compute_sss_contribution()`
  - `compute_philhealth_contribution()`
  - `compute_pagibig_contribution()`
  - `compute_income_tax()`
  - `compute_total_deductions()`

- **Main Function:**  
  The `main()` function handles the user input and orchestrates the flow of the program, creating an instance of `SalaryCalculator` and calling the `display_salary_breakdown()` method to display the results.

---
