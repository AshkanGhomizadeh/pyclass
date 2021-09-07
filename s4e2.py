#Ashkan Ghomizadeh Thursdays 14:00 - 18:00
#Cone and sphere calculator
def cone(radius:float, height:float) -> str:
    if feature == "surface area":
        length = ((radius ** 2) + (height ** 2)) ** 0.5
        amount = (3.14 * radius * length) + (3.14 * radius ** 2)
        result = f"The cone surface area equals = {amount}"
    elif feature == "volume":
        amount = 3.14 * (radius ** 2) * height / 3
        result = f"The cone volume equals = {amount}"
    else:
        result = "Are you in the loop?"
    return result
def sphere(radius: float) -> str:
    if feature == "surface area":
        amount = 4 * 3.14 * (radius ** 2)
        result = f"The sphere surface area equals = {amount}"
    elif feature == "volume":
        amount = 4 / 3 * (radius ** 3) * 3.14
        result = f"The sphere volume equals = {amount}"
    else:
        result = "Are you in the loop?"
    return result
shape = input('''Hey there,
Choose one!
Cone or Sphere\n''')
feature = input('''And also another choice.
Which feature of the mentioned shape you want to be calculated?
Surface area or Volume\n''')
shape = shape.lower()
feature = feature.lower()
if shape == "cone":
    radius = float(input('''How much is its radius?
    Mention it in cm!\n'''))
    height = float(input('''How about its height?
    Mention this one, also in cm!\n'''))
    last_result = cone(radius, height)
    print(last_result)
elif shape == "sphere":
    radius = float(input('''How much is its radius?
    Mention it in cm!\n'''))
    last_result = sphere(radius)
    print(last_result)
else:
    print("Are you in the loop?")
