def find_solutions(n, C):
    solutions = []
    for x1 in range(C + 1):
        for x2 in range(C + 1):
            for x3 in range(C + 1):
                # Continue this pattern for n variables
                # To generalize this for n, you can use itertools.product
                if x1 + x2 + x3 == C:
                    solutions.append((x1, x2, x3))  # Add the solution to the list
    return solutions

def main():
    n = 3  # Number of variables
    C = 5  # Constant

    solutions = find_solutions(n, C)

    print(f"Solutions for x1 + x2 + x3 = {C}:")
    for sol in solutions:
        print(sol)

if __name__ == "__main__":
    main()