# author LM (AMDG) 11/29/21

def basketball_points(free_throw, beyond, inside):
    free_throw = free_throw * 1
    beyond = beyond * 2
    inside = inside * 3
    total = free_throw + beyond + inside
    return(total)

free_throw = int(input("Enter the number of free throws: "))
beyond = int(input("Enter the number of points beyond three point line: "))
inside = int(input("Enter the amount of points inside the three point line: "))
print(basketball_points(free_throw, beyond, inside))
print(basketball_points(1, 1, 1) == 6)
print(basketball_points(1, 2, 3) == 14)
print(basketball_points(2, 2, 2) == 12)
