#Ashkan Ghomizadeh Thursdays 14:00 - 18:00
#Miyangine liste delkhahe karbar
user_list = list()
sum = 0
while True:
    user_input = input("Would you like to enter a new number?\n")
    user_input = user_input.lower()
    if user_input == "no":
        break
    else:
        user_number = float(input("Adad ra vared konid.\n"))
    user_list.append(user_number)
for number in user_list:
    sum = sum + number
if len(user_list) == 0:
    average = 0
else:
    average = sum / len(user_list)
print(f"The average equals : {average}")
