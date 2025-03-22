from FA import FA
from math import ceil

def display(fa):
    """This display function is made to help us see an automaton.
    Sponsored by : https://www.compart.com/en/unicode/block/U+2500"""
    epsilon=fa.uses_epsilon()

    for i in fa.nodes:
        alpha = len(fa.nodes[i])
        break

    columnswidth=[9]
    for i in range(not epsilon,alpha):
        columnswidth.append(5)        
        for j in fa.nodes:
            t = str(fa.nodes[j][i])
            t = max(5, len(t)-t.count("'")-t.count(" ")-t.count("[")-t.count("]"))
            if columnswidth[-1] < t:
                columnswidth[-1] = t


    print("   "+"┌",end="")
    for column in columnswidth[:-1:]:
        print("─"*column+"┬",end="")
    print("─"*columnswidth[-1]+"┐")

    print("   │"+" "*int((columnswidth[0]-5)/2)+'State'+" "*int(ceil((columnswidth[0]-5)/2)), end="")
    for i in range(not epsilon,alpha):
        if i != 0:
            char = chr(96+i)
        else:
            char = 'ε'
        print("│"+" "*int((columnswidth[i+epsilon]-1)/2)+char+" "*int(ceil((columnswidth[i+epsilon]-1)/2)), end="")

    print("│")

    for i in fa.nodes:
    
        print("   "+"├",end="")
        for column in columnswidth[:-1:]:
            print("─"*column+"┼",end="")
        print("─"*columnswidth[-1]+"┤")

        if (i in fa.terminals) and not(i in fa.entries): print(" <-", end="")
        if not (i in fa.terminals) and (i in fa.entries): print(" ->", end="")
        if (i in fa.terminals) and (i in fa.entries): print("<->", end="")
        if not (i in fa.terminals) and not (i in fa.entries): print("   ", end="")

        print("│"+" "*int((columnswidth[0]-len(i))/2)+i+" "*int(ceil((columnswidth[0]-len(i))/2))+"│", end="")
        for j in range(not epsilon,len(fa.nodes[i])):

            t = str(fa.nodes[i][j])
            t = len(t)-t.count("'") -t.count(" ")-t.count("[")-t.count("]")
            t = (columnswidth[j+epsilon]-t)/2
            
            print(" "*int(t), end="")
            for k in range(len(fa.nodes[i][j])-1):
                print(fa.nodes[i][j][k], end=",")

            if len(fa.nodes[i][j]) > 0: print(fa.nodes[i][j][-1], end="")
            
            print(" "*int(ceil(t))+"│", end="")
        print("")

    print("   "+"└",end="")
    for column in columnswidth[:-1:]:
        print("─"*column+"┴",end="")
    print("─"*columnswidth[-1]+"┘")


