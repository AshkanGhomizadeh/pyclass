#Ashkan Ghomizadeh Thursdays 14:00 -18:00
#Algebraic identities
def square_of_a_binomal(a:float, b:float) -> str:
    '''
    This function calculates square of a binomal algebraic identities.
    '''
    if user_request == "I":
        amount = (a ** 2) + (2 * a * b) + (b ** 2)
        result = f"(a + b) ** 2 = (a ** 2) + (2 * a * b) + (b ** 2) = \
{amount}"
    if user_request == "II":
        amount = (a ** 2) - (2 * a * b) + (b ** 2)
        result = f"(a - b) ** 2 = (a ** 2) - (2 * a * b) + (b ** 2) = \
{amount}"
    return result
def difference_of_squares(a:float, b:float) -> str:
    '''
    This function calculates difference of squares algebraic identities.
    '''
    amount = (a + b) * (a - b)
    result = f"(a ** 2) - (b ** 2) = (a + b) * (a - b) = \
{amount}"
    return result
def cube_of_a_binomal(a:float, b:float) -> str:
    '''
    This function calculates cube of a binomal algebraic identities.
    '''
    if user_request == "IV":
        amount = (a ** 3) + (3 * a ** 2 * b) + (3 * b ** 2 * a) + (b ** 3)
        result = f"(a + b) ** 3 = (a ** 3) + (3 * a ** 2 * b)\
+ (3 * b ** 2 * a) + (b ** 3) = {amount}"
    if user_request == "V":
        amount = (a ** 3) - (3 * a ** 2 * b) + (3 * b ** 2 * a) - (b ** 3)
        result = f"(a - b) ** 3 = (a ** 3) - (3 * a ** 2 * b)\
+ (3 * b ** 2 * a) - (b ** 3) = {amount}"
    return result
def square_of_a_trinomal(a:float, b:float, c:float) -> str:
    '''
    This function calculates square of a trinomal algebraic identities.
    '''
    amount = (a ** 2) + (b ** 2) + (c ** 2) +\
(2 * a * b) + (2 * b * c) + (2 * c * a)
    result = f"(a + b + c) ** 2 = (a ** 2) + (b ** 2) + (c ** 2) +\
(2 * a * b) + (2 * b * c) + (2 * c * a) = {amount}"
    return result
def sum_of_cubes(a:float, b:float) -> str:
    '''
    This function calculates sum of cubes algebraic identities.
    '''
    amount = (a + b) * ((a ** 2) - (a * b) + (b ** 2))
    result = f"(a ** 3) + (b ** 3) = (a + b) *\
((a ** 2) - (a * b) + (b ** 2)) = {amount}"
    return result
def difference_of_cubes(a:float, b:float) -> str:
    '''
    This function calculates difference of cubes algebraic identities.
    '''
    amount = (a - b) * ((a ** 2) + (a * b) + (b ** 2))
    result = f"(a ** 3) - (b ** 3) = (a - b) *\
((a ** 2) + (a * b) + (b ** 2)) = {amount}"
    return result
def product_of_two_binomals(a:float, b:float, x:float) -> str:
    '''
    This function calculates product of two binomals algebraic identities.
    '''
    amount = (x ** 2) + ((a + b) * x) + (a * b)
    result = f"(x + a)(x + b) = (x ** 2) + ((a + b) * x) + (a * b) = {amount}"
    return result
user_request = input('''Which type of algebraic identity you're looking for?
Type I: square of a binomal -> (a + b) ** 2
Type II: square of a binomal -> (a - b) ** 2
Type III: difference of squares -> (a ** 2) - (b ** 2)
Type IV: cube of a binomal -> (a + b) ** 3
Type V: cube of a binomal -> (a - b) ** 3
Type VI: square of a trinomal -> (a + b + c) ** 2
Type VII: sum of cubes -> (a ** 3) + (b ** 3)
Type VIII: difference of cubes -> (a ** 3) - (b ** 3)
Type IX: product of two binomals -> (x + a)(x + b)
Enter the type in numbers, please.\n''')
user_request = user_request.upper()
if user_request == "I":
    a = float(input("Now, enter the value of a.\n"))
    b = float(input("And also, enter the value of b.\n"))
    last_result = square_of_a_binomal(a, b)
elif user_request == "II":
    a = float(input("Now, enter the value of a.\n"))
    b = float(input("And also, enter the value of b.\n"))
    last_result = square_of_a_binomal(a, b)
elif user_request == "III":
    a = float(input("Now, enter the value of a.\n"))
    b = float(input("And also, enter the value of b.\n"))
    last_result = difference_of_squares(a, b)
elif user_request == "IV":
    a = float(input("Now, enter the value of a.\n"))
    b = float(input("And also, enter the value of b.\n"))
    last_result = cube_of_a_binomal(a, b)
elif user_request == "V":
    a = float(input("Now, enter the value of a.\n"))
    b = float(input("And also, enter the value of b.\n"))
    last_result = cube_of_a_binomal(a, b)
elif user_request == "VI":
    a = float(input("Now, enter the value of a.\n"))
    b = float(input("And also, enter the value of b.\n"))
    c = float(input("How about the value of c?\n"))
    last_result = square_of_a_trinomal(a, b, c)
elif user_request == "VII":
    a = float(input("Now, enter the value of a.\n"))
    b = float(input("And also, enter the value of b.\n"))
    last_result = sum_of_cubes(a, b)
elif user_request == "VIII":
    a = float(input("Now, enter the value of a.\n"))
    b = float(input("And also, enter the value of b.\n"))
    last_result = difference_of_cubes(a, b)
elif user_request == "IX":
    a = float(input("Now, enter the value of a.\n"))
    b = float(input("And also, enter the value of b.\n"))
    x = float(input("How about the value of x?\n"))
    last_result = product_of_two_binomals(a, b, x)
print(last_result)
