#from data import runtests

def my_solve(N, streets):
    print(f"Place: {N}, ulice: {len(streets)}")

    def build_graph(N, streets):
      G = [set() for _ in range(N + 1)]
      edges_weights = {}
      for a, b, t in streets:
        G[a].add(b)
        G[b].add(a)
        edges_weights[(a,b)] = t
        edges_weights[(b,a)] = t
      
      return G, edges_weights

    def is_transit(G, v):
      neighbors = G[v]

      for u in neighbors:
        for t in neighbors:
          if u == t:
            continue
          if u in G[t] or t in G[u]:
            continue
          
          common_neighbors = G[u].intersection(G[t])
          if len(common_neighbors) == 1:
            return True

      return False

    G, edges_weights = build_graph(N, streets)
    transit_squares = set()

    for i in range(1, N):
      if is_transit(G, i):
        transit_squares.add(i)

    return transit_squares

#runtests(my_solve)

graph = [
  (1,2, 3),
  (2,3, 5), (3,4, 1), (2,4, 3), (3,5, 6), (4,5, 9),
  (5,6, 1), (6,7, 5), (5,7, 8),
  (7,8, 5), (7,9, 11), (8,9, 7),
  (5,10, 7), (10,11, 3), (11,15, 2), (5,15, 3), (10,15, 8),
  (11,12, 13),
  (12,13, 5), (13,14, 2), (12,14, 2),
  (15,16, 7), (15,17, 7), (16,17, 4), (16,18, 5), (17,18, 6),
  (18,19, 13)
  ]

print(my_solve(19, graph))