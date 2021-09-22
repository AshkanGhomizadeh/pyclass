#Ashkan Ghomizadeh Thursdays 14:00 - 18:00
#Listi begirid va az n e delkhahe karbar ta akhar index o ozv begooyid ba while
names = list()
while True:
    yes_or_no = input("Aya farde jadidi dari?\n")
    yes_or_no.lower()
    if yes_or_no == "no":
        break
    else:
        name = input("Ozve jadid vared kon\n")
        names.append(name)
if len(names) == 0:
    print("Liste shoma khalist")
else:
    user_name = input("az che fardi bayan shavad?\n")
    index = names.index(user_name)
    while index <= (len(names) - 1):
        print(f"{names[index]} nafare {index + 1} dar list ast.")
        index = index + 1
