# Password Strength Checker 🔒

A simple Python script to check the strength of passwords. The script analyzes a password based on length, uppercase letters, lowercase letters, numbers, special characters, and common patterns. It provides a score and actionable feedback to help improve password security.

## Features

- Checks for minimum length (8+ characters recommended)
- Detects uppercase and lowercase letters
- Checks for numbers and special characters
- Identifies common weak patterns like "123456" or "password"
- Provides a clear score and strength rating
- Gives suggestions to improve password strength

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git

Navigate to the project folder:

cd password-strength-checker

Run the script:

python password_checker.py

Enter a password when prompted and see the analysis.

Example Output
🔒 Password Strength Checker 🔒
Enter a password to check: P@ssw0rd123

========================================
🔐 PASSWORD STRENGTH ANALYSIS
========================================
✅ Good length
✅ Has uppercase letters
✅ Has lowercase letters
✅ Has numbers
✅ Has special characters
----------------------------------------
Strength: 🟢 STRONG 💪 (Score: 6/7)
Requirements

Python 3.x

No external libraries required (uses built-in re module)
