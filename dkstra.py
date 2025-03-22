'''DIJKSTRA(G, w, s)
1 INITIALIZE-SINGLE-SOURCE(G, s)
2 S = Ø
3 Q = Ø
4 for each vertex u ∈ G.V
5   INSERT(Q, u)
6 while Q ≠ Ø
7   u = EXTRACT-MIN(Q)
8   S = S ∪ {u}
9   for each vertex v in G.Adj[u]
10	    RELAX(u, v, w)
11	    if the call of RELAX decreased v.d
12	    DECREASE-KEY(Q, v, v.d)

MLA 9th Edition (Modern Language Assoc.)
Thomas H. Cormen, et al. Introduction to Algorithms, Fourth Edition. The MIT Press, 2022.

APA 7th Edition (American Psychological Assoc.)
Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, &amp; Clifford Stein. (2022). Introduction to Algorithms, Fourth Edition: Vol. Fourth edition. The MIT Press.'''

def getMinIdx(l, seen):
    minVal = float('inf')
    minI = 0
    
    for i, v in enumerate(l):
        if v < minVal and i not in seen:
            minI = i
            minVal = v
            
    return minI

def dijkstra(graph, src):
    
    # the distances, initialize all to inf except src node
    dist = [float('inf') for _ in range(len(graph))]
    dist[src] = 0
    
    # set storing which nodes have not been visited
    non_visited_nodes = set()
    for i in range(len(graph)):
        non_visited_nodes.add(i)
        
    nodes_visited = []
    
    while len(non_visited_nodes) > 0:
            
        # get minimum of the currently unvisited nodes
        cur_node = getMinIdx(dist, nodes_visited)
        
        # store that we've visited it
        nodes_visited.append(cur_node)
        non_visited_nodes.remove(cur_node) # remove it form the set
        
        for dst, w in graph[cur_node].items(): # for each edge (dst and weight) at cur_node
            # if the distance to current node + weight of edge is less than the preivous shorteset distance to dst overwrite it
            if dist[cur_node] + w < dist[dst]: 
                dist[dst] = dist[cur_node] + w
    
    return dist

# Example graph represented as an adjacency list with weights.
graph = {
    0: {1: 1, 3: 2},
    1: {3: 1, 2: 2},
    2: {4: 1},
    3: {2: 3},
    4: {}
}

print(dijkstra(graph, 0))


