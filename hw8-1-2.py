# author LM (AMDG) 12/5/21
def quadratic_formula(a, b, c):
    solution1 = (-b + ((b**2 - (4 * a * c))**.5)) / (2 * a)
    solution2 = (-b - ((b**2 - (4 * a * c))**.5)) / (2 * a)

    return(solution1, solution2)

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))
print(quadratic_formula(a, b, c))
print(quadratic_formula(2, 1, -528) == (16.0, -16.5))
print(quadratic_formula(1, -5, -14) == (7.0, -2.0))
print(quadratic_formula(1, -11, 28) == (7.0, 4.0))
