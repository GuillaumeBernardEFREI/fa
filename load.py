from os import path
from FA import FA

def split_with_alphabet(_str):
    for i in range(len(_str)):
        if not (_str[i] in "{.0123456789}"):
            return [_str[:i], _str[i], str(int(_str[i+1:]))]


def load_fa(fa_path, fa_folder) -> FA:
    f = open(path.join(fa_folder, fa_path), mode="r")
    # symbols in the alphabet
    alp = int(f.readline().replace("\n", ""))+1
    # Number of states
    n = int(f.readline().replace("\n", ""))
    
    nodes = {}
    
    # Create a dic of form {Q : [p.a.q]}
    for i in range(n):
        nodes[str(i)] = []
        for j in range(alp):
            nodes[str(i)].append([])

    # initianlize the entries (I)
    line = f.readline().replace("\n", "")
    entries_number = int(line.split(" ")[0])

    entries = []
    for i in line.split(" ")[1:]:
        entries.append(i)
        
    # Initianalize the Terminals (T)
    line = f.readline().replace("\n", "")
    terminal_number = int(line.split(" ")[0])

    terminals = []
    for i in line.split(" ")[1:]:
        terminals.append(i)
    
    # Initianalize the transitions
    f.readline().replace("\n", "")
    lines = f.readlines()
    # for each transition
    for line in lines:
        line.replace("\n", "")
        t = split_with_alphabet(line)
        # from the t[0] th node,
        # add a transition of the character t[1] (97 is the ord of 'a')(So we get a number from 0-25)
        # to the t[2] th node
        if t[1] == '!': nodes[t[0]][0].append(t[2])
        else: nodes[t[0]][ord(t[1])-96].append(t[2])
    fa = FA(entries_number, terminal_number, entries, terminals, nodes)
    
    return fa

