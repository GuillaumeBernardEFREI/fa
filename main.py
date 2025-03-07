from os import path
fa_folder = "automates"
class FA:
    def __init__(self,entries_number,terminal_number,entries,terminals,nodes):
        self.entries_number = entries_number
        self.entries=entries.copy()
        self.terminals=terminals.copy()
        self.terminal_number= terminal_number
        self.nodes = nodes.copy()
        return
    def __str__(self):
        return "---FA---\nnumber of entry :"+str(self.entries_number)+"\nentries :"+str(self.entries)+"\nnumber of terminal :"+str(self.terminal_number)+"\nterminals:"+str(self.terminals)+"\nnodes :"+str(self.nodes)
    def __eq__(self, value):
        return False
    

def split_with_alphabet(_str):
    for i in range(len(_str)):
        if not(_str[i] in "0123456789"):
            return [_str[:i],_str[i],str(int(_str[i+1:]))]



def load_fa(fa_path)->FA:
    f = open(path.join(fa_folder,fa_path),mode="r")
    alp = int(f.readline())
    n = int(f.readline())
    
    nodes={}
    
    for i in range(n):
        nodes[str(i)]=[]
        for j in range(alp):
            nodes[str(i)].append([])

    
    line = f.readline()
    entries_number = int(line.split(" ")[0])

    entries = []
    for i in line.split(" ")[1:]:
        entries.append(str(int(i)))
        
    line = f.readline()
    terminal_number = int(line.split(" ")[0])

    terminals=[]
    for i in line.split(" ")[1:]:
        terminals.append(str(int(i)))
    
    f.readline()
    lines = f.readlines()
    for line in lines:
        t = split_with_alphabet(line)
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



def is_determined(fa):
    return True


def is_minimized(fa):
    return


f = load_fa("auto1.txt")
f = complementarize(f)


print(f)
