# Salary Calculator

## Overview
The Salary Calculator is a Python program that computes the net salary after deductions, including SSS, PhilHealth, Pag-IBIG, and income tax. Users input their monthly salary, and the program calculates and displays a detailed salary breakdown.

## Refactored Changes

### Enhancements & Fixes

#### Input Validation & Error Handling
- Ensured salary input is a positive numeric value.
- Added exception handling for invalid inputs to prevent crashes.
- Prevented zero or negative salary inputs.

#### Code Readability & Maintainability
- Improved variable naming for better clarity.
- Standardized formatting in salary breakdown output.
- Fixed syntax errors in the main execution check.

## Technical Debt Identified
- The income tax calculation is currently a fixed value, which is not dynamic or based on actual tax brackets.
- The SSS contribution is hardcoded instead of being computed based on official tables.
- No unit tests are implemented to verify the correctness of calculations.

## Refactoring Improvements Made
- Implemented robust error handling for salary input.
- Enhanced user experience by ensuring input validation.
- Increased code maintainability by fixing syntax issues and improving clarity.

## Challenges Faced & Solutions

### Handling Invalid Inputs Gracefully
**Solution:** Used a `while True` loop with exception handling to continuously prompt the user until a valid salary is entered.

### Ensuring Accurate and Realistic Salary Deductions
**Solution:** Identified areas where deductions need to be dynamically calculated (e.g., tax brackets, SSS tables) for future improvements.

### Correcting Minor Syntax Errors
**Solution:** Fixed `if __name__ == "_main_":` to `if __name__ == "__main__":` to ensure proper script execution.

