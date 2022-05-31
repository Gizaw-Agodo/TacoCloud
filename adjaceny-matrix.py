

class Graph():

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Adding edges
    def add_edge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    
    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print(val , end= '  '),
            print()


def main():
    myGraph = Graph(5)
    myGraph.add_edge(0, 1)
    myGraph.add_edge(0, 2)
    myGraph.add_edge(2, 1)
    myGraph.add_edge(2, 0)
    myGraph.add_edge(2, 3)

    myGraph.print_matrix()


if __name__ == '__main__':
    main()