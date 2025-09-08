# merge two lists with ascending order
a = [-9, 1, 6, 8, 12]
b = [-7, 7 , 13, 15]
c = []

a_idx = 0
b_idx = 0
while not len(c) == (len(a)+len(b)):
    
    if a_idx >= len(a):
        c.append(b[b_idx])
        b_idx += 1
        continue
    
    if b_idx >= len(b):
        c.append(a[a_idx])
        a_idx += 1
        continue
     
    if a[a_idx] > b[b_idx]:
        c.append(b[b_idx])
        b_idx += 1
    else:
        c.append(a[a_idx])
        a_idx += 1
        
print(c)
    
