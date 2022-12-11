# Python like pseudocode not real python3
def is_braving(G, u, visited):
    u.mark = True
    visited[u] = u
    # loop over u's adjacency list
    for v in G.Adj[u]:
        # if u's adjacent v is already in visited it means more paths exist mark that v as false as it violates the rule
        if v in visited:
            v.mark = False
         
        elif v.mark == False:
            # if u is not in v's adjacency list visit v
            if not (u in G.Adj[v]):
                is_braving(G, v)
            # if u was in v's adjancency list and v was in u's adjancency list, the rule is violated, v must be marked false
            else:
                visited[v] = v

def is_brave_ancestor(G):
    
    visited = {}
    
    # initialize all vertices marks to false
    for v in G.V:
        v.mark = False
    
    # loop over vertices in G
    for v in G.V:
        # if vertex's mark is false and vertex is not in visited then visit vertex
        if v.mark == False and not (v in visited):
            is_braving(G, v, visited)
            
    for v in G.V:
        if v.mark == False:
            return False
    
    return True
        

   
        