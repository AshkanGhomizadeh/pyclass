# Ashkan Ghomizadeh Thursdays 14:00 - 18:00
# MOHASEBEYE MOHIT VA MASAHATE ASHKALE HENDESI (SESSION 3)
def mohit_mashate_ashkale_hendesi(darkhast, shekl):
    darkhast = darkhast.lower()
    shekl = shekl.lower()
    if shekl == "mostatil":
        a = float(input("Toole mostatil vared shavad \n"))
        b = float(input("Arze mostatil vared shavad \n"))
        if darkhast == "mohit":
            print(f"Mohite mostatil = {(a + b)*2}")
        if darkhast == "masahat":
            print(f"Masahate mostatil = {a * b}")
    if shekl == "mosallas":
        a = float(input("Ghaede vared shavad \n"))
        if darkhast == "masahat":
            b = float(input("Ertefa vared shavad \n"))
            print(f"Masahate mosallas = {a * b / 2}")
        elif darkhast == "mohit":
            print(f"Mohite mosallas = {a * 3}")
    if shekl == "dayere":
        a = float(input("Shoaa vared shavad \n"))
        if darkhast == "mohit":
            print(f"Mohite dayere = {2 * 3.14 * a}")
        if darkhast == "masahat":
            print(f"Masahate dayere = {3.14 * (a**2)}")
    if shekl == "lozi":
        if darkhast == "mohit":
            c = float(input("Zele lozi vared shavad \n"))
            print(f"Mohite lozi = {c * 4}")
        if darkhast == "masahat":
            a = float(input("Toole ghotre bozorg vared shavad \n"))
            b = float(input("Toole ghotre koochik vared shavad \n"))
            print(f"Masahate lozi = {a * b / 2}")
    if shekl == "zoozanaghe":
        a = float(input("Toole ghaedeye bozorg vared shavad \n"))
        b = float(input("Toole ghaedeye koochik vared shavad \n"))
        if darkhast == "mohit":
            print(f"Mohite zoozanaghe = {(a + b) * 2}")
        if darkhast == "masahat":
            c = float(input("Ertefaa vared shavad \n"))
            print(f"Masahate zoozanaghe = {(a + b) * c / 2}")
    if shekl == "morabba":
        a = float(input("Toole morabba vared shavad \n"))
        if darkhast == "mohit":
            print(f"Mohite morabba = {a * 4}")
        if darkhast == "masahat":
            print(f"Masahate morabba = {a ** 2}")
    if shekl == "motevaziolazlaa":
        a = float(input("Zel vared shavad \n"))
        if darkhast == "mohit":
            c = float(input("Digar zel vared shavad \n"))
            print(f"Mohite motevaziolazlaa = {(a + c) * 2}")
        if darkhast == "masahat":
            b = float(input("Ertefa vared shavad \n"))
            print(f"Masahate motevaziolazlaa = {a * b}")
mohit_mashate_ashkale_hendesi(input("Mohit ya masahat? \n"), input("Che she\
kli? \n"))
