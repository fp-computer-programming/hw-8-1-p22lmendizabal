# author LM (AMDG) 12/5/21
def quadratic_formula(a, b, c):
    solution1 = (-b + ((b**2 - (4 * a * c))**.5)) / (2 * a)
    solution2 = (-b - ((b**2 - (4 * a * c))**.5)) / (2 * a)

    print(solution1, solution2)

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))
quadratic_formula(a, b, c)
