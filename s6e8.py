#Ashkan Ghomizadeh Thursdays 14:00 - 18:00
#Listi az esm ha ra ba horoof joda va beyne har esm ham fasele biyandazid(while)
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
    new_names = list()
    i = 0
    while i <= (len(names) - 1):
        new_names.append((names[i]))
        i += 1
    j = 0
    while j <= (len(new_names) - 1):
        each_name = new_names[j]
        each_name = list(each_name)
        r = 0
        while r <= (len(each_name) - 1):
            print(each_name[r])
            r += 1
        j += 1
