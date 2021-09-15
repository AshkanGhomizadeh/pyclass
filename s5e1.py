#Ashkan Ghomizaeh Thursdays 14:00 - 18:00
#3 list ezafe shavad sepas baraks yeki dar miyan chap shavad
def task_achiever(nos:list, noss:list, nosss:list) -> list:
    nos.extend(noss + nosss)
    nos.reverse()
    nos = nos[::2]
    return nos
printable = task_achiever([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(printable)
