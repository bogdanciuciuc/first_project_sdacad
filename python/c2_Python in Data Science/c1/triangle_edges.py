from math import sqrt

right_triangles = [[10, 5], [20, 30], [15, 25]]


def find_third_edge(edge_list):
    third_edge = []
    for item in edge_list:
        third_edge.append(sqrt(item[0]**2+item[1]**2))
    return third_edge


print(find_third_edge(right_triangles))


def find_third_edge(edge_list):
    for i in range(len(edge_list)):
        edge_list[i].append(int(sqrt(edge_list[i][0]**2+edge_list[i][1]**2)))
    return edge_list


print(find_third_edge(right_triangles))
