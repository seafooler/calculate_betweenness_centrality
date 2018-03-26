#! /usr/bin/python

# visited = {}
adj_list = {}

class Graph(object):

    # def __init__(self):
        # self.visited = {}
        # self.adj_list = {}

    # Build adjacent_list from matrix
    def build_adjacent_list(self, matrix):
        for line in matrix:
            if not adj_list.has_key(line[0]):
                adj_list[line[0]] = {}
                adj_list[line[0]][line[1]] = []
                (adj_list[line[0]][line[1]]).append([line[2], 1])
            elif not adj_list[line[0]].has_key(line[1]):
                adj_list[line[0]][line[1]] = []
                (adj_list[line[0]][line[1]]).append([line[2], 1])
            else:
                (adj_list[line[0]][line[1]]).append([line[2], 1])

    def remove_loop(self):
        def depth_first_find_loop(cur_node, edge_no, path, once_visited):
            once_visited[cur_node] = True
            path.append((cur_node, edge_no))
            if adj_list.has_key(cur_node):
                for to_node in adj_list[cur_node]:
                    for w, b in enumerate(adj_list[cur_node][to_node]):
                        # if adj_list[cur_node][nb_key][1] == 1:
                        if b[1] == 1:
                            # path.append((to_node, w))
                            # once_visited[to_node] = True
                            # if (not nb_key in once_visited) and (adj_list[cur_node][nb_key][1] == 1):
                            if not to_node in once_visited:
                                tmp_path = list(path)
                                tmp_visited = once_visited.copy()
                                depth_first_find_loop(to_node, w, tmp_path, tmp_visited)
                                # depth_first_find_loop(to_node, tmp_path, tmp_visited)
                            elif to_node == path[0][0]:
                                weight = []
                                tmp_path = list(path)
                                tmp_path.append(path[0])
                                tmp_path_len = len(tmp_path)
                                for i in range(0, tmp_path_len-1):
                                    weight.append(adj_list[tmp_path[i][0]][tmp_path[i+1][0]][tmp_path[i+1][1]][0])
                                flag = True
                                for i in range(0, len(weight)-1):
                                    if weight[i] >= weight[i+1]:
                                        flag = False
                                if flag:
                                    print(tmp_path)
                                    for i in range(0, tmp_path_len-1):
                                        for to_key, edges in adj_list[tmp_path[i][0]].items():
                                            for e in edges:
                                                if e[0] >= adj_list[tmp_path[i][0]][tmp_path[i+1][0]][tmp_path[i+1][1]][0]:
                                                    e[1] = 0
                                        # adj_list[tmp_path[i]][tmp_path[i+1]][1] = 0

        for key in adj_list:
            depth_first_find_loop(key, 0, [], {})

if __name__ == '__main__':
    mat = (
        (1, 3, 11),
        (1, 6, 10),
        (1, 6, 10),
        #(1, 6, 3), # (1, 6, 10),
        (2, 4, 3),
        (4, 3, 4),
        (2, 3, 2),
        (5, 3, 3),
        (5, 4, 7),
        (5, 2, 5),
        (5, 2, 5),
        (6, 4, 7),
        (2, 1, 9),
        (2, 1, 9),
        (6, 5, 11),
        (6, 5, 11),
        (6, 2, 1),
        #(6, 2, 5), # (6, 2, 1),
        (8, 9, 5)
    )
    g = Graph()
    g.build_adjacent_list(mat)
    print(adj_list)
    g.remove_loop()
    print(adj_list)
