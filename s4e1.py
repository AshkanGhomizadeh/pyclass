#Ashkan Ghomizadeh Thursdays 14:00 - 18:00
#BMI WITH FUNCTIONS USAGE
def bmi_calculator(mass: float, height: float) -> float:
    '''
    This function calculates the BMI refered to your entered information.
    '''
    bmi = mass / (height ** 2)
    return bmi
def bmi_ranges(mass: float, height: float) -> str:
    '''
    This function shows your BMI health class.
    '''
    info = bmi_calculator(mass, height)
    if info < 16.5:
        return (f"Severly Underweight : {info}")
    if 16.5 <= info < 18.5:
        return (f"Underweight : {info}")
    if 18.5 <= info < 25:
        return (f"Normal Weight : {info}")
    if 25 <= info < 30:
        return (f"Overweight : {info}")
    if 30 <= info < 35:
        return (f"Obesity Class I : {info}")
    if 35 <= info < 40:
        return (f"Obesity Class II : {info}")
    if 40 <= info:
        return (f"Obesity Class III : {info}")
user_mass = float(input('''Hey there,
Enter your mass in kilogram please!\n'''))
user_height = float(input("And, your height in meter please!\n"))
code_result = bmi_ranges(user_mass, user_height)
print(code_result)
