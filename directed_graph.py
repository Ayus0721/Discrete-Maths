class DirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = {i: [] for i in range(num_vertices)}

    def add_edge(self, start_vertex, end_vertex):
        self.adjacency_list[start_vertex].append(end_vertex)

    def compute_degrees(self):
        in_degrees = [0] * self.num_vertices
        out_degrees = [0] * self.num_vertices

        for start_vertex in self.adjacency_list:
            out_degrees[start_vertex] = len(self.adjacency_list[start_vertex])
            for end_vertex in self.adjacency_list[start_vertex]:
                in_degrees[end_vertex] += 1

        return in_degrees, out_degrees

def main():
    num_vertices = 4  # Number of vertices in the graph
    graph = DirectedGraph(num_vertices)

    # Add edges to the graph
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)

    in_degrees, out_degrees = graph.compute_degrees()

    print("Vertex\tIn-Degree\tOut-Degree")
    for vertex in range(num_vertices):
        print(f"{vertex}\t{in_degrees[vertex]}\t\t{out_degrees[vertex]}")

if __name__ == "__main__":
    main()