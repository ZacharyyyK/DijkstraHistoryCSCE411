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

import heapq
                
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
    for i in graph:
        non_visited_nodes.add(i)
        
    nodes_visited = set()
    
    while len(non_visited_nodes) > 0:
            
        # get minimum of the currently unvisited nodes
        cur_node = getMinIdx(dist, nodes_visited)
        
        # store that we've visited it
        nodes_visited.add(cur_node)
        non_visited_nodes.remove(cur_node) # remove it form the set
        
        for dst, w in graph[cur_node].items(): # for each edge (dst and weight) at cur_node
            # if the distance to current node + weight of edge is less than the preivous shorteset distance to dst overwrite it
            if dist[cur_node] + w < dist[dst]: 
                dist[dst] = dist[cur_node] + w
    
    return dist    

def dijkstra2(graph, src):
    
    # the distances, initialize all to inf except src node
    dists = [float('inf') for _ in range(len(graph) + 1)]
    dists[src] = 0
    
    Q = []
    heapq.heappush(Q, [0, src]) # push only valid distance (src) into the minimum priority queue
    
    # set storing which nodes have not been visite
        
    nodes_visited = set()
    
    while len(Q) > 0:
        # get minimum of the currently unvisited nodes
        dist, cur_node = heapq.heappop(Q) # grab the node with the minimum distance and distance up to that node
                
        # store that we've visited it
        nodes_visited.add(cur_node) # add this node to our visited set
     
        for dst, w in graph[cur_node].items(): # for each edge (dst and weight) at cur_node
            # if the distance to current node + weight of edge is less than the preivous shorteset distance to dst overwrite it
            if dist + w < dists[dst]: 
                dists[dst] = dists[cur_node] + w  # rewrite as before
                heapq.heappush(Q, [dists[dst], dst]) # if we've rewrote this, then we have a new shortest path we need to account for
    
    return dists    


# Example graph represented as an adjacency list with weights.
graph = {
    0: {1: 1, 3: 2},
    1: {3: 1, 2: 2},
    2: {4: 1},
    3: {2: 3},
    4: {}
}

print(dijkstra2(graph, 0))

graph = {}

for i in range(1, 23):
    graph[i] = None
    
graph[1] = {2 : 1, 11 : 1}
graph[2] = {1 : 1, 3 : 1, 21 : 1}
graph[3] = {2 : 1, 4 : 1, 8 : 1}
graph[4] = {3 : 1, 5 : 1 }
graph[5] = {4 : 1, 7 : 1, 6 : 2, 22 : 1}
graph[6] = {5 : 1, 7 : 1}
graph[7] = {5 : 1, 6 : 1, 8 : 1}
graph[8] = {3 : 1, 7 : 1, 9 : 1}
graph[9] = {8 : 1, 10 : 1, 19 : 1}
graph[10] = {9 : 1, 11 : 1, 18 : 1} 
graph[11] = {10 : 1, 1 : 1, 12 : 2, 17 : 1}
graph[12] = {11 : 2, 13 : 2}
graph[13] = {12 : 2, 21 : 1, 14 : 2}
graph[14] = {13 : 2, 16 : 1, 15 : 1, 20 : 1}
graph[15] = {14 : 1}
graph[16] = {14 : 1, 17 : 1}
graph[17] = {16 : 1, 11 : 1}
graph[18] = {17 : 1, 19 : 2, 10 : 1}
graph[19] = { 18 : 2, 9 : 2}
graph[20] = {14 : 1, 21 : 1, 22 : 1}
graph[21] = {20 : 2, 22 : 2, 13 : 1, 2 : 1}
graph[22] = {20 : 1, 21 : 2, 5 : 1}

print(dijkstra2(graph, 1))


