# Ashkan Ghomizadeh Thursdays 14:00 - 18:00
# BASIC CALCULATOR (SESSION 3)
def basic_calculator(adad1, adad2, amalgar):
    if amalgar == "+":
        print(adad1 + adad2)
    elif amalgar == "-":
        print(adad1 - adad2)
    elif amalgar == "*":
        print(adad1 * adad2)
    elif amalgar == "**":
        print(adad1 ** adad2)
    elif amalgar == "/":
        print(adad1 / adad2)
    elif amalgar == "//":
        print(adad1 // adad2)
    elif amalgar == "%":
        print(adad1 % adad2)
print('''Salam,
Darkhaste Khod ra vared konid''')
basic_calculator(float(input("Adade avval: \n")), float(input("Adade \n\
dovvom: \n")), input("Amalgar: \n"))
