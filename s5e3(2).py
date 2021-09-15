#Ashkan Ghomizadeh Thursdays 14:00 - 18:00
#tedad mivehaye monhaser be fard
def exclusive_fruits_counter(fruits:list) -> int:
    fruits_set = set()
    fruits_set.add(fruits[0])
    fruits_set.add(fruits[1])
    fruits_set.add(fruits[2])
    fruits_set.add(fruits[3])
    fruits_set.add(fruits[4])
    result = len(fruits_set)
    return result
fruits = [input("Miveye avval's gonna be: \n"),\
input("Miveye dovvom's gonna be: \n"),input("Miveye sevvom's gonna be: \n"),\
input("Miveye chaharom's gonna be: \n"), input("Miveye panjom's gonna be: \n")]
printable = exclusive_fruits_counter(fruits)
print(printable)
