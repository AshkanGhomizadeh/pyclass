#Ashkan Ghomizadeh Thursdays 14:00 - 18:00
#Listi az esm ha ra ba horoof joda va beyne har esm ham fasele biyandazid
names = list()
while True:
    yes_or_no = input("Aya esme jadid dari?\n")
    if yes_or_no == "no":
        break
    else:
        name = input("Name e morede nazar ra vared konid.\n")
        name = name + "-"
        names.append(name)
if len(names) == 0:
     print("Liste shoma khalist!")
else:
    for name in names :
        for harf in name:
            print(harf)
