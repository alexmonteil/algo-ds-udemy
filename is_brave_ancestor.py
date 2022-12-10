# Python like pseudocode not real python3
def is_braving(G, u, visited):
    u.mark = True
    visited[u] = u
    for v in G.Adj[u]:
        if v.mark == False and v != u:
            if not (u in G.Adj[v]) and not (v in visited):
                is_braving(G, v)
            else:
                visited[v] = v
        elif v == u:
            v.mark = False

def is_brave_ancestor(G):
    
    visited = {}
    
    # initialize all vertices marks to false
    for v in G.V:
        v.mark = False
    
    # loop over vertices in G, for each vertex if the mark is false and it is not visited call is_braving on it.
    for v in G.V:
        if v.mark == False and not (v in visited):
            is_braving(G, v, visited)
            
    for v in G.V:
        if v.mark == False:
            return False
    
    return True
        

   
        