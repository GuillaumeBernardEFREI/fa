from os import path
from FA import FA

def split_with_alphabet(_str):
    for i in range(len(_str)):
        if not(_str[i] in "0123456789"):
            return [_str[:i],_str[i],str(int(_str[i+1:]))]


def load_fa(fa_path,fa_folder)->FA:
    f = open(path.join(fa_folder,fa_path),mode="r")
    #symbols in the alphabet
    alp = int(f.readline().replace("\n",""))
    # Number of states
    n = int(f.readline().replace("\n",""))
    
    nodes={}
    
    #Create a dic of form {Q : [p.a.q]}
    for i in range(n):
        nodes[str(i)]=[]
        for j in range(alp):
            nodes[str(i)].append([])

    #initianlize the entries (I)
    line = f.readline().replace("\n","")
    entries_number = int(line.split(" ")[0])

    entries = []
    for i in line.split(" ")[1:]:
        entries.append(str(int(i)))
        
    #Initianalize the Terminals (T)
    line = f.readline().replace("\n","")
    terminal_number = int(line.split(" ")[0])

    terminals=[]
    for i in line.split(" ")[1:]:
        terminals.append(str(int(i)))
    
    #Initianalize the transitions
    f.readline().replace("\n","")
    lines = f.readlines()
    # for each transition
    for line in lines:
        line.replace("\n","")
        t = split_with_alphabet(line)
        # from the t[0] th node,
        # add a transition of the character t[1] (97 is the ord of 'a')(So we get a number from 0-25)
        # to the t[2] th node.
        nodes[t[0]][ord(t[1])-97].append(t[2])
    fa = FA(entries_number,terminal_number,entries,terminals,nodes)
    
    return fa


def complementarize(fa)->FA:
    _terminals=[str(i) for i in range(len(fa.nodes))]
    for i in fa.terminals:
        try:
            _terminals.remove(str(i))
        except:
            continue
    return FA(fa.entries_number,len(_terminals),fa.entries,_terminals,fa.nodes)


def determinize(fa)->FA:
    new_nodes = {} # the new dict for the new Fa
    list_states = []
    new_fa = FA(0,[''],0,[''],new_nodes) #create an empty FA in order to fill it from the previous one
    if not(fa.isdeterministic()):
        for state in fa.entries: #we are looking for each intial state
            current_state = state #intialize the current state with the initiale state
            for i in range(0,len(fa.nodes[state]),1): #we are looking for each transition
                add_initial = 0 #to be sure that we add only once intial/terminal number by state
                add_terminal = 0
                #if len(current_state[i]) > 1: #if there is an ambiguïtie with one transition
                next_state = ""
                for j in range(0,len(fa.nodes[current_state][i]),1): #The Transition
                    next_state += fa.nodes[current_state][i][j]
                    if fa.nodes[current_state][i][j] in fa.entries and add_initial == 0:#we have to check if the new_state is intial/termnial state
                        add_initial = 1
                        new_fa.entries_number +=1
                    if fa.nodes[current_state][i][j] in fa.terminals and add_terminal == 0:
                        add_terminal = 1
                        new_fa.terminal_number +=1
                if not (next_state in list_states): # look if the state already exist or not
                    list_states.append(next_state)
                    new_fa.nodes[current][i][0] = next_state
                    current = next_state
                    #new_fa.nodes[new_state] = new_nodes
        return new_fa
    else:
        return fa

