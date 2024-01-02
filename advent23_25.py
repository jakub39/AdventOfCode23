import math
import networkx as nx

file = open('advent23_25.txt','r').read()
def solution(s):
    G  = nx.Graph()
    for line in s.strip().split('\n'):
        a,bs = line.split(': ')
        for b in bs.split():
            G.add_edge(a,b)
    G.remove_edges_from(nx.minimum_edge_cut(G))
    return math.prod(len(c) for c in nx.connected_components(G))

print(solution(file))