from FA import FA

def remove_epsilons(FA:FA) -> FA:
    for node in FA.nodes:
        #for every epsilon transition
        print(FA.nodes[node][0])
        for transition in FA.nodes[node][0]:
            print(node,transition)
            #add the transitions to the one of the current node.
            #then delete the transition itself.
            FA.nodes=copytransitions(FA.nodes,node,transition)
            
            #Test if the node the transition leads to is a terminal
            if node not in FA.terminals and transition in FA.terminals:
                FA.terminals.append(node)
                FA.terminal_number+=1

        #resets everything and removes every transition inside (they have already been brought in)
        FA.nodes[node][0]=list()
    FA=remove_unused_nodes(FA)
    return FA

def copytransitions(nodes:dict[str,list[list]],copyto:str,copyfrom:str):
    #for each symbol in the alphabet
    for i in range(1,len(nodes[copyto])):
        #for each node that you can go to with the given symbol.
        for tocopy in nodes[copyfrom][i]:
            #if it's not already in the transition table (to not create duplicates)
            if tocopy not in nodes[copyto][i]:
                nodes[copyto][i].append(tocopy)
    
    return nodes

def remove_unused_nodes(FA:FA)-> FA:
    visited_nodes=[]
    for node in FA.entries:
        visited_nodes=recursive_exploration(visited_nodes,FA,node)
    
    node_to_destroy=[]
    for node in FA.nodes:
        if node not in visited_nodes:
            node_to_destroy.append(node)
    
    for node in node_to_destroy:
        FA.nodes.__delitem__(node)

    return FA

def recursive_exploration(visited:list,FA:FA,cur_node):
    if cur_node==str():
        return visited
    
    if cur_node not in visited:
        visited.append(cur_node)
        for transition in FA.nodes[cur_node]:
            for node in transition:
                visited=recursive_exploration(visited,FA,node)

    #The node has already been visited so it did not go into the loop.
    return visited
    