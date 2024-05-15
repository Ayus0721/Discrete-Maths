class Relation:
    def __init__(self, enter_matrix):
        self.matrix = enter_matrix
        self.size = len(enter_matrix)

    def is_reflexive(self):
        for i in range(self.size):
            if self.matrix[i][i] != 1:
                return False
        return True

    def is_symmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if i != j and self.matrix[i][j] == 1 and self.matrix[j][i] == 1:
                    return False
        return True

    def is_transitive(self):
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    if self.matrix[i][j] == 1 and self.matrix[j][k] == 1 and self.matrix[i][k] != 1:
                        return False
        return True

def check_relation_type(relation):
    if relation.is_reflexive() and relation.is_symmetric() and relation.is_transitive():
        return "Equivalence Relation"
    elif relation.is_reflexive() and relation.is_antisymmetric() and relation.is_transitive():
        return "Partial Order Relation"
    else:
        return "None"

def enter_matrix():
    lst = list(map(int, input("Enter all relations in the form of matrix values separated by a space: ").split()))
    row = int(input("Enter the number of rows or columns in your square matrix: "))
    matrix = [lst[i:i + row] for i in range(0, len(lst), row)]
    print("Your matrix is: \n", matrix)
    return matrix

relation = Relation(enter_matrix())

print("Is Reflexive:", relation.is_reflexive())
print("Is Symmetric:", relation.is_symmetric())
print("Is Antisymmetric:", relation.is_antisymmetric())
print("Is Transitive:", relation.is_transitive())
print("Type of Relation:", check_relation_type(relation))
