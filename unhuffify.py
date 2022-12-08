def unhuffify(B,H):
    decoded_str = ""
    head = H
    
    for bit in B:
        
        if (head.left == None and head.right == None):
            decoded_str += head.char
        
        if bit == 0:
            head = head.left
        else:
            head = head.right
        
        return decoded_str