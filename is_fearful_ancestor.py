# Python like pseudocode not real python 3
def is_fearful_ancestor(G, u):
    
    # Traverse set of vertices other than u and set their mark to false
    for v in G.V - {u}:
        v.mark = False
    
    # Set u's mark to true
    u.mark = True
    
    # instantiate an empty queue
    q = Queue()
    
    # enqueue u
    q.enqueue(u)
    
    # loop while queue is not empty
    while not q.is_empty():
        # dequeue vertex
        a = q.dequeue()
        # loop over the vertex's adjacency list
        for v in G.Adj[a]:
            # if current vertex's mark is false and current vertex is not a mark it true and enqueue it
            if v.mark == False and v != a:
                v.mark = True
                q.enqueue(v)
            # otherwise mark it as false
            else:
                v.mark = False
    
    # loop over all vertices in G and if one has false mark return false
    for v in G.V:
        if v.mark == False:
            return False
        

    return True
            
        
        