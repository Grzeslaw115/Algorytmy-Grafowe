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