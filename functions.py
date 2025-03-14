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


