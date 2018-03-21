#! /usr/bin/python

visited = {}
adj_list = {}

class Graph(object):

    def __init__(self):
        self.visited = {}
        self.adj_list = {}

    def build_adjacent_list(self, matrix):
        for line in matrix:
            if not adj_list.has_key(line[0]):
                adj_list[line[0]] = [(line[1], line[2], 1)]
            else:
                adj_list[line[0]].append((line[1], line[2], 1))

    def remove_loop(self):
        def depth_first_find_loop(cur_node):
            visited[cur_node] = True
            print(str(cur_node) + " ")
            if adj_list.has_key(cur_node):
                for nb in adj_list[cur_node]:
                    if not nb[0] in visited:
                        depth_first_find_loop(nb[0])

        for key in adj_list:
            if not key in visited:
                depth_first_find_loop(key)

if __name__ == '__main__':
    mat = (
        (1, 3, 11),
        (1, 6, 10),
        (2, 4, 3),
        (4, 3, 4),
        (2, 3, 2),
        (5, 3, 3),
        (5, 4, 7),
        (5, 2, 5),
        (6, 4, 7),
        (2, 1, 9),
        (6, 5, 11),
        (6, 2, 1),
        (8, 9, 5)
    )
    g = Graph()
    g.build_adjacent_list(mat)
    print(adj_list)
    g.remove_loop()
