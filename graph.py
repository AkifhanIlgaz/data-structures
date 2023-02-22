class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self,  u, v):
        x = set()
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])

        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def breadth_first_search(self, v):
        visited = []
        to_visit = []
        to_visit.append(v)
        while to_visit:
            newly_visited = to_visit.pop(0)
            visited.append(newly_visited)
            sorted_neighbors = sorted(self.graph[newly_visited])
            for neighbor in sorted_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
        return visited

    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        sorted_neighbors = sorted(self.graph[current_vertex])
        for neighbor in sorted_neighbors:
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]


def main():
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 4)
    graph.add_edge(4, 3)
    graph.add_edge(1, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)

    test(graph, 0, 1)
    test(graph, 0, 4)
    test(graph, 5, 1)
    test(graph, 3, 2)
    test(graph, 4, 4)
    test(graph, 3, 1)


def test(graph, u, v):
    print(f"{u} connects with {v}: {graph.edge_exists(u, v)}")


main()
