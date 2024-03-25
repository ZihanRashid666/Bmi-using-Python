def calculate_bmi(weight, height):
    if weight > 0 and height > 0:
        final_bmi = weight / ((height / 100) ** 2)
        if final_bmi < 18.5:
            meaning = "That you are too thin."
        elif final_bmi >= 18.5 and final_bmi < 25:
            meaning = "That you are healthy."
        else:
            meaning = "That you have overweight."
        return final_bmi, meaning
    else:
        return None, "Please fill in everything correctly."

def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    bmi, meaning = calculate_bmi(weight, height)
    if bmi is not None:
        print(f"Your BMI: {bmi}")
        print(f"This means: {meaning}")
    else:
        print(meaning)

if __name__ == "__main__":
    main()
