class Graph:

    def __init__(self,edges):
        self.edges = edges
        self.graph_dic = {}
        for start, end in self.edges:
            if start in self.graph_dic:
                self.graph_dic[start].append(end)

            else:
                self.graph_dic[start] = [end]

        print("Graph dict:",self.graph_dic)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dic:
            return []

        paths = []
        for node in self.graph_dic[start]:

            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path = []):
        path = path +  [start]


        if start == end:
            return path
        if start not in self.graph_dic:
            return None

        sp = None
        for node in self.graph_dic[start]:
            if node not in path:
                shortest_path = self.get_shortest_path(node, end, path)
                if shortest_path:
                    if sp is None or len(shortest_path) < len(sp):
                        sp = shortest_path

        return sp

        



if __name__ == '__main__':

    routes = [ ("Mumbai", "Paris"),
               ("Mumbai", "Dubai"),
               ("Paris", "Dubai"),
               ("Paris", "New York"),
               ("Dubai", "New York"),
               ("New York", "Toronto")
               ]


    route_graph = Graph(routes)
    start = "Mumbai"
    end = "New York"
    print(f"Paths between {start} and {end}:", route_graph.get_paths(start,end))
    print(f"Shortest Paths between {start} and {end}:", route_graph.get_shortest_path(start,end))


