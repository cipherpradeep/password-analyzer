import re

def analyze_password(password):
    """
    Analyze the password for various criteria.
    """
    analysis = {
        "length": len(password) >= 12,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "numbers": bool(re.search(r"[0-9]", password)),
        "special_characters": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),  # Fixed: Added password argument
        "recommendations": []
    }

    # Add recommendations based on missing criteria
    if not analysis["length"]:
        analysis["recommendations"].append("Use at least 12 characters.")
    if not analysis["uppercase"]:
        analysis["recommendations"].append("Include at least one uppercase letter.")
    if not analysis["lowercase"]:
        analysis["recommendations"].append("Include at least one lowercase letter.")
    if not analysis["numbers"]:
        analysis["recommendations"].append("Include at least one number.")
    if not analysis["special_characters"]:
        analysis["recommendations"].append("Include at least one special character (e.g., !@#$%).")

    return analysis

def evaluate_strength(analysis):
    """
    Evaluate the overall strength of the password based on the analysis.
    """
    criteria_met = sum([
        analysis["length"],
        analysis["uppercase"],
        analysis["lowercase"],
        analysis["numbers"],
        analysis["special_characters"]
    ])

    if criteria_met == 5:
        return "Strong"
    elif criteria_met >= 3:
        return "Moderate"
    else:
        return "Weak"

def main():
    print("Welcome to the Password Analyzer!")
    print("This tool will evaluate the strength of your password and provide recommendations for improvement.\n")

    # Prompt user for password input
    password = input("Enter the password you want to analyze: ")

    # Analyze the password
    analysis = analyze_password(password)

    # Display analysis results
    print("\nPassword Analysis Results:")
    print(f"1. Length (at least 12 characters): {'✔' if analysis['length'] else '✘'}")
    print(f"2. Contains Uppercase Letters: {'✔' if analysis['uppercase'] else '✘'}")
    print(f"3. Contains Lowercase Letters: {'✔' if analysis['lowercase'] else '✘'}")
    print(f"4. Contains Numbers: {'✔' if analysis['numbers'] else '✘'}")
    print(f"5. Contains Special Characters: {'✔' if analysis['special_characters'] else '✘'}")

    # Provide recommendations for improvement
    if analysis["recommendations"]:
        print("\nRecommendations to Improve Password Strength:")
        for i, recommendation in enumerate(analysis["recommendations"], start=1):
            print(f"{i}. {recommendation}")

    # Evaluate overall password strength
    strength = evaluate_strength(analysis)
    print(f"\nOverall Password Strength: {strength}")

if __name__ == "__main__":
    main()
