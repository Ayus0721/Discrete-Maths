import itertools

def generate_permutations(digits, with_repetition=False):
    if with_repetition:
        permutations = list(itertools.product(digits, repeat=len(digits)))
    else:
        permutations = list(itertools.permutations(digits))
    return permutations

def main():
    digits = [1, 2, 3]
    with_repetition = False

    permutations = generate_permutations(digits, with_repetition)

    print("Permutations:")
    for p in permutations:
        print(p)

if __name__ == "__main__":
    main()