#Ashkan Ghomizadeh Thursdays 14:00 - 18:00
#Daily Calorie needs calculator
def bmr_calculator(mass:float, height:float, age:int) -> float:
    gender = input("Let us know your gender.\n")
    gender = gender.lower()
    if gender == "female":
        bmr_result = 655.1 + (9.563 * user_mass) + (1.85 * user_height) -\
        (4.676 * user_age)
    elif gender == "male":
        bmr_result = 66.47 + (13.75 * user_mass) + (5.003 * user_height) -\
        (6.755 * user_age)
    else:
        print("Are you in the loop?!")
    return bmr_result
    amr_claculator(bmr_result)
def amr_claculator(user_bmr:float) -> str:
    life_style = input('''Mention your life style:
    Sedentary : No exercise
    Lightly active : exercise 1-3 days per week
    Moderately active : exercise 3-5 days per week
    Active : exercise 6-7 days per week
    Very Active : hard exercise 6-7 days per week\n''')
    life_style = life_style.lower()
    if life_style == "sedentary":
        amr_result_1 = user_bmr * 1.2
        amr_result_2 = (f'''You burn {amr_result_1} calories during a typical \
day.
        As a result to stabilize your mass you should consume this amount \
of calories per day.
        But, you can consume lower amounts for weight loss!''')
    elif life_style == "lightly active":
        amr_result_1 = user_bmr * 1.375
        amr_result_2 = (f'''You burn {amr_result_1} calories during a typical \
day.
        As a result to stabilize your mass you should consume this amount \
of calories per day.
        But, you can consume lower amounts for weight loss!''')
    elif life_style == "moderately active":
        amr_result_1 = user_bmr * 1.55
        amr_result_2 = (f'''You burn {amr_result_1} calories during a typical \
day.
        As a result to stabilize your mass you should consume this amount \
of calories per day.
        But, you can consume lower amounts for weight loss!''')
    elif life_style == "active":
        amr_result_1 = user_bmr * 1.725
        amr_result_2 = (f'''You burn {amr_result_1} calories during a typical \
day.
        As a result to stabilize your mass you should consume this amount \
of calories per day.
        But, you can consume lower amounts for weight loss!''')
    elif life_style == "very active":
        amr_result_1 = user_bmr * 1.9
        amr_result_2 = (f'''You burn {amr_result_1} calories during a typical \
day.
        As a result to stabilize your mass you should consume this amount \
of calories per day.
        But, you can consume lower amounts for weight loss!''')
    else:
        print("Are you in the loop?")
    return amr_result_2
user_mass = float(input('''Hey there,
Please make sure of answering the upcoming questions correctly, whether not \
you'll get a wrong result.
Enter your mass in Kg.\n'''))
user_height = float(input("And also, would you inform us, how tall you are in\
 cm?\n"))
user_age = int(input('''Finally,
Could you please mention your age?\n'''))
amr_input = bmr_calculator(user_mass, user_height, user_age)
code_output = amr_claculator(amr_input)
print(code_output)
