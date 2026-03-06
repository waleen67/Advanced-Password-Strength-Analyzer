import re


def check_password_strength(password):
    score = 0
    feedback = []


    if len(password) >= 12:
        score += 2
        feedback.append("✅ Good length")
    elif len(password) >= 8:
        score += 1
        feedback.append("⚠️  Decent length, but longer is better")
    else:
        feedback.append("❌ Password too short (minimum 8 characters)")


    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✅ Has uppercase letters")
    else:
        feedback.append("❌ Add uppercase letters")


    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✅ Has lowercase letters")
    else:
        feedback.append("❌ Add lowercase letters")


    if re.search(r'\d', password):
        score += 1
        feedback.append("✅ Has numbers")
    else:
        feedback.append("❌ Add numbers")


    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("✅ Has special characters")
    else:
        feedback.append("❌ Add special characters")


    common_patterns = ['password', '123456', 'qwerty', 'abc123']
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 2
        feedback.append("❌ Contains common patterns")

  
    print("\n" + "=" * 40)
    print("🔐 PASSWORD STRENGTH ANALYSIS")
    print("=" * 40)

    for item in feedback:
        print(item)

    print("-" * 40)

    if score >= 5:
        strength = "STRONG 💪"
        color = "🟢"
    elif score >= 3:
        strength = "MODERATE ⚠️"
        color = "🟡"
    else:
        strength = "WEAK ❌"
        color = "🔴"

    print(f"Strength: {color} {strength} (Score: {score}/7)")

    if score < 5:
        print("\nSuggestions for improvement:")
        for item in feedback:
            if item.startswith("❌"):
                print(f"  • {item[2:]}")


def main():
    print("🔒 Password Strength Checker 🔒")
    password = input("Enter a password to check: ")
    check_password_strength(password)


if __name__ == "__main__":
    main()
