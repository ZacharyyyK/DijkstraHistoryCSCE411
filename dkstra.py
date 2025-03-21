'''DIJKSTRA(G, w, s)
1 INITIALIZE-SINGLE-SOURCE(G, s)
2 S = Ø
3 Q = Ø
4 for each vertex u ∈ G.V
5 INSERT(Q, u)
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