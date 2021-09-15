#Ashkan Ghomizadeh Thursdays 14:00 - 18:00
#tedad mivehaye monhaser be fard
def exclusive_fruits_counter(fruits:list) -> int:
    fruit_counter = list()
    a = 0
    if fruits[a] in fruit_counter:
        a = a + 1
    else:
        fruit_counter.append(fruits[a])
        a = a + 1
    if fruits[a] in fruit_counter:
        a = a + 1
    else:
        fruit_counter.append(fruits[a])
        a = a + 1
    if fruits[a] in fruit_counter:
        a = a + 1
    else:
        fruit_counter.append(fruits[a])
        a = a + 1
    if fruits[a] in fruit_counter:
        a = a + 1
    else:
        fruit_counter.append(fruits[a])
        a = a + 1
    if fruits[a] in fruit_counter:
        a = a + 1
    else:
        fruit_counter.append(fruits[a])
        a = a + 1
    result = len(fruit_counter)
    return result
fruits = [input("Miveye avval's gonna be: \n"),\
input("Miveye dovvom's gonna be: \n"),input("Miveye sevvom's gonna be: \n"),\
input("Miveye chaharom's gonna be: \n"), input("Miveye panjom's gonna be: \n")]
printable = exclusive_fruits_counter(fruits)
print(printable)
