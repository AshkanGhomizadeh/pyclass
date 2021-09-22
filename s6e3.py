#Ashkan Ghomizadeh Thursdays 14:00 - 18:00
#Miyangine liste delkhahe karbar ba taabe
def list_collector(clear_list: list = list()) -> list:
    while True:
        continuation = input("Aya adade jadid baraye vared kardan darid?\n")
        continuation.lower()
        if continuation == "no":
            break
        else:
            user_number = float(input("Adad ra vared konid.\n"))
            clear_list.append(user_number)
    return clear_list
def average_calculator(user_list: list) -> str:
    if len(user_list) == 0:
        last_result = "Miyangin barabare 0 ast"
    else:
        majmoo = sum(user_list)
        result = majmoo / len(user_list)
        last_result = f"Miyangin barabare {result} ast"
    return (last_result)
last_list = list_collector()
average = average_calculator(last_list)
print(average)
