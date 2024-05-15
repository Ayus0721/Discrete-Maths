class Set:
    def __init__(self, elements):
        self.elements = set(elements)

    def is_member(self, element):
        return element in self.elements

    def powerset(self):
        from itertools import chain, combinations
        return list(chain.from_iterable(combinations(self.elements, r) for r in range(len(self.elements)+1)))

    def subset(self, other_set):
        return self.elements.issubset(other_set.elements)

    def union(self, other_set):
        return self.elements.union(other_set.elements)

    def intersection(self, other_set):
        return self.elements.intersection(other_set.elements)

    def complement(self, universal_set):
        return universal_set.elements - self.elements

    def set_difference(self, other_set):
        return self.elements.difference(other_set.elements)

    def symmetric_difference(self, other_set):
        return self.elements.symmetric_difference(other_set.elements)

    def cartesian_product(self, other_set):
        from itertools import product
        return set(product(self.elements, other_set.elements))

def main():
    set1 = Set([1, 2, 3])
    set2 = Set([2, 3, 4])
    universal_set = Set([1, 2, 3, 4, 5])

    while True:
        print("\n1. Is Member")
        print("2. Powerset")
        print("3. Subset")
        print("4. Union")
        print("5. Intersection")
        print("6. Complement")
        print("7. Set Difference")
        print("8. Symmetric Difference")
        print("9. Cartesian Product")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = int(input("Enter the element to check: "))
            print(set1.is_member(element))
        elif choice == 2:
            print(set1.powerset())
        elif choice == 3:
            print(set1.subset(set2))
        elif choice == 4:
            print(set1.union(set2))
        elif choice == 5:
            print(set1.intersection(set2))
        elif choice == 6:
            print(set1.complement(universal_set))
        elif choice == 7:
            print(set1.set_difference(set2))
        elif choice == 8:
            print(set1.symmetric_difference(set2))
        elif choice == 9:
            print(set1.cartesian_product(set2))
        elif choice == 0:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()