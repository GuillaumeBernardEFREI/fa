from FA import FA
from math import ceil

def display(fa):
    
    for i in fa.nodes:
        alpha = len(fa.nodes[i])
        break

    columnswidth=[9]
    for i in range(alpha):
        columnswidth.append(5)        
        for j in fa.nodes:
            t = str(fa.nodes[j][i])
            t = max(5, len(t)-t.count("'")-t.count(" ")-t.count("[")-t.count("]"))
            if columnswidth[-1] < t:
                columnswidth[-1] = t

    print("   |"+" "*int((columnswidth[0]-5)/2)+'State'+" "*int(ceil((columnswidth[0]-5)/2)), end="")
    for i in range(alpha):
        if i != 0:
            char = chr(96+i)
        else:
            char = 'ε'
        print("|"+" "*int((columnswidth[i+1]-1)/2)+char+" "*int(ceil((columnswidth[i+1]-1)/2)), end="")

    print("|")
    print("   "+"-"*(sum(columnswidth)+1+len(columnswidth)))

    for i in fa.nodes:
        if (i in fa.terminals) and not(i in fa.entries): print(" <-", end="")
        if not (i in fa.terminals) and (i in fa.entries): print(" ->", end="")
        if (i in fa.terminals) and (i in fa.entries): print("<->", end="")
        if not (i in fa.terminals) and not (i in fa.entries): print("   ", end="")

        print("|"+" "*int((columnswidth[0]-len(i))/2)+i+" "*int(ceil((columnswidth[0]-len(i))/2))+"|", end="")
        for j in range(len(fa.nodes[i])):

            t = str(fa.nodes[i][j])
            t = len(t)-t.count("'") -t.count(" ")-t.count("[")-t.count("]")
            t = (columnswidth[j+1]-t)/2
            
            print(" "*int(t), end="")
            for k in range(len(fa.nodes[i][j])-1):
                print(fa.nodes[i][j][k], end=",")

            if len(fa.nodes[i][j]) > 0: print(fa.nodes[i][j][-1], end="")
            
            print(" "*int(ceil(t))+"|", end="")
        print("")
        print("   "+"-"*(sum(columnswidth)+len(columnswidth)+1))        

