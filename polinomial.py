def evaluate_polynomial(coefficients, n):
    result = 0
    for power, coeff in enumerate(coefficients):
        result += coeff * (n ** power)
    return result

def main():
    # Store the coefficients of the polynomial function f(x) = 4n^2 + 2n + 9 in an array
    coefficients = [9, 2, 4]  # The coefficients are in the order of n^0, n^1, n^2

    n = 5  # Given value of n

    result = evaluate_polynomial(coefficients, n)
    print(f"The value of f({n}) is: {result}")

if __name__ == "__main__":
    main()